package main

import (
	"log"
	"net/http"
	"os"
	"time"

	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
	"github.com/joho/godotenv"
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
	"gorm.io/gorm/clause"
)

type Restoran struct {
	ID                 uint      `gorm:"primaryKey" json:"id"`
	PlaceID            string    `gorm:"uniqueIndex" json:"place_id"`
	Nama               string    `json:"nama"`
	Kategori           string    `json:"kategori"`
	Wilayah            string    `json:"wilayah"`
	Alamat             string    `json:"alamat"`
	Latitude           float64   `json:"latitude"`
	Longitude          float64   `json:"longitude"`
	Rating             float64   `json:"rating"`
	JumlahUlasan       int       `json:"jumlah_ulasan"`
	LinkGmaps          string    `json:"link_gmaps"`
	JenisMasakan       string    `json:"jenis_masakan"`
	RentangHarga       string    `json:"rentang_harga"`
	SumberData         string    `json:"sumber_data"`
	TerakhirDisinkron  time.Time `json:"terakhir_disinkron"`
}

var DB *gorm.DB

func main() {
	godotenv.Load()

	// Menggunakan SQLite lokal
	var err error
	DB, err = gorm.Open(sqlite.Open("kuliner.db"), &gorm.Config{})
	if err != nil {
		log.Println("Gagal koneksi ke SQLite:", err)
	} else {
		log.Println("Terkoneksi ke SQLite (kuliner.db)")
		DB.AutoMigrate(&Restoran{})
	}

	r := gin.Default()
	r.Use(cors.Default())

	r.GET("/health", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{"status": "Kuliner Service is running"})
	})

	r.GET("/api/kuliner", func(c *gin.Context) {
		wilayah := c.Query("wilayah")
		minRating := c.Query("min_rating")

		dbQuery := DB.Order("rating desc")
		
		if wilayah != "" {
			dbQuery = dbQuery.Where("wilayah = ?", wilayah)
		}
		if minRating != "" {
			dbQuery = dbQuery.Where("rating >= ?", minRating)
		}

		var restorans []Restoran
		dbQuery.Find(&restorans)

		c.JSON(http.StatusOK, restorans)
	})

	// Webhook endpoint (Pengganti RabbitMQ)
	r.POST("/webhook/restoran-sync", func(c *gin.Context) {
		var resto Restoran
		if err := c.ShouldBindJSON(&resto); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}

		resto.SumberData = "Google Places API"
		resto.TerakhirDisinkron = time.Now()

		// Upsert based on PlaceID
		DB.Clauses(clause.OnConflict{
			Columns:   []clause.Column{{Name: "place_id"}},
			DoUpdates: clause.AssignmentColumns([]string{"nama", "kategori", "wilayah", "alamat", "latitude", "longitude", "rating", "jumlah_ulasan", "link_gmaps", "terakhir_disinkron"}),
		}).Create(&resto)

		log.Println("Update dari Harvester via Webhook:", resto.Nama)
		c.JSON(http.StatusOK, gin.H{"message": "Data tersinkronisasi"})
	})

	port := os.Getenv("PORT")
	if port == "" {
		port = "8003"
	}
	r.Run(":" + port)
}

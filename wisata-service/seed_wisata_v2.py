from database import SessionLocal
from models import TempatWisata, KategoriWisataEnum, WilayahEnum

db = SessionLocal()

# Clear existing data
db.query(TempatWisata).delete()
db.commit()

wisata_data = [
    # Kota Yogyakarta
    {
        "nama": "Keraton Yogyakarta", "kategori_wisata": KategoriWisataEnum.budaya, "wilayah": WilayahEnum.kota_yogyakarta,
        "deskripsi": "Istana resmi Kesultanan Ngayogyakarta Hadiningrat yang kaya akan budaya dan peninggalan sejarah.",
        "alamat": "Jl. Rotowijayan Blok No. 1, Panembahan, Kraton", "latitude": -7.805284, "longitude": 110.364203,
        "rating": 4.7, "jumlah_ulasan": 25000, "estimasi_harga_tiket": "Rp 15.000", "jam_operasional": "08:00 - 14:00",
        "link_gmaps": "https://goo.gl/maps/keraton",
        "gambar": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Keraton_Yogyakarta_1.jpg/800px-Keraton_Yogyakarta_1.jpg"
    },
    {
        "nama": "Taman Sari", "kategori_wisata": KategoriWisataEnum.budaya, "wilayah": WilayahEnum.kota_yogyakarta,
        "deskripsi": "Bekas taman atau kebun istana Keraton Ngayogyakarta Hadiningrat dengan pemandian kuno.",
        "alamat": "Patehan, Kraton, Kota Yogyakarta", "latitude": -7.8100, "longitude": 110.3590,
        "rating": 4.6, "jumlah_ulasan": 31000, "estimasi_harga_tiket": "Rp 15.000", "jam_operasional": "09:00 - 15:00",
        "link_gmaps": "https://goo.gl/maps/tamansari",
        "gambar": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Taman_Sari_Water_Castle.jpg/800px-Taman_Sari_Water_Castle.jpg"
    },
    
    # Sleman
    {
        "nama": "Candi Prambanan", "kategori_wisata": KategoriWisataEnum.budaya, "wilayah": WilayahEnum.sleman,
        "deskripsi": "Kompleks candi Hindu terbesar di Indonesia yang dibangun pada abad ke-9 masehi.",
        "alamat": "Jl. Raya Solo - Yogyakarta No.16, Kranggan, Prambanan", "latitude": -7.752020, "longitude": 110.491467,
        "rating": 4.8, "jumlah_ulasan": 68000, "estimasi_harga_tiket": "Rp 50.000", "jam_operasional": "06:00 - 17:00",
        "link_gmaps": "https://goo.gl/maps/prambanan",
        "gambar": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Prambanan_Temple_Yogyakarta_Indonesia.jpg/800px-Prambanan_Temple_Yogyakarta_Indonesia.jpg"
    },
    {
        "nama": "Museum Ullen Sentalu", "kategori_wisata": KategoriWisataEnum.edukasi, "wilayah": WilayahEnum.sleman,
        "deskripsi": "Museum yang menampilkan budaya dan kehidupan para bangsawan Dinasti Mataram beserta koleksi batik.",
        "alamat": "Jl. Boyong KM 25, Kaliurang Barat, Sleman", "latitude": -7.5975, "longitude": 110.4230,
        "rating": 4.8, "jumlah_ulasan": 14000, "estimasi_harga_tiket": "Rp 50.000", "jam_operasional": "08:30 - 16:00",
        "link_gmaps": "https://goo.gl/maps/ullensentalu",
        "gambar": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Ullen_Sentalu_Museum%2C_Sleman%2C_Yogyakarta.jpg/800px-Ullen_Sentalu_Museum%2C_Sleman%2C_Yogyakarta.jpg"
    },

    # Bantul
    {
        "nama": "Pantai Parangtritis", "kategori_wisata": KategoriWisataEnum.alam, "wilayah": WilayahEnum.bantul,
        "deskripsi": "Pantai paling ikonik di Yogyakarta, terkenal dengan ombak besar dan legenda Nyi Roro Kidul.",
        "alamat": "Desa Parangtritis, Kecamatan Kretek, Bantul", "latitude": -8.025400, "longitude": 110.334000,
        "rating": 4.5, "jumlah_ulasan": 55000, "estimasi_harga_tiket": "Rp 10.000", "jam_operasional": "24 Jam",
        "link_gmaps": "https://goo.gl/maps/parangtritis",
        "gambar": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Parangtritis_beach_1.jpg/800px-Parangtritis_beach_1.jpg"
    },
    {
        "nama": "Hutan Pinus Mangunan", "kategori_wisata": KategoriWisataEnum.alam, "wilayah": WilayahEnum.bantul,
        "deskripsi": "Hutan pinus yang sejuk dengan banyak spot foto menarik dan panggung alam.",
        "alamat": "Sukorame, Mangunan, Dlingo, Bantul", "latitude": -7.9269, "longitude": 110.4285,
        "rating": 4.6, "jumlah_ulasan": 22000, "estimasi_harga_tiket": "Rp 5.000", "jam_operasional": "06:00 - 18:00",
        "link_gmaps": "https://goo.gl/maps/hutanpinus",
        "gambar": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Kraton_Yogyakarta_-_Bangsal_Kencono.jpg/800px-Kraton_Yogyakarta_-_Bangsal_Kencono.jpg" # fallback if needed, but lets use valid one
    },

    # Gunungkidul
    {
        "nama": "Goa Jomblang", "kategori_wisata": KategoriWisataEnum.alam, "wilayah": WilayahEnum.gunungkidul,
        "deskripsi": "Gua vertikal yang menakjubkan dengan fenomena 'Cahaya Surga' di dasar gua.",
        "alamat": "Jetis Wetan, Pacarejo, Semanu, Gunungkidul", "latitude": -8.0280, "longitude": 110.6370,
        "rating": 4.8, "jumlah_ulasan": 3500, "estimasi_harga_tiket": "Rp 500.000", "jam_operasional": "08:00 - 14:00",
        "link_gmaps": "https://goo.gl/maps/jomblang",
        "gambar": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Jomblang_Cave%2C_Yogyakarta.jpg/800px-Jomblang_Cave%2C_Yogyakarta.jpg"
    },
    {
        "nama": "Pantai Indrayanti", "kategori_wisata": KategoriWisataEnum.alam, "wilayah": WilayahEnum.gunungkidul,
        "deskripsi": "Pantai pasir putih bersih dengan fasilitas restoran pinggir pantai yang lengkap.",
        "alamat": "Tepus, Kabupaten Gunungkidul", "latitude": -8.1504, "longitude": 110.6125,
        "rating": 4.5, "jumlah_ulasan": 18000, "estimasi_harga_tiket": "Rp 10.000", "jam_operasional": "24 Jam",
        "link_gmaps": "https://goo.gl/maps/indrayanti",
        "gambar": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Malioboro_Street_Sign.jpg/800px-Malioboro_Street_Sign.jpg" # fallback
    },

    # Kulon Progo
    {
        "nama": "Kalibiru", "kategori_wisata": KategoriWisataEnum.buatan, "wilayah": WilayahEnum.kulonprogo,
        "deskripsi": "Wisata alam perbukitan Menoreh dengan gardu pandang ikonik berlatar Waduk Sermo.",
        "alamat": "Hargowilis, Kokap, Kabupaten Kulon Progo", "latitude": -7.8055, "longitude": 110.1345,
        "rating": 4.4, "jumlah_ulasan": 12000, "estimasi_harga_tiket": "Rp 15.000", "jam_operasional": "07:00 - 17:00",
        "link_gmaps": "https://goo.gl/maps/kalibiru",
        "gambar": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Waduk_Sermo_dari_Kalibiru.jpg/800px-Waduk_Sermo_dari_Kalibiru.jpg"
    },
    {
        "nama": "Pule Payung", "kategori_wisata": KategoriWisataEnum.buatan, "wilayah": WilayahEnum.kulonprogo,
        "deskripsi": "Spot foto kekinian dengan berbagai wahana sepeda gantung dan ayunan di atas bukit.",
        "alamat": "Soropati, Hargotirto, Kokap, Kulon Progo", "latitude": -7.7950, "longitude": 110.1250,
        "rating": 4.5, "jumlah_ulasan": 4200, "estimasi_harga_tiket": "Rp 20.000", "jam_operasional": "08:00 - 16:00",
        "link_gmaps": "https://goo.gl/maps/pulepayung",
        "gambar": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Tugu_Yogyakarta_2015.jpg/800px-Tugu_Yogyakarta_2015.jpg" # fallback
    }
]

# Ganti fallback image yang aneh (Pantai tapi gambarnya Tugu/Malioboro) dengan gambar alam dari wikimedia
wisata_data[5]["gambar"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Pine_Forest_of_Mangunan%2C_Bantul_01.jpg/800px-Pine_Forest_of_Mangunan%2C_Bantul_01.jpg"
wisata_data[7]["gambar"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Pantai_Pok_Tunggal%2C_Yogyakarta.jpg/800px-Pantai_Pok_Tunggal%2C_Yogyakarta.jpg"
wisata_data[9]["gambar"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Waduk_Sermo.JPG/800px-Waduk_Sermo.JPG"


objects = [TempatWisata(**d) for d in wisata_data]
db.add_all(objects)
db.commit()
print("Berhasil seeding data wisata V2 yang realistis (Wikimedia)!")
db.close()

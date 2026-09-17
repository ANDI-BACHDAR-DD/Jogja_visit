import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import TempatWisata, Base

# Hubungkan ke SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./wisata.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Buat tabel jika belum ada
Base.metadata.create_all(bind=engine)

db = SessionLocal()

wisata_data = [
    {
        "nama": "Candi Prambanan",
        "kategori_wisata": "Budaya/Heritage",
        "wilayah": "Sleman",
        "deskripsi": "Mahakarya arsitektur Hindu abad ke-9, Candi Prambanan merupakan candi Hindu terbesar di Indonesia yang menjulang setinggi 47 meter. Relief Ramayana terukir indah di dinding candi, menceritakan kisah epik legendaris.",
        "latitude": -7.752,
        "longitude": 110.491,
        "rating": 4.8,
        "jumlah_ulasan": 5000,
        "link_gmaps": "https://maps.google.com/?q=-7.752,110.491",
        "gambar": "https://images.unsplash.com/photo-1596404981882-747d4e5ff012?auto=format&fit=crop&q=80&w=800",
        "sumber_data": "Seed Data"
    },
    {
        "nama": "Keraton Yogyakarta",
        "kategori_wisata": "Budaya/Heritage",
        "wilayah": "Kota Yogyakarta",
        "deskripsi": "Jantung kebudayaan Jawa yang masih aktif. Sebagai istana resmi Kesultanan Ngayogyakarta Hadiningrat, tempat ini menyimpan pusaka keraton, kereta kencana, dan sejarah panjang Mataram Islam.",
        "latitude": -7.805,
        "longitude": 110.364,
        "rating": 4.7,
        "jumlah_ulasan": 4000,
        "link_gmaps": "https://maps.google.com/?q=-7.805,110.364",
        "gambar": "https://images.unsplash.com/photo-1549473889-14f364a66e4a?auto=format&fit=crop&q=80&w=800",
        "sumber_data": "Seed Data"
    },
    {
        "nama": "Pantai Parangtritis",
        "kategori_wisata": "Alam",
        "wilayah": "Bantul",
        "deskripsi": "Pantai ikonik Jogja yang terkenal dengan ombak besarnya, gumuk pasir pelangkus, dan pemandangan sunset magis. Pengunjung dapat menyewa ATV atau naik delman menyusuri garis pantai.",
        "latitude": -8.025,
        "longitude": 110.33,
        "rating": 4.5,
        "jumlah_ulasan": 3500,
        "link_gmaps": "https://maps.google.com/?q=-8.025,110.33",
        "gambar": "https://images.unsplash.com/photo-1614713702517-8eeb960fcdbb?auto=format&fit=crop&q=80&w=800",
        "sumber_data": "Seed Data"
    },
    {
        "nama": "Goa Jomblang",
        "kategori_wisata": "Alam",
        "wilayah": "Gunungkidul",
        "deskripsi": "Gua vertikal sedalam 60 meter yang terbentuk dari runtuhnya tanah (sinkhole). Keajaiban utamanya adalah 'cahaya surga' yang menyinari dasar gua yang dipenuhi hutan purba pada siang hari.",
        "latitude": -8.028,
        "longitude": 110.638,
        "rating": 4.9,
        "jumlah_ulasan": 1200,
        "link_gmaps": "https://maps.google.com/?q=-8.028,110.638",
        "gambar": "https://images.unsplash.com/photo-1610486821360-64ab7f564dc7?auto=format&fit=crop&q=80&w=800",
        "sumber_data": "Seed Data"
    },
    {
        "nama": "Air Terjun Kedung Pedut",
        "kategori_wisata": "Alam",
        "wilayah": "Kulon Progo",
        "deskripsi": "Taman bermain air alami dengan air terjun dua warna (putih jernih dan tosca). Kolam-kolam alami bertingkat sangat cocok untuk berenang dan bermain air di tengah hutan yang asri.",
        "latitude": -7.766,
        "longitude": 110.134,
        "rating": 4.7,
        "jumlah_ulasan": 1800,
        "link_gmaps": "https://maps.google.com/?q=-7.766,110.134",
        "gambar": "https://images.unsplash.com/photo-1433086966358-54859d0ed716?auto=format&fit=crop&q=80&w=800",
        "sumber_data": "Seed Data"
    }
]

# Hapus data lama agar tidak duplikat saat di-run ulang
db.query(TempatWisata).delete()

# Masukkan data baru
for w in wisata_data:
    item = TempatWisata(**w)
    db.add(item)

db.commit()
db.close()

print("Data wisata berhasil disemai (seed) ke SQLite lokal!")

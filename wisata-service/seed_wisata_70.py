import urllib.parse
import random

print("Generating 70 Wisata per region...")

regions = ["Kota Yogyakarta", "Sleman", "Bantul", "Gunungkidul", "Kulon Progo"]

base_coords = {
    "Kota Yogyakarta": (-7.7956, 110.3695),
    "Sleman": (-7.7156, 110.3556),
    "Bantul": (-7.8856, 110.3256),
    "Gunungkidul": (-7.9656, 110.6056),
    "Kulon Progo": (-7.8256, 110.1556)
}

wisata_data = []

kat_wisata_list = ["Alam", "Budaya/Heritage", "Edukasi", "Religi", "Buatan/Instagramable"]
wisata_names = ["Taman", "Candi", "Pantai", "Goa", "Museum", "Bukit", "Hutan", "Air Terjun", "Desa Wisata", "Kampung", "Monumen", "Alun-Alun", "Puncak", "Embung", "Waduk", "Tebing", "Gumuk", "Kebun", "Gedung", "Situs", "Istana", "Keraton", "Telaga", "Sendang", "Curug"]
wisata_suf = ["Indah", "Asri", "Lestari", "Nusantara", "Pusaka", "Harapan", "Jaya", "Bakti", "Kencana", "Makmur", "Sejahtera", "Damai", "Bening", "Pesona", "Mulia", "Kuning", "Putih", "Biru", "Selatan", "Utara", "Timur", "Barat", "Tengah", "Agung", "Raya", "Bagus"]

for wil in regions:
    lat_b, lon_b = base_coords[wil]
    
    # Generate 70 Wisata per region
    for i in range(70):
        lat = lat_b + random.uniform(-0.15, 0.15)
        lon = lon_b + random.uniform(-0.15, 0.15)
        kat = random.choice(kat_wisata_list)
        
        if "Budaya" in kat or "Religi" in kat:
            kw = "temple"
        elif "Edukasi" in kat or "Buatan" in kat:
            kw = "museum"
        else:
            kw = "nature"
            
        img = f"https://loremflickr.com/800/600/indonesia,{kw}?random={random.randint(1,5000)}"
        nama = f"{random.choice(wisata_names)} {random.choice(wisata_suf)} {random.randint(1,999)}"
        
        # Link gmaps menggunakan nama destinasi agar tidak ambigu
        query_text = f"{nama} {wil}"
        encoded_query = urllib.parse.quote(query_text)
        link_gmaps = f"https://www.google.com/maps/search/?api=1&query={encoded_query}"
        
        wisata_data.append({
            "nama": nama,
            "kategori_wisata": kat,
            "wilayah": wil,
            "deskripsi": f"Destinasi {kat.lower()} yang menakjubkan di {wil}. Menawarkan pemandangan dan pengalaman yang tak terlupakan bagi setiap pengunjung yang datang. Buka setiap hari dengan fasilitas yang lengkap dan nyaman untuk keluarga.",
            "alamat": f"Jl. Pariwisata No. {random.randint(1,999)}, {wil}",
            "latitude": lat,
            "longitude": lon,
            "link_gmaps": link_gmaps,
            "rating": round(random.uniform(4.0, 5.0), 1),
            "jumlah_ulasan": random.randint(100, 25000),
            "estimasi_harga_tiket": f"Rp {random.choice([10, 15, 20, 25, 30, 35, 40, 50, 75, 100])}.000",
            "jam_operasional": "08:00 - 17:00",
            "gambar": img
        })

print("Menyimpan ke SQLite...")
from database import SessionLocal, engine
from models import TempatWisata, Base

Base.metadata.create_all(bind=engine)
db = SessionLocal()
db.query(TempatWisata).delete()
db.commit()

objects = [TempatWisata(**d) for d in wisata_data]
db.add_all(objects)
db.commit()
db.close()

print(f"Berhasil! Total Wisata: {len(wisata_data)} (70 per wilayah)")

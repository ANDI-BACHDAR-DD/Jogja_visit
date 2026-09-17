import requests
import json
import random
import time

print("Generating Mega Seed Data v2 (100 per category)...")

regions = ["Kota Yogyakarta", "Sleman", "Bantul", "Gunungkidul", "Kulon Progo"]

# Real image pools for categories
img_alam = [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Merapi_Mountain_Yogyakarta.jpg/800px-Merapi_Mountain_Yogyakarta.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Parangtritis_Beach_Yogyakarta.jpg/800px-Parangtritis_Beach_Yogyakarta.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Timang_Beach.jpg/800px-Timang_Beach.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Indrayanti_Beach.jpg/800px-Indrayanti_Beach.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Pindul_Cave.jpg/800px-Pindul_Cave.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Jomblang_Cave_2.jpg/800px-Jomblang_Cave_2.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Kalibiru_National_Park.jpg/800px-Kalibiru_National_Park.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Pine_Forest_Mangunan.jpg/800px-Pine_Forest_Mangunan.jpg"
]

img_budaya = [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Yogyakarta_Indonesia_Tugu-Yogyakarta-02.jpg/800px-Yogyakarta_Indonesia_Tugu-Yogyakarta-02.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Prambanan_Temple_Yogyakarta_Indonesia.jpg/800px-Prambanan_Temple_Yogyakarta_Indonesia.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Kraton_Yogyakarta_2.jpg/800px-Kraton_Yogyakarta_2.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Taman_Sari_Water_Castle.jpg/800px-Taman_Sari_Water_Castle.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Ratu_Boko_Temple.jpg/800px-Ratu_Boko_Temple.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Malioboro_Street.jpg/800px-Malioboro_Street.jpg"
]

img_kuliner = [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Gudeg_Yogyakarta.jpg/800px-Gudeg_Yogyakarta.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Sate_Klatak.jpg/800px-Sate_Klatak.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Bakpia_Pathok.jpg/800px-Bakpia_Pathok.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Kopi_Joss.jpg/800px-Kopi_Joss.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Mie_Lethek.jpg/800px-Mie_Lethek.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Mangut_Lele.jpg/800px-Mangut_Lele.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Soto_Kadipiro.jpg/800px-Soto_Kadipiro.jpg"
]

img_rental = [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Toyota_Avanza_1.5_G_W101RE_%2820230219%29.jpg/800px-Toyota_Avanza_1.5_G_W101RE_%2820230219%29.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/2018_Toyota_Innova.jpg/800px-2018_Toyota_Innova.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Honda_Brio_Satya_E.jpg/800px-Honda_Brio_Satya_E.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/2019_Honda_Vario_150.jpg/800px-2019_Honda_Vario_150.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Yamaha_NMAX_155.jpg/800px-Yamaha_NMAX_155.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Toyota_HiAce_Commuter.jpg/800px-Toyota_HiAce_Commuter.jpg"
]

# Base coordinates for regions to generate random nearby coordinates
base_coords = {
    "Kota Yogyakarta": (-7.7956, 110.3695),
    "Sleman": (-7.7156, 110.3556),
    "Bantul": (-7.8856, 110.3256),
    "Gunungkidul": (-7.9656, 110.6056),
    "Kulon Progo": (-7.8256, 110.1556)
}

wisata_data = []
kuliner_data = []
rental_data = []

kat_wisata_list = ["Alam", "Budaya/Heritage", "Edukasi", "Religi", "Buatan/Instagramable"]
jenis_masakan_list = ["Gudeg", "Sate", "Soto", "Kopi & Angkringan", "Seafood", "Jawa Klasik", "Olahan Jamur", "Bakmi"]
jenis_kendaraan_list = ["Mobil MPV", "Motor Matic", "Mobil City Car", "Minibus"]

wisata_names = ["Taman", "Candi", "Pantai", "Goa", "Museum", "Bukit", "Hutan", "Air Terjun", "Desa Wisata", "Kampung", "Monumen", "Alun-Alun", "Puncak", "Embung", "Waduk", "Tebing", "Gumuk", "Kebun", "Gedung", "Situs"]
wisata_suf = ["Indah", "Asri", "Lestari", "Nusantara", "Pusaka", "Harapan", "Jaya", "Bakti", "Kencana", "Makmur", "Sejahtera", "Damai", "Bening", "Pesona", "Mulia", "Kuning", "Putih", "Biru", "Selatan", "Utara"]

kuliner_names = ["Warung", "Resto", "Sate", "Soto", "Gudeg", "Angkringan", "Kopi", "Bakmi", "Pecel", "Rumah Makan", "Lesehan", "Kedai", "Cafe", "Depot", "Pusat Oleh-oleh"]
kuliner_suf = ["Pak Budi", "Bu Narti", "Mbah Joyo", "Yu Djum", "Pak Pong", "Mbah Marto", "Pak Min", "Bu Tini", "Lek Man", "Mas Yono", "Mbak Sari", "Kang Ozan", "Bu Ageng", "Pak Slamet", "Mbah Carik"]

rental_names = ["Jogja", "Trans", "Rent", "Auto", "Motor", "Car", "Sewa", "Transport", "Mandiri", "Berkah", "Jaya", "Lancar", "Amanah", "Pesona", "Wisata"]
rental_suf = ["Rental", "Trans", "Car Rent", "Motorbike", "Tour", "Travel", "Rent a Car", "Sewa Motor", "Garage", "Drive"]

for wil in regions:
    lat_b, lon_b = base_coords[wil]
    
    # Generate 20 Wisata per region
    for i in range(20):
        lat = lat_b + random.uniform(-0.05, 0.05)
        lon = lon_b + random.uniform(-0.05, 0.05)
        kat = random.choice(kat_wisata_list)
        img = random.choice(img_budaya) if "Budaya" in kat or "Edukasi" in kat or "Religi" in kat else random.choice(img_alam)
        nama = f"{random.choice(wisata_names)} {random.choice(wisata_suf)} {i+1}"
        
        wisata_data.append({
            "nama": nama,
            "kategori_wisata": kat,
            "wilayah": wil,
            "deskripsi": f"Destinasi {kat.lower()} yang menakjubkan di {wil}. Menawarkan pemandangan dan pengalaman yang tak terlupakan bagi setiap pengunjung yang datang. Buka setiap hari dengan fasilitas yang lengkap dan nyaman untuk keluarga.",
            "alamat": f"Jl. Pariwisata No. {random.randint(1,99)}, {wil}",
            "latitude": lat,
            "longitude": lon,
            "link_gmaps": f"https://www.google.com/maps/search/?api=1&query={lat},{lon}",
            "rating": round(random.uniform(4.2, 4.9), 1),
            "jumlah_ulasan": random.randint(100, 15000),
            "estimasi_harga_tiket": f"Rp {random.choice([10, 15, 20, 25, 30, 50])}.000",
            "jam_operasional": "08:00 - 17:00",
            "gambar": img
        })

    # Generate 20 Kuliner per region
    for i in range(20):
        lat = lat_b + random.uniform(-0.05, 0.05)
        lon = lon_b + random.uniform(-0.05, 0.05)
        nama = f"{random.choice(kuliner_names)} {random.choice(kuliner_suf)} {i+1}"
        
        kuliner_data.append({
            "place_id": f"KUL_{wil.replace(' ', '_')}_{i}",
            "nama": nama,
            "kategori": random.choice(["Restoran", "Warung", "Angkringan", "Kafe"]),
            "wilayah": wil,
            "alamat": f"Jl. Kuliner No. {random.randint(1,99)}, {wil}",
            "latitude": lat,
            "longitude": lon,
            "rating": round(random.uniform(4.0, 4.9), 1),
            "jumlah_ulasan": random.randint(50, 10000),
            "jenis_masakan": random.choice(jenis_masakan_list),
            "rentang_harga": f"Rp {random.choice([10, 15, 20, 30, 40, 50])}.000",
            "link_gmaps": f"https://www.google.com/maps/search/?api=1&query={lat},{lon}",
            "gambar": random.choice(img_kuliner)
        })

    # Generate 20 Rental per region
    for i in range(20):
        lat = lat_b + random.uniform(-0.05, 0.05)
        lon = lon_b + random.uniform(-0.05, 0.05)
        nama = f"{random.choice(rental_names)} {random.choice(rental_suf)} {wil.split()[0]} {i+1}"
        jk = random.choice(jenis_kendaraan_list)
        
        rental_data.append({
            "nama": nama,
            "wilayah": wil,
            "jenis_kendaraan": jk,
            "harga": f"Rp {random.choice([70, 80, 100])}.000/hari" if "Motor" in jk else f"Rp {random.choice([250, 300, 350, 400])}.000/hari",
            "rating": round(random.uniform(4.3, 5.0), 1),
            "jumlah_ulasan": random.randint(20, 2000),
            "tautan_wa": f"https://wa.me/628123456789{random.randint(0,9)}",
            "alamat": f"Jl. Rental Kendaraan No. {random.randint(1,99)}, {wil}",
            "latitude": lat,
            "longitude": lon,
            "link_gmaps": f"https://www.google.com/maps/search/?api=1&query={lat},{lon}",
            "gambar": random.choice(img_rental)
        })


print("Seeding Wisata (SQLAlchemy)...")
import os
import sys

# Because we run from root, we need to add wisata-service to path
sys.path.append(os.path.abspath("wisata-service"))
from database import SessionLocal
from models import TempatWisata

db = SessionLocal()
db.query(TempatWisata).delete()
db.commit()

objects = [TempatWisata(**d) for d in wisata_data]
db.add_all(objects)
db.commit()
db.close()

print("Seeding Kuliner...")
try:
    requests.post("http://localhost:4000/api/kuliner/webhook", json={"type": "SEED", "data": kuliner_data})
except Exception as e:
    print("Kuliner webhook err:", e)

print("Seeding Rental...")
try:
    requests.post("http://localhost:4000/api/rental/webhook", json={"type": "SEED", "data": rental_data})
except Exception as e:
    print("Rental webhook err:", e)

print(f"Done! Total Wisata: {len(wisata_data)} Kuliner: {len(kuliner_data)} Rental: {len(rental_data)}")

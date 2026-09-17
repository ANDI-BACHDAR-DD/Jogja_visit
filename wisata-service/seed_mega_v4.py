import requests
import json
import random
import time
import os
import sys

print("Generating Mega Seed Data v4 (100 per category with proper webhooks)...")

regions = ["Kota Yogyakarta", "Sleman", "Bantul", "Gunungkidul", "Kulon Progo"]

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
        
        # Determine image keyword
        if "Budaya" in kat or "Religi" in kat:
            kw = "temple"
        elif "Edukasi" in kat or "Buatan" in kat:
            kw = "museum"
        else:
            kw = "nature"
            
        img = f"https://loremflickr.com/800/600/indonesia,{kw}?random={random.randint(1,1000)}"
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
            "rating": round(random.uniform(4.0, 5.0), 1),
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
        img = f"https://loremflickr.com/800/600/indonesia,food?random={random.randint(1,1000)}"
        
        kuliner_data.append({
            "place_id": f"KUL_{wil.replace(' ', '_')}_{i}",
            "nama": nama,
            "kategori": random.choice(["Restoran", "Warung", "Angkringan", "Kafe"]),
            "wilayah": wil,
            "alamat": f"Jl. Kuliner No. {random.randint(1,99)}, {wil}",
            "latitude": lat,
            "longitude": lon,
            "rating": round(random.uniform(4.0, 5.0), 1),
            "jumlah_ulasan": random.randint(50, 10000),
            "jenis_masakan": random.choice(jenis_masakan_list),
            "rentang_harga": f"Rp {random.choice([10, 15, 20, 30, 40, 50])}.000",
            "link_gmaps": f"https://www.google.com/maps/search/?api=1&query={lat},{lon}",
            "gambar": img
        })

    # Generate 20 Rental per region
    for i in range(20):
        lat = lat_b + random.uniform(-0.05, 0.05)
        lon = lon_b + random.uniform(-0.05, 0.05)
        nama = f"{random.choice(rental_names)} {random.choice(rental_suf)} {wil.split()[0]} {i+1}"
        jk = random.choice(jenis_kendaraan_list)
        img = f"https://loremflickr.com/800/600/car,indonesia?random={random.randint(1,1000)}"
        
        rental_data.append({
            "place_id": f"RNT_{wil.replace(' ', '_')}_{i}",
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
            "gambar": img
        })


print("Seeding Wisata (SQLAlchemy)...")
from database import SessionLocal, engine
from models import TempatWisata, Base

# Pastikan table terbentuk
Base.metadata.create_all(bind=engine)

db = SessionLocal()
db.query(TempatWisata).delete()
db.commit()

objects = [TempatWisata(**d) for d in wisata_data]
db.add_all(objects)
db.commit()
db.close()

print("Seeding Kuliner (via 8003 webhook)...")
for k in kuliner_data:
    try:
        requests.post("http://localhost:8003/webhook/restoran-sync", json=k)
    except Exception as e:
        print("Kuliner webhook err for", k["nama"], ":", e)

print("Seeding Rental (via 8002 webhook)...")
for r in rental_data:
    try:
        requests.post("http://localhost:8002/webhook/rental-sync", json=r)
    except Exception as e:
        print("Rental webhook err for", r["nama"], ":", e)

print(f"Done! Total Wisata: {len(wisata_data)} Kuliner: {len(kuliner_data)} Rental: {len(rental_data)}")

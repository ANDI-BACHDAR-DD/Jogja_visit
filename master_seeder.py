import requests
import json
import time

# --- WEBHOOK URLS ---
RENTAL_WEBHOOK = "http://localhost:4000/api/rental/webhook/rental-sync" # wait, API Gateway doesn't have route for webhook. It forwards /api/rental to rental service. But the route in rental service is /webhook/rental-sync, not /api/rental/webhook. 
# Better send direct to services:
RENTAL_SERVICE = "http://localhost:8002/webhook/rental-sync"
KULINER_SERVICE = "http://localhost:8003/webhook/restoran-sync"

print("Memulai seeding data Kuliner dan Rental secara massive via Webhook...")

kuliner_data = [
    # Kota
    {"place_id": "K001", "nama": "Gudeg Yu Djum Wijilan", "kategori": "Restoran", "wilayah": "Kota Yogyakarta", "alamat": "Jl. Wijilan No.167", "latitude": -7.809, "longitude": 110.367, "rating": 4.6, "jumlah_ulasan": 5000, "jenis_masakan": "Gudeg", "rentang_harga": "Rp 25.000 - Rp 50.000"},
    {"place_id": "K002", "nama": "Oseng Mercon Bu Narti", "kategori": "Restoran", "wilayah": "Kota Yogyakarta", "alamat": "Jl. KH. Ahmad Dahlan", "latitude": -7.801, "longitude": 110.362, "rating": 4.4, "jumlah_ulasan": 3200, "jenis_masakan": "Pedas", "rentang_harga": "Rp 20.000 - Rp 40.000"},
    # Sleman
    {"place_id": "K003", "nama": "Kopi Klotok Kaliurang", "kategori": "Kafe", "wilayah": "Sleman", "alamat": "Jl. Kaliurang KM.16", "latitude": -7.671, "longitude": 110.418, "rating": 4.7, "jumlah_ulasan": 8000, "jenis_masakan": "Tradisional Jawa", "rentang_harga": "Rp 15.000 - Rp 35.000"},
    {"place_id": "K004", "nama": "Jejamuran", "kategori": "Restoran", "wilayah": "Sleman", "alamat": "Jl. Pendowoharjo", "latitude": -7.712, "longitude": 110.364, "rating": 4.5, "jumlah_ulasan": 12000, "jenis_masakan": "Olahan Jamur", "rentang_harga": "Rp 30.000 - Rp 70.000"},
    # Bantul
    {"place_id": "K005", "nama": "Sate Klatak Pak Pong", "kategori": "Restoran", "wilayah": "Bantul", "alamat": "Jl. Imogiri Timur", "latitude": -7.873, "longitude": 110.395, "rating": 4.6, "jumlah_ulasan": 9500, "jenis_masakan": "Sate Kambing", "rentang_harga": "Rp 30.000 - Rp 60.000"},
    {"place_id": "K006", "nama": "Mangut Lele Mbah Marto", "kategori": "Restoran", "wilayah": "Bantul", "alamat": "Panggungharjo, Sewon", "latitude": -7.846, "longitude": 110.354, "rating": 4.5, "jumlah_ulasan": 4200, "jenis_masakan": "Ikan Pari Asap", "rentang_harga": "Rp 25.000 - Rp 50.000"},
    # Gunungkidul
    {"place_id": "K007", "nama": "Tiwul Yu Tum", "kategori": "Makanan Khas", "wilayah": "Gunungkidul", "alamat": "Wonosari", "latitude": -7.965, "longitude": 110.601, "rating": 4.7, "jumlah_ulasan": 2100, "jenis_masakan": "Jajanan Tradisional", "rentang_harga": "Rp 10.000 - Rp 25.000"},
    {"place_id": "K008", "nama": "Lobster Pantai Timang", "kategori": "Seafood", "wilayah": "Gunungkidul", "alamat": "Pantai Timang", "latitude": -8.106, "longitude": 110.648, "rating": 4.8, "jumlah_ulasan": 1100, "jenis_masakan": "Seafood", "rentang_harga": "Rp 200.000 - Rp 400.000"},
    # Kulon Progo
    {"place_id": "K009", "nama": "Kopi Ampirono", "kategori": "Kafe", "wilayah": "Kulon Progo", "alamat": "Girimulyo", "latitude": -7.755, "longitude": 110.134, "rating": 4.5, "jumlah_ulasan": 3400, "jenis_masakan": "Kopi & Snack", "rentang_harga": "Rp 10.000 - Rp 30.000"},
    {"place_id": "K010", "nama": "Geblek Pari Nanggulan", "kategori": "Restoran", "wilayah": "Kulon Progo", "alamat": "Nanggulan", "latitude": -7.766, "longitude": 110.203, "rating": 4.6, "jumlah_ulasan": 4500, "jenis_masakan": "Makanan Tradisional", "rentang_harga": "Rp 15.000 - Rp 35.000"},
]

rental_data = [
    # Kota
    {"place_id": "R001", "nama": "JOGJA EMPAT RODA", "jenis_kendaraan": "Mobil", "wilayah": "Kota Yogyakarta", "rating": 4.9, "jumlah_ulasan": 1200, "tautan_wa": "https://wa.me/628123456701", "harga": "Rp 300.000/hari"},
    {"place_id": "R002", "nama": "Tugu Trans Motor", "jenis_kendaraan": "Motor", "wilayah": "Kota Yogyakarta", "rating": 4.7, "jumlah_ulasan": 500, "tautan_wa": "https://wa.me/628123456702", "harga": "Rp 70.000/hari"},
    # Sleman
    {"place_id": "R003", "nama": "Sleman Transport", "jenis_kendaraan": "Mobil", "wilayah": "Sleman", "rating": 4.8, "jumlah_ulasan": 850, "tautan_wa": "https://wa.me/628123456703", "harga": "Rp 350.000/hari"},
    {"place_id": "R004", "nama": "Seturan Rent", "jenis_kendaraan": "Motor", "wilayah": "Sleman", "rating": 4.6, "jumlah_ulasan": 420, "tautan_wa": "https://wa.me/628123456704", "harga": "Rp 80.000/hari"},
    # Bantul
    {"place_id": "R005", "nama": "Bantul Jaya Rent", "jenis_kendaraan": "Mobil", "wilayah": "Bantul", "rating": 4.5, "jumlah_ulasan": 300, "tautan_wa": "https://wa.me/628123456705", "harga": "Rp 250.000/hari"},
    {"place_id": "R006", "nama": "Parangtritis Motor", "jenis_kendaraan": "Motor", "wilayah": "Bantul", "rating": 4.4, "jumlah_ulasan": 150, "tautan_wa": "https://wa.me/628123456706", "harga": "Rp 60.000/hari"},
    # Gunungkidul
    {"place_id": "R007", "nama": "Gunungkidul Explorer", "jenis_kendaraan": "Mobil (Jeep)", "wilayah": "Gunungkidul", "rating": 4.9, "jumlah_ulasan": 2100, "tautan_wa": "https://wa.me/628123456707", "harga": "Rp 500.000/trip"},
    {"place_id": "R008", "nama": "Wonosari Motor", "jenis_kendaraan": "Motor", "wilayah": "Gunungkidul", "rating": 4.5, "jumlah_ulasan": 120, "tautan_wa": "https://wa.me/628123456708", "harga": "Rp 100.000/hari"},
    # Kulon Progo
    {"place_id": "R009", "nama": "Wates Rent Car", "jenis_kendaraan": "Mobil", "wilayah": "Kulon Progo", "rating": 4.6, "jumlah_ulasan": 280, "tautan_wa": "https://wa.me/628123456709", "harga": "Rp 280.000/hari"},
    {"place_id": "R010", "nama": "YIA Motor Rent", "jenis_kendaraan": "Motor", "wilayah": "Kulon Progo", "rating": 4.8, "jumlah_ulasan": 650, "tautan_wa": "https://wa.me/628123456710", "harga": "Rp 75.000/hari"},
]

for k in kuliner_data:
    try:
        requests.post(KULINER_SERVICE, json=k)
    except:
        print("Failed to post kuliner", k['nama'])

for r in rental_data:
    try:
        requests.post(RENTAL_SERVICE, json=r)
    except:
        print("Failed to post rental", r['nama'])

print("Seeding Kuliner & Rental selesai.")

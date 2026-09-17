import os
import time
import requests
import schedule
from dotenv import load_dotenv

load_dotenv()

GOOGLE_PLACES_API_KEY = os.getenv("GOOGLE_PLACES_API_KEY", "MOCK_KEY_FOR_DEV")
RENTAL_WEBHOOK_URL = os.getenv("RENTAL_WEBHOOK_URL", "http://localhost:3000/webhook/rental-sync") # API Gateway / rental port
KULINER_WEBHOOK_URL = os.getenv("KULINER_WEBHOOK_URL", "http://localhost:3000/webhook/restoran-sync") # API Gateway / kuliner port

# Ganti port webhook target ke direct port jika API Gateway belum men-setup routing webhook
# Karena API gateway di port 3000 belum ada route /webhook, kita tembak langsung ke service backend.
RENTAL_SERVICE_WEBHOOK = "http://localhost:8002/webhook/rental-sync"
KULINER_SERVICE_WEBHOOK = "http://localhost:8003/webhook/restoran-sync"

def fetch_and_publish_mock_data():
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Menjalankan sinkronisasi data (MOCK)...")

    # Data Mock Rental
    mock_rental = {
        "place_id": "mock_rental_001",
        "nama": "Jogja Trans (Mock)",
        "kategori": "Rental Kendaraan",
        "wilayah": "Sleman",
        "alamat": "Jl. Seturan Raya",
        "latitude": -7.7612,
        "longitude": 110.4093,
        "rating": 4.8,
        "jumlah_ulasan": 150,
        "nomor_kontak": "+628123456789",
        "nomor_wa_ternormalisasi": "628123456789",
        "tautan_wa": "https://wa.me/628123456789",
        "jenis_kendaraan": "Motor",
    }

    # Data Mock Kuliner
    mock_kuliner = {
        "place_id": "mock_resto_001",
        "nama": "Gudeg Yu Djum (Mock)",
        "kategori": "Restoran",
        "wilayah": "Kota Yogyakarta",
        "alamat": "Jl. Wijilan",
        "latitude": -7.8066,
        "longitude": 110.3683,
        "rating": 4.5,
        "jumlah_ulasan": 2100,
        "jenis_masakan": "Gudeg, Masakan Jawa",
    }

    try:
        # Kirim Webhook ke Rental Service
        res_rental = requests.post(RENTAL_SERVICE_WEBHOOK, json=mock_rental, timeout=5)
        print(f"Webhook ke Rental Service: {res_rental.status_code}")

        # Kirim Webhook ke Kuliner Service
        res_kuliner = requests.post(KULINER_SERVICE_WEBHOOK, json=mock_kuliner, timeout=5)
        print(f"Webhook ke Kuliner Service: {res_kuliner.status_code}")
    except Exception as e:
        print(f"Error publishing webhook: {e}")

if __name__ == "__main__":
    print("Harvester Service started (Webhook Mode).")
    
    # Jalankan sekali saat start
    fetch_and_publish_mock_data()

    # Schedule setiap menit untuk testing
    schedule.every(1).minutes.do(fetch_and_publish_mock_data)

    while True:
        schedule.run_pending()
        time.sleep(1)

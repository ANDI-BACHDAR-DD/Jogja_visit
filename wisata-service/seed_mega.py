import requests
import json
import time

def get_wiki_image(title):
    url = f"https://id.wikipedia.org/w/api.php?action=query&titles={title}&prop=pageimages&format=json&pithumbsize=800"
    try:
        resp = requests.get(url).json()
        pages = resp.get("query", {}).get("pages", {})
        for page_id, page_info in pages.items():
            if "thumbnail" in page_info:
                return page_info["thumbnail"]["source"]
    except Exception as e:
        pass
    
    # Fallback to English wiki
    url = f"https://en.wikipedia.org/w/api.php?action=query&titles={title}&prop=pageimages&format=json&pithumbsize=800"
    try:
        resp = requests.get(url).json()
        pages = resp.get("query", {}).get("pages", {})
        for page_id, page_info in pages.items():
            if "thumbnail" in page_info:
                return page_info["thumbnail"]["source"]
    except:
        pass
    
    # Ultimate fallback if wiki has no image
    return f"https://ui-avatars.com/api/?name={title.replace(' ', '+')}&background=random&size=800"


print("Generating Mega Seed Data...")

wisata_raw = [
    # Kota Yogyakarta
    ("Keraton Yogyakarta", "Budaya/Heritage", "Kota Yogyakarta", "Istana resmi Kesultanan Ngayogyakarta Hadiningrat.", "Jl. Rotowijayan Blok No. 1", -7.805284, 110.364203, "https://goo.gl/maps/kraton"),
    ("Taman Sari", "Budaya/Heritage", "Kota Yogyakarta", "Bekas taman istana Keraton Ngayogyakarta.", "Patehan, Kraton", -7.8100, 110.3590, "https://goo.gl/maps/tamansari"),
    ("Jalan Malioboro", "Belanja/Ikonik", "Kota Yogyakarta", "Jalan legendaris di pusat kota Yogyakarta, surga belanja dan kuliner.", "Jl. Malioboro", -7.7925, 110.3658, "https://goo.gl/maps/malioboro"),
    ("Museum Sonobudoyo", "Edukasi/Sejarah", "Kota Yogyakarta", "Museum sejarah dan kebudayaan Jawa terlengkap di Yogyakarta.", "Jl. Trikora No.6", -7.8023, 110.3629, "https://goo.gl/maps/sonobudoyo"),
    ("Tugu Yogyakarta", "Ikonik", "Kota Yogyakarta", "Landmark paling terkenal dan simbol kota Yogyakarta.", "Gowongan, Jetis", -7.7829, 110.3670, "https://goo.gl/maps/tugujogja"),
    
    # Sleman
    ("Prambanan", "Budaya/Heritage", "Sleman", "Kompleks candi Hindu terbesar di Indonesia.", "Jl. Raya Solo - Yogyakarta", -7.7520, 110.4914, "https://goo.gl/maps/prambanan"),
    ("Ratu Boko", "Budaya/Heritage", "Sleman", "Situs purbakala kompleks keraton kuno di atas bukit.", "Bokoharjo, Prambanan", -7.7705, 110.4894, "https://goo.gl/maps/ratuboko"),
    ("Museum Ullen Sentalu", "Edukasi", "Sleman", "Museum budaya dan seni Jawa berarsitektur unik di lereng Merapi.", "Kaliurang Barat", -7.5975, 110.4230, "https://goo.gl/maps/ullensentalu"),
    ("Monumen Yogya Kembali", "Edukasi/Sejarah", "Sleman", "Monumen sejarah perjuangan kemerdekaan Indonesia.", "Ring Road Utara", -7.7495, 110.3695, "https://goo.gl/maps/monjali"),
    ("Gunung Merapi", "Alam", "Sleman", "Gunung berapi paling aktif di Indonesia, populer untuk wisata lava tour.", "Kaliurang", -7.5407, 110.4457, "https://goo.gl/maps/merapi"),
    
    # Bantul
    ("Parangtritis", "Alam", "Bantul", "Pantai ikonik Yogyakarta dengan gumuk pasir dan pemandangan sunset.", "Kretek, Bantul", -8.0254, 110.3340, "https://goo.gl/maps/parangtritis"),
    ("Hutan Pinus Mangunan", "Alam", "Bantul", "Hutan pinus asri dengan spot foto kekinian.", "Mangunan, Dlingo", -7.9269, 110.4285, "https://goo.gl/maps/hutanpinus"),
    ("Kebun Buah Mangunan", "Alam", "Bantul", "Gardu pandang terkenal dengan julukan 'Negeri di Atas Awan'.", "Mangunan", -7.9400, 110.4243, "https://goo.gl/maps/kebunbuah"),
    ("Pantai Depok (Bantul)", "Alam/Kuliner", "Bantul", "Pantai yang terkenal dengan pasar ikan dan kuliner seafood segar.", "Parangtritis, Kretek", -8.0135, 110.3129, "https://goo.gl/maps/pantaidepok"),
    ("Gumuk Pasir Parangkusumo", "Alam", "Bantul", "Gurun pasir unik ala Timur Tengah di pesisir selatan Jawa.", "Parangtritis", -8.0163, 110.3204, "https://goo.gl/maps/gumukpasir"),
    
    # Gunungkidul
    ("Goa Jomblang", "Alam", "Gunungkidul", "Gua vertikal dengan fenomena 'cahaya dari surga'.", "Pacarejo, Semanu", -8.0280, 110.6370, "https://goo.gl/maps/jomblang"),
    ("Pantai Indrayanti", "Alam", "Gunungkidul", "Pantai pasir putih dengan fasilitas modern dan bersih.", "Tepus, Gunungkidul", -8.1504, 110.6125, "https://goo.gl/maps/indrayanti"),
    ("Pantai Baron", "Alam", "Gunungkidul", "Pantai unik tempat bertemunya air laut dan air tawar.", "Kemadang, Tanjungsari", -8.1288, 110.5488, "https://goo.gl/maps/pantaibaron"),
    ("Pantai Timang", "Alam", "Gunungkidul", "Pantai ekstrem dengan gondola tradisional melintasi ombak besar.", "Tepus", -8.1064, 110.6483, "https://goo.gl/maps/pantaitimang"),
    ("Goa Pindul", "Alam", "Gunungkidul", "Wisata cave tubing menyusuri sungai bawah tanah di dalam gua.", "Bejiharjo, Karangmojo", -7.9287, 110.6482, "https://goo.gl/maps/goapindul"),
    
    # Kulon Progo
    ("Kalibiru", "Alam/Buatan", "Kulon Progo", "Wisata alam perbukitan dengan pemandangan Waduk Sermo.", "Hargowilis, Kokap", -7.8055, 110.1345, "https://goo.gl/maps/kalibiru"),
    ("Waduk Sermo", "Alam/Buatan", "Kulon Progo", "Danau buatan yang indah dan dikelilingi perbukitan hijau.", "Hargowilis", -7.8173, 110.1171, "https://goo.gl/maps/waduksermo"),
    ("Pule Payung", "Buatan", "Kulon Progo", "Spot foto kekinian dengan pemandangan alam Kulon Progo dari ketinggian.", "Hargotirto", -7.7950, 110.1250, "https://goo.gl/maps/pulepayung"),
    ("Kedung Pedut", "Alam", "Kulon Progo", "Air terjun bertingkat dengan kolam alami berwarna toska.", "Jatimulyo, Girimulyo", -7.7618, 110.1213, "https://goo.gl/maps/kedungpedut"),
    ("Pantai Glagah", "Alam", "Kulon Progo", "Pantai dengan tetrapod beton pemecah ombak yang khas.", "Temon, Kulon Progo", -7.9150, 110.0768, "https://goo.gl/maps/pantaiglagah"),
]

wisata_data = []
for idx, (title, kat, wil, desc, alamat, lat, lon, gmap) in enumerate(wisata_raw):
    print(f"Fetching image for {title}...")
    img = get_wiki_image(title)
    wisata_data.append({
        "nama": title, "kategori_wisata": kat, "wilayah": wil, "deskripsi": desc,
        "alamat": alamat, "latitude": lat, "longitude": lon, "link_gmaps": gmap,
        "rating": round(4.5 + (idx % 5)*0.1, 1), "jumlah_ulasan": 5000 + idx * 100,
        "estimasi_harga_tiket": "Rp 15.000 - 50.000", "jam_operasional": "08:00 - 17:00",
        "gambar": img
    })


kuliner_data = [
    # Kota
    {"place_id": "K001", "nama": "Gudeg Yu Djum Wijilan 167", "kategori": "Restoran", "wilayah": "Kota Yogyakarta", "alamat": "Jl. Wijilan No.167", "latitude": -7.809, "longitude": 110.367, "rating": 4.6, "jumlah_ulasan": 15000, "jenis_masakan": "Gudeg", "rentang_harga": "Rp 30.000", "link_gmaps": "https://maps.app.goo.gl/QcZq3D4vR3"},
    {"place_id": "K002", "nama": "Oseng Mercon Bu Narti", "kategori": "Restoran", "wilayah": "Kota Yogyakarta", "alamat": "Jl. KH. Ahmad Dahlan No.107", "latitude": -7.801, "longitude": 110.362, "rating": 4.4, "jumlah_ulasan": 8200, "jenis_masakan": "Pedas", "rentang_harga": "Rp 25.000", "link_gmaps": "https://maps.app.goo.gl/GZ5D9W82h6"},
    {"place_id": "K003", "nama": "Soto Kadipiro Asli", "kategori": "Restoran", "wilayah": "Kota Yogyakarta", "alamat": "Jl. Wates No.33", "latitude": -7.800, "longitude": 110.347, "rating": 4.5, "jumlah_ulasan": 6000, "jenis_masakan": "Soto", "rentang_harga": "Rp 20.000", "link_gmaps": "https://maps.app.goo.gl/7eR4"},
    {"place_id": "K004", "nama": "Kopi Joss Lek Man", "kategori": "Angkringan", "wilayah": "Kota Yogyakarta", "alamat": "Jl. Wongsodirjan", "latitude": -7.789, "longitude": 110.363, "rating": 4.5, "jumlah_ulasan": 9000, "jenis_masakan": "Kopi & Angkringan", "rentang_harga": "Rp 10.000", "link_gmaps": "https://maps.app.goo.gl/Lekman"},
    {"place_id": "K005", "nama": "House of Raminten", "kategori": "Restoran", "wilayah": "Kota Yogyakarta", "alamat": "Jl. FM Noto No.7", "latitude": -7.784, "longitude": 110.373, "rating": 4.4, "jumlah_ulasan": 18000, "jenis_masakan": "Jawa Klasik", "rentang_harga": "Rp 40.000", "link_gmaps": "https://maps.app.goo.gl/Raminten"},
    
    # Sleman
    {"place_id": "K006", "nama": "Kopi Klotok Pakem", "kategori": "Restoran", "wilayah": "Sleman", "alamat": "Jl. Kaliurang KM.16", "latitude": -7.671, "longitude": 110.418, "rating": 4.7, "jumlah_ulasan": 35000, "jenis_masakan": "Jawa Desa", "rentang_harga": "Rp 20.000", "link_gmaps": "https://maps.app.goo.gl/Klotok"},
    {"place_id": "K007", "nama": "Jejamuran", "kategori": "Restoran", "wilayah": "Sleman", "alamat": "Niron, Pandowoharjo", "latitude": -7.712, "longitude": 110.364, "rating": 4.6, "jumlah_ulasan": 22000, "jenis_masakan": "Olahan Jamur", "rentang_harga": "Rp 35.000", "link_gmaps": "https://maps.app.goo.gl/Jejamuran"},
    {"place_id": "K008", "nama": "Sate Ratu", "kategori": "Restoran", "wilayah": "Sleman", "alamat": "Jl. Tiyasan, Condongcatur", "latitude": -7.747, "longitude": 110.398, "rating": 4.9, "jumlah_ulasan": 14000, "jenis_masakan": "Sate Ayam", "rentang_harga": "Rp 35.000", "link_gmaps": "https://maps.app.goo.gl/SateRatu"},
    {"place_id": "K009", "nama": "Kala Jumpa", "kategori": "Kafe", "wilayah": "Sleman", "alamat": "Jl. Kaliurang", "latitude": -7.742, "longitude": 110.384, "rating": 4.5, "jumlah_ulasan": 1200, "jenis_masakan": "Kopi & Dessert", "rentang_harga": "Rp 40.000", "link_gmaps": "https://maps.app.goo.gl/KalaJumpa"},
    {"place_id": "K010", "nama": "Gudeg Pawon", "kategori": "Restoran", "wilayah": "Sleman", "alamat": "Jl. Janturan", "latitude": -7.808, "longitude": 110.386, "rating": 4.4, "jumlah_ulasan": 4500, "jenis_masakan": "Gudeg", "rentang_harga": "Rp 25.000", "link_gmaps": "https://maps.app.goo.gl/GudegPawon"},

    # Bantul
    {"place_id": "K011", "nama": "Sate Klatak Pak Pong", "kategori": "Restoran", "wilayah": "Bantul", "alamat": "Jl. Sultan Agung, Jejeran", "latitude": -7.873, "longitude": 110.395, "rating": 4.6, "jumlah_ulasan": 28000, "jenis_masakan": "Sate Kambing", "rentang_harga": "Rp 40.000", "link_gmaps": "https://maps.app.goo.gl/PakPong"},
    {"place_id": "K012", "nama": "Mangut Lele Mbah Marto", "kategori": "Restoran", "wilayah": "Bantul", "alamat": "Panggungharjo, Sewon", "latitude": -7.846, "longitude": 110.354, "rating": 4.5, "jumlah_ulasan": 8500, "jenis_masakan": "Ikan Asap Pedas", "rentang_harga": "Rp 30.000", "link_gmaps": "https://maps.app.goo.gl/MbahMarto"},
    {"place_id": "K013", "nama": "Ingkung Kuali", "kategori": "Restoran", "wilayah": "Bantul", "alamat": "Kalakijo, Guwosari", "latitude": -7.864, "longitude": 110.316, "rating": 4.6, "jumlah_ulasan": 6200, "jenis_masakan": "Ayam Ingkung", "rentang_harga": "Rp 150.000", "link_gmaps": "https://maps.app.goo.gl/Ingkung"},
    {"place_id": "K014", "nama": "Mie Lethek Mbah Mendes", "kategori": "Restoran", "wilayah": "Bantul", "alamat": "Jl. Parangtritis KM 8", "latitude": -7.875, "longitude": 110.345, "rating": 4.5, "jumlah_ulasan": 3400, "jenis_masakan": "Mie Tradisional", "rentang_harga": "Rp 20.000", "link_gmaps": "https://maps.app.goo.gl/MieLethek"},
    {"place_id": "K015", "nama": "Bumi Langit Institute", "kategori": "Restoran/Edukasi", "wilayah": "Bantul", "alamat": "Imogiri", "latitude": -7.915, "longitude": 110.395, "rating": 4.7, "jumlah_ulasan": 1800, "jenis_masakan": "Organik", "rentang_harga": "Rp 50.000", "link_gmaps": "https://maps.app.goo.gl/BumiLangit"},

    # Gunungkidul
    {"place_id": "K016", "nama": "Tiwul Yu Tum", "kategori": "Pusat Oleh-oleh", "wilayah": "Gunungkidul", "alamat": "Jl. Pramuka, Wonosari", "latitude": -7.965, "longitude": 110.601, "rating": 4.7, "jumlah_ulasan": 5100, "jenis_masakan": "Jajanan Tiwul", "rentang_harga": "Rp 15.000", "link_gmaps": "https://maps.app.goo.gl/TiwulYuTum"},
    {"place_id": "K017", "nama": "Lobster Pantai Timang (Pak Sis)", "kategori": "Seafood", "wilayah": "Gunungkidul", "alamat": "Pantai Timang", "latitude": -8.106, "longitude": 110.648, "rating": 4.8, "jumlah_ulasan": 2200, "jenis_masakan": "Lobster & Seafood", "rentang_harga": "Rp 350.000", "link_gmaps": "https://maps.app.goo.gl/PakSis"},
    {"place_id": "K018", "nama": "Kampoeng Lobster", "kategori": "Seafood", "wilayah": "Gunungkidul", "alamat": "Pantai Sepanjang", "latitude": -8.136, "longitude": 110.560, "rating": 4.4, "jumlah_ulasan": 1500, "jenis_masakan": "Seafood", "rentang_harga": "Rp 150.000", "link_gmaps": "https://maps.app.goo.gl/KpgLobster"},
    {"place_id": "K019", "nama": "Sate Kambing Pak Turut", "kategori": "Restoran", "wilayah": "Gunungkidul", "alamat": "Wonosari", "latitude": -7.968, "longitude": 110.602, "rating": 4.5, "jumlah_ulasan": 3100, "jenis_masakan": "Sate Kambing", "rentang_harga": "Rp 35.000", "link_gmaps": "https://maps.app.goo.gl/PakTurut"},
    {"place_id": "K020", "nama": "Walang Goreng Pak Gareng", "kategori": "Oleh-oleh Ekstrem", "wilayah": "Gunungkidul", "alamat": "Jl. Baron", "latitude": -7.975, "longitude": 110.590, "rating": 4.3, "jumlah_ulasan": 900, "jenis_masakan": "Belalang Goreng", "rentang_harga": "Rp 25.000", "link_gmaps": "https://maps.app.goo.gl/Walang"},

    # Kulon Progo
    {"place_id": "K021", "nama": "Kopi Ampirono", "kategori": "Kafe", "wilayah": "Kulon Progo", "alamat": "Pendoworejo, Girimulyo", "latitude": -7.755, "longitude": 110.134, "rating": 4.5, "jumlah_ulasan": 7400, "jenis_masakan": "Kopi & Snack", "rentang_harga": "Rp 20.000", "link_gmaps": "https://maps.app.goo.gl/KopiAmpirono"},
    {"place_id": "K022", "nama": "Geblek Pari Nanggulan", "kategori": "Restoran", "wilayah": "Kulon Progo", "alamat": "Kembang, Nanggulan", "latitude": -7.766, "longitude": 110.203, "rating": 4.6, "jumlah_ulasan": 12500, "jenis_masakan": "Tradisional Pedesaan", "rentang_harga": "Rp 20.000", "link_gmaps": "https://maps.app.goo.gl/GeblekPari"},
    {"place_id": "K023", "nama": "Kopi Sulingan", "kategori": "Kafe", "wilayah": "Kulon Progo", "alamat": "Kalibiru", "latitude": -7.805, "longitude": 110.135, "rating": 4.4, "jumlah_ulasan": 1100, "jenis_masakan": "Kopi", "rentang_harga": "Rp 25.000", "link_gmaps": "https://maps.app.goo.gl/Sulingan"},
    {"place_id": "K024", "nama": "Tiwul Pegunungan Menoreh", "kategori": "Oleh-oleh", "wilayah": "Kulon Progo", "alamat": "Samigaluh", "latitude": -7.695, "longitude": 110.165, "rating": 4.7, "jumlah_ulasan": 500, "jenis_masakan": "Tiwul", "rentang_harga": "Rp 15.000", "link_gmaps": "https://maps.app.goo.gl/Menoreh"},
    {"place_id": "K025", "nama": "Seafood Pantai Glagah", "kategori": "Seafood", "wilayah": "Kulon Progo", "alamat": "Pantai Glagah", "latitude": -7.915, "longitude": 110.076, "rating": 4.2, "jumlah_ulasan": 1800, "jenis_masakan": "Seafood", "rentang_harga": "Rp 80.000", "link_gmaps": "https://maps.app.goo.gl/SeafoodGlagah"},
]

rental_data = [
    # Kota
    {"place_id": "R001", "nama": "JOGJA EMPAT RODA", "jenis_kendaraan": "Mobil", "wilayah": "Kota Yogyakarta", "rating": 4.9, "jumlah_ulasan": 2200, "tautan_wa": "https://wa.me/628123456701", "harga": "Rp 300.000/hari", "link_gmaps": "https://maps.app.goo.gl/EmpatRoda"},
    {"place_id": "R002", "nama": "Pamitran Rental Motor", "jenis_kendaraan": "Motor", "wilayah": "Kota Yogyakarta", "rating": 4.8, "jumlah_ulasan": 1500, "tautan_wa": "https://wa.me/628123456702", "harga": "Rp 70.000/hari", "link_gmaps": "https://maps.app.goo.gl/Pamitran"},
    {"place_id": "R003", "nama": "Sabila Transport", "jenis_kendaraan": "Mobil", "wilayah": "Kota Yogyakarta", "rating": 4.7, "jumlah_ulasan": 3400, "tautan_wa": "https://wa.me/628123456703", "harga": "Rp 250.000/hari", "link_gmaps": "https://maps.app.goo.gl/Sabila"},
    {"place_id": "R004", "nama": "Alif Transport Jogja", "jenis_kendaraan": "Mobil & Elf", "wilayah": "Kota Yogyakarta", "rating": 4.6, "jumlah_ulasan": 1100, "tautan_wa": "https://wa.me/628123456704", "harga": "Rp 400.000/hari", "link_gmaps": "https://maps.app.goo.gl/Alif"},
    {"place_id": "R005", "nama": "Mandiri Motor Rent", "jenis_kendaraan": "Motor", "wilayah": "Kota Yogyakarta", "rating": 4.7, "jumlah_ulasan": 800, "tautan_wa": "https://wa.me/628123456705", "harga": "Rp 60.000/hari", "link_gmaps": "https://maps.app.goo.gl/Mandiri"},
    
    # Sleman
    {"place_id": "R006", "nama": "Sleman Trans", "jenis_kendaraan": "Mobil", "wilayah": "Sleman", "rating": 4.8, "jumlah_ulasan": 850, "tautan_wa": "https://wa.me/628123456706", "harga": "Rp 350.000/hari", "link_gmaps": "https://maps.app.goo.gl/SlemanTrans"},
    {"place_id": "R007", "nama": "Seturan Rent", "jenis_kendaraan": "Motor", "wilayah": "Sleman", "rating": 4.6, "jumlah_ulasan": 420, "tautan_wa": "https://wa.me/628123456707", "harga": "Rp 80.000/hari", "link_gmaps": "https://maps.app.goo.gl/Seturan"},
    {"place_id": "R008", "nama": "Abadi Transport Maguwo", "jenis_kendaraan": "Mobil", "wilayah": "Sleman", "rating": 4.7, "jumlah_ulasan": 1100, "tautan_wa": "https://wa.me/628123456708", "harga": "Rp 300.000/hari", "link_gmaps": "https://maps.app.goo.gl/Abadi"},
    {"place_id": "R009", "nama": "UGM Rental Sepeda & Motor", "jenis_kendaraan": "Sepeda & Motor", "wilayah": "Sleman", "rating": 4.9, "jumlah_ulasan": 2500, "tautan_wa": "https://wa.me/628123456709", "harga": "Rp 50.000/hari", "link_gmaps": "https://maps.app.goo.gl/UGMRent"},
    {"place_id": "R010", "nama": "Kaliurang Jeep Adventure", "jenis_kendaraan": "Jeep", "wilayah": "Sleman", "rating": 4.8, "jumlah_ulasan": 3400, "tautan_wa": "https://wa.me/628123456710", "harga": "Rp 400.000/trip", "link_gmaps": "https://maps.app.goo.gl/KaliurangJeep"},

    # Bantul
    {"place_id": "R011", "nama": "Bantul Jaya Rent", "jenis_kendaraan": "Mobil", "wilayah": "Bantul", "rating": 4.5, "jumlah_ulasan": 300, "tautan_wa": "https://wa.me/628123456711", "harga": "Rp 250.000/hari", "link_gmaps": "https://maps.app.goo.gl/BantulJaya"},
    {"place_id": "R012", "nama": "Parangtritis Rent Bike", "jenis_kendaraan": "Motor", "wilayah": "Bantul", "rating": 4.4, "jumlah_ulasan": 150, "tautan_wa": "https://wa.me/628123456712", "harga": "Rp 60.000/hari", "link_gmaps": "https://maps.app.goo.gl/ParisBike"},
    {"place_id": "R013", "nama": "Sewon Mobil", "jenis_kendaraan": "Mobil", "wilayah": "Bantul", "rating": 4.6, "jumlah_ulasan": 520, "tautan_wa": "https://wa.me/628123456713", "harga": "Rp 280.000/hari", "link_gmaps": "https://maps.app.goo.gl/SewonMobil"},
    {"place_id": "R014", "nama": "Imogiri Rent", "jenis_kendaraan": "Motor & Mobil", "wilayah": "Bantul", "rating": 4.7, "jumlah_ulasan": 810, "tautan_wa": "https://wa.me/628123456714", "harga": "Rp 75.000/hari", "link_gmaps": "https://maps.app.goo.gl/ImogiriRent"},
    {"place_id": "R015", "nama": "Jeep Gumuk Pasir", "jenis_kendaraan": "Jeep Wisata", "wilayah": "Bantul", "rating": 4.8, "jumlah_ulasan": 1400, "tautan_wa": "https://wa.me/628123456715", "harga": "Rp 350.000/trip", "link_gmaps": "https://maps.app.goo.gl/JeepGumuk"},

    # Gunungkidul
    {"place_id": "R016", "nama": "Gunungkidul Explorer", "jenis_kendaraan": "Mobil (Jeep/Hiace)", "wilayah": "Gunungkidul", "rating": 4.9, "jumlah_ulasan": 2100, "tautan_wa": "https://wa.me/628123456716", "harga": "Rp 500.000/hari", "link_gmaps": "https://maps.app.goo.gl/GKExplorer"},
    {"place_id": "R017", "nama": "Wonosari Motor Rent", "jenis_kendaraan": "Motor", "wilayah": "Gunungkidul", "rating": 4.5, "jumlah_ulasan": 120, "tautan_wa": "https://wa.me/628123456717", "harga": "Rp 100.000/hari", "link_gmaps": "https://maps.app.goo.gl/WonosariMotor"},
    {"place_id": "R018", "nama": "Pantai Selatan Trans", "jenis_kendaraan": "Mobil Elf", "wilayah": "Gunungkidul", "rating": 4.7, "jumlah_ulasan": 890, "tautan_wa": "https://wa.me/628123456718", "harga": "Rp 700.000/hari", "link_gmaps": "https://maps.app.goo.gl/PantaiSelatanTrans"},
    {"place_id": "R019", "nama": "Timang Jeep Adventure", "jenis_kendaraan": "Jeep Wisata", "wilayah": "Gunungkidul", "rating": 4.8, "jumlah_ulasan": 1800, "tautan_wa": "https://wa.me/628123456719", "harga": "Rp 350.000/trip", "link_gmaps": "https://maps.app.goo.gl/TimangJeep"},
    {"place_id": "R020", "nama": "Goa Pindul Tube Rent", "jenis_kendaraan": "Ban/Alat Wisata", "wilayah": "Gunungkidul", "rating": 4.6, "jumlah_ulasan": 4000, "tautan_wa": "https://wa.me/628123456720", "harga": "Rp 50.000/set", "link_gmaps": "https://maps.app.goo.gl/PindulRent"},

    # Kulon Progo
    {"place_id": "R021", "nama": "YIA Airport Rent Car", "jenis_kendaraan": "Mobil", "wilayah": "Kulon Progo", "rating": 4.8, "jumlah_ulasan": 3200, "tautan_wa": "https://wa.me/628123456721", "harga": "Rp 350.000/hari", "link_gmaps": "https://maps.app.goo.gl/YIARent"},
    {"place_id": "R022", "nama": "Wates Motor Rent", "jenis_kendaraan": "Motor", "wilayah": "Kulon Progo", "rating": 4.6, "jumlah_ulasan": 280, "tautan_wa": "https://wa.me/628123456722", "harga": "Rp 75.000/hari", "link_gmaps": "https://maps.app.goo.gl/WatesMotor"},
    {"place_id": "R023", "nama": "Nanggulan Bike", "jenis_kendaraan": "Sepeda Onthel", "wilayah": "Kulon Progo", "rating": 4.9, "jumlah_ulasan": 950, "tautan_wa": "https://wa.me/628123456723", "harga": "Rp 25.000/hari", "link_gmaps": "https://maps.app.goo.gl/NanggulanBike"},
    {"place_id": "R024", "nama": "Kokap Trans", "jenis_kendaraan": "Mobil", "wilayah": "Kulon Progo", "rating": 4.5, "jumlah_ulasan": 410, "tautan_wa": "https://wa.me/628123456724", "harga": "Rp 280.000/hari", "link_gmaps": "https://maps.app.goo.gl/KokapTrans"},
    {"place_id": "R025", "nama": "Menoreh Jeep Wisata", "jenis_kendaraan": "Jeep Wisata", "wilayah": "Kulon Progo", "rating": 4.7, "jumlah_ulasan": 670, "tautan_wa": "https://wa.me/628123456725", "harga": "Rp 400.000/trip", "link_gmaps": "https://maps.app.goo.gl/MenorehJeep"},
]


# 1. Clear database Wisata & Re-insert
import sqlite3
import os

print("Seeding Wisata (SQLAlchemy)...")
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
# Webhooks
for k in kuliner_data:
    try:
        requests.post("http://localhost:8003/webhook/restoran-sync", json=k)
    except:
        print("Fail Kuliner:", k['nama'])

print("Seeding Rental...")
# Rental NeDB is append-only for updates, but actually webhook upserts based on place_id!
# Let's clear the NeDB data first so there are no duplicates.
try:
    with open("rental-service/data/rentals.db", "w") as f:
        f.write("")
except Exception as e:
    print(e)
    
for r in rental_data:
    try:
        requests.post("http://localhost:8002/webhook/rental-sync", json=r)
    except:
        print("Fail Rental:", r['nama'])

print("Done! Total Wisata:", len(wisata_data), "Kuliner:", len(kuliner_data), "Rental:", len(rental_data))

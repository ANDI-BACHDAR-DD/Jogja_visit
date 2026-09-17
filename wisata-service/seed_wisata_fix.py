from database import SessionLocal
from models import TempatWisata, KategoriWisataEnum, WilayahEnum
import requests

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
    url = f"https://en.wikipedia.org/w/api.php?action=query&titles={title}&prop=pageimages&format=json&pithumbsize=800"
    try:
        resp = requests.get(url).json()
        pages = resp.get("query", {}).get("pages", {})
        for page_id, page_info in pages.items():
            if "thumbnail" in page_info:
                return page_info["thumbnail"]["source"]
    except:
        pass
    return f"https://ui-avatars.com/api/?name={title.replace(' ', '+')}&background=random&size=800"


db = SessionLocal()
db.query(TempatWisata).delete()
db.commit()

wisata_raw = [
    # Kota Yogyakarta
    ("Keraton Yogyakarta", KategoriWisataEnum.budaya, WilayahEnum.kota_yogyakarta, "Istana resmi Kesultanan Ngayogyakarta Hadiningrat.", "Jl. Rotowijayan Blok No. 1", -7.805284, 110.364203, "https://goo.gl/maps/kraton"),
    ("Taman Sari", KategoriWisataEnum.budaya, WilayahEnum.kota_yogyakarta, "Bekas taman istana Keraton Ngayogyakarta.", "Patehan, Kraton", -7.8100, 110.3590, "https://goo.gl/maps/tamansari"),
    ("Jalan Malioboro", KategoriWisataEnum.buatan, WilayahEnum.kota_yogyakarta, "Jalan legendaris di pusat kota Yogyakarta, surga belanja dan kuliner.", "Jl. Malioboro", -7.7925, 110.3658, "https://goo.gl/maps/malioboro"),
    ("Museum Sonobudoyo", KategoriWisataEnum.edukasi, WilayahEnum.kota_yogyakarta, "Museum sejarah dan kebudayaan Jawa terlengkap di Yogyakarta.", "Jl. Trikora No.6", -7.8023, 110.3629, "https://goo.gl/maps/sonobudoyo"),
    ("Tugu Yogyakarta", KategoriWisataEnum.buatan, WilayahEnum.kota_yogyakarta, "Landmark paling terkenal dan simbol kota Yogyakarta.", "Gowongan, Jetis", -7.7829, 110.3670, "https://goo.gl/maps/tugujogja"),
    
    # Sleman
    ("Prambanan", KategoriWisataEnum.budaya, WilayahEnum.sleman, "Kompleks candi Hindu terbesar di Indonesia.", "Jl. Raya Solo - Yogyakarta", -7.7520, 110.4914, "https://goo.gl/maps/prambanan"),
    ("Ratu Boko", KategoriWisataEnum.budaya, WilayahEnum.sleman, "Situs purbakala kompleks keraton kuno di atas bukit.", "Bokoharjo, Prambanan", -7.7705, 110.4894, "https://goo.gl/maps/ratuboko"),
    ("Museum Ullen Sentalu", KategoriWisataEnum.edukasi, WilayahEnum.sleman, "Museum budaya dan seni Jawa berarsitektur unik di lereng Merapi.", "Kaliurang Barat", -7.5975, 110.4230, "https://goo.gl/maps/ullensentalu"),
    ("Monumen Yogya Kembali", KategoriWisataEnum.edukasi, WilayahEnum.sleman, "Monumen sejarah perjuangan kemerdekaan Indonesia.", "Ring Road Utara", -7.7495, 110.3695, "https://goo.gl/maps/monjali"),
    ("Gunung Merapi", KategoriWisataEnum.alam, WilayahEnum.sleman, "Gunung berapi paling aktif di Indonesia, populer untuk wisata lava tour.", "Kaliurang", -7.5407, 110.4457, "https://goo.gl/maps/merapi"),
    
    # Bantul
    ("Parangtritis", KategoriWisataEnum.alam, WilayahEnum.bantul, "Pantai ikonik Yogyakarta dengan gumuk pasir dan pemandangan sunset.", "Kretek, Bantul", -8.0254, 110.3340, "https://goo.gl/maps/parangtritis"),
    ("Hutan Pinus Mangunan", KategoriWisataEnum.alam, WilayahEnum.bantul, "Hutan pinus asri dengan spot foto kekinian.", "Mangunan, Dlingo", -7.9269, 110.4285, "https://goo.gl/maps/hutanpinus"),
    ("Kebun Buah Mangunan", KategoriWisataEnum.alam, WilayahEnum.bantul, "Gardu pandang terkenal dengan julukan 'Negeri di Atas Awan'.", "Mangunan", -7.9400, 110.4243, "https://goo.gl/maps/kebunbuah"),
    ("Pantai Depok (Bantul)", KategoriWisataEnum.alam, WilayahEnum.bantul, "Pantai yang terkenal dengan pasar ikan dan kuliner seafood segar.", "Parangtritis, Kretek", -8.0135, 110.3129, "https://goo.gl/maps/pantaidepok"),
    ("Gumuk Pasir Parangkusumo", KategoriWisataEnum.alam, WilayahEnum.bantul, "Gurun pasir unik ala Timur Tengah di pesisir selatan Jawa.", "Parangtritis", -8.0163, 110.3204, "https://goo.gl/maps/gumukpasir"),
    
    # Gunungkidul
    ("Goa Jomblang", KategoriWisataEnum.alam, WilayahEnum.gunungkidul, "Gua vertikal dengan fenomena 'cahaya dari surga'.", "Pacarejo, Semanu", -8.0280, 110.6370, "https://goo.gl/maps/jomblang"),
    ("Pantai Indrayanti", KategoriWisataEnum.alam, WilayahEnum.gunungkidul, "Pantai pasir putih dengan fasilitas modern dan bersih.", "Tepus, Gunungkidul", -8.1504, 110.6125, "https://goo.gl/maps/indrayanti"),
    ("Pantai Baron", KategoriWisataEnum.alam, WilayahEnum.gunungkidul, "Pantai unik tempat bertemunya air laut dan air tawar.", "Kemadang, Tanjungsari", -8.1288, 110.5488, "https://goo.gl/maps/pantaibaron"),
    ("Pantai Timang", KategoriWisataEnum.alam, WilayahEnum.gunungkidul, "Pantai ekstrem dengan gondola tradisional melintasi ombak besar.", "Tepus", -8.1064, 110.6483, "https://goo.gl/maps/pantaitimang"),
    ("Goa Pindul", KategoriWisataEnum.alam, WilayahEnum.gunungkidul, "Wisata cave tubing menyusuri sungai bawah tanah di dalam gua.", "Bejiharjo, Karangmojo", -7.9287, 110.6482, "https://goo.gl/maps/goapindul"),
    
    # Kulon Progo
    ("Kalibiru", KategoriWisataEnum.buatan, WilayahEnum.kulonprogo, "Wisata alam perbukitan dengan pemandangan Waduk Sermo.", "Hargowilis, Kokap", -7.8055, 110.1345, "https://goo.gl/maps/kalibiru"),
    ("Waduk Sermo", KategoriWisataEnum.alam, WilayahEnum.kulonprogo, "Danau buatan yang indah dan dikelilingi perbukitan hijau.", "Hargowilis", -7.8173, 110.1171, "https://goo.gl/maps/waduksermo"),
    ("Pule Payung", KategoriWisataEnum.buatan, WilayahEnum.kulonprogo, "Spot foto kekinian dengan pemandangan alam Kulon Progo dari ketinggian.", "Hargotirto", -7.7950, 110.1250, "https://goo.gl/maps/pulepayung"),
    ("Kedung Pedut", KategoriWisataEnum.alam, WilayahEnum.kulonprogo, "Air terjun bertingkat dengan kolam alami berwarna toska.", "Jatimulyo, Girimulyo", -7.7618, 110.1213, "https://goo.gl/maps/kedungpedut"),
    ("Pantai Glagah", KategoriWisataEnum.alam, WilayahEnum.kulonprogo, "Pantai dengan tetrapod beton pemecah ombak yang khas.", "Temon, Kulon Progo", -7.9150, 110.0768, "https://goo.gl/maps/pantaiglagah"),
]

wisata_data = []
for idx, (title, kat, wil, desc, alamat, lat, lon, gmap) in enumerate(wisata_raw):
    img = get_wiki_image(title)
    wisata_data.append({
        "nama": title, "kategori_wisata": kat.value, "wilayah": wil.value, "deskripsi": desc,
        "alamat": alamat, "latitude": lat, "longitude": lon, "link_gmaps": gmap,
        "rating": round(4.5 + (idx % 5)*0.1, 1), "jumlah_ulasan": 5000 + idx * 100,
        "estimasi_harga_tiket": "Rp 15.000 - 50.000", "jam_operasional": "08:00 - 17:00",
        "gambar": img
    })

objects = [TempatWisata(**d) for d in wisata_data]
db.add_all(objects)
db.commit()
db.close()
print("Wisata fixed.")

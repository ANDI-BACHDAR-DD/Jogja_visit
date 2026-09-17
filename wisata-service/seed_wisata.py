from database import SessionLocal
from models import TempatWisata, KategoriWisataEnum, WilayahEnum

db = SessionLocal()

# Check if data already exists
if db.query(TempatWisata).count() == 0:
    wisata1 = TempatWisata(
        nama="Keraton Yogyakarta",
        kategori_wisata=KategoriWisataEnum.budaya,
        wilayah=WilayahEnum.kota_yogyakarta,
        deskripsi="Istana resmi Kesultanan Ngayogyakarta Hadiningrat. Tempat yang kaya akan budaya dan sejarah.",
        alamat="Jl. Rotowijayan Blok No. 1, Panembahan, Kecamatan Kraton, Kota Yogyakarta",
        latitude=-7.805284,
        longitude=110.364203,
        rating=4.7,
        jumlah_ulasan=25000,
        estimasi_harga_tiket="Rp 15.000",
        jam_operasional="08:00 - 14:00",
        link_gmaps="https://goo.gl/maps/keraton",
        gambar="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Keraton_Yogyakarta_1.jpg/800px-Keraton_Yogyakarta_1.jpg"
    )
    
    wisata2 = TempatWisata(
        nama="Candi Prambanan",
        kategori_wisata=KategoriWisataEnum.budaya,
        wilayah=WilayahEnum.sleman,
        deskripsi="Candi Hindu terbesar di Indonesia yang dibangun pada abad ke-9 Masehi.",
        alamat="Jl. Raya Solo - Yogyakarta No.16, Kranggan, Bokoharjo, Prambanan, Kabupaten Sleman",
        latitude=-7.752020,
        longitude=110.491467,
        rating=4.8,
        jumlah_ulasan=40000,
        estimasi_harga_tiket="Rp 50.000",
        jam_operasional="06:00 - 17:00",
        link_gmaps="https://goo.gl/maps/prambanan",
        gambar="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Prambanan_Temple_Yogyakarta_Indonesia.jpg/800px-Prambanan_Temple_Yogyakarta_Indonesia.jpg"
    )
    
    wisata3 = TempatWisata(
        nama="Pantai Parangtritis",
        kategori_wisata=KategoriWisataEnum.alam,
        wilayah=WilayahEnum.bantul,
        deskripsi="Pantai yang paling terkenal di Yogyakarta dengan pemandangan matahari terbenam yang indah.",
        alamat="Kecamatan Kretek, Kabupaten Bantul, Daerah Istimewa Yogyakarta",
        latitude=-8.025400,
        longitude=110.334000,
        rating=4.5,
        jumlah_ulasan=18000,
        estimasi_harga_tiket="Rp 10.000",
        jam_operasional="24 Jam",
        link_gmaps="https://goo.gl/maps/parangtritis",
        gambar="https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Parangtritis_Beach_2.jpg/800px-Parangtritis_Beach_2.jpg"
    )

    db.add_all([wisata1, wisata2, wisata3])
    db.commit()
    print("Berhasil memasukkan data seed wisata!")
else:
    print("Data wisata sudah ada, skip seeding.")

db.close()

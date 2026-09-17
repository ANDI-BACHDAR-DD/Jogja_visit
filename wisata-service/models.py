from sqlalchemy import Column, Integer, String, Float, Text, Enum
from database import Base
import enum

class WilayahEnum(str, enum.Enum):
    sleman = "Sleman"
    bantul = "Bantul"
    gunungkidul = "Gunungkidul"
    kulonprogo = "Kulon Progo"
    kota_yogyakarta = "Kota Yogyakarta"

class KategoriWisataEnum(str, enum.Enum):
    alam = "Alam"
    budaya = "Budaya/Heritage"
    edukasi = "Edukasi"
    religi = "Religi"
    buatan = "Buatan/Instagramable"

class TempatWisata(Base):
    __tablename__ = "tempat_wisata"

    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String, index=True)
    kategori_wisata = Column(Enum(KategoriWisataEnum))
    wilayah = Column(Enum(WilayahEnum))
    deskripsi = Column(Text)
    alamat = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    rating = Column(Float, default=0.0)
    jumlah_ulasan = Column(Integer, default=0)
    estimasi_harga_tiket = Column(String)
    jam_operasional = Column(String)
    link_gmaps = Column(String)
    gambar = Column(String)
    dikurasi_oleh = Column(String)
    sumber_data = Column(String, default="Admin")

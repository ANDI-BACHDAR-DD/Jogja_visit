from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
import models
from database import engine, get_db

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Wisata Service")

# Pydantic schema untuk respon
class TempatWisataResponse(BaseModel):
    id: int
    nama: str
    kategori_wisata: str
    wilayah: str
    deskripsi: str | None = None
    alamat: str | None = None
    rating: float
    link_gmaps: str | None = None
    gambar: str | None = None
    jam_operasional: str | None = None
    estimasi_harga_tiket: str | None = None

    class Config:
        from_attributes = True

@app.get("/health")
def health_check():
    return {"status": "Wisata Service is running"}

@app.get("/api/wisata", response_model=List[TempatWisataResponse])
def get_wisata(wilayah: str = None, kategori: str = None, db: Session = Depends(get_db)):
    query = db.query(models.TempatWisata)
    if wilayah:
        query = query.filter(models.TempatWisata.wilayah == wilayah)
    if kategori:
        query = query.filter(models.TempatWisata.kategori_wisata == kategori)
    return query.all()

@app.get("/api/wisata/{wisata_id}", response_model=TempatWisataResponse)
def get_wisata_by_id(wisata_id: int, db: Session = Depends(get_db)):
    wisata = db.query(models.TempatWisata).filter(models.TempatWisata.id == wisata_id).first()
    if not wisata:
        raise HTTPException(status_code=404, detail="Tempat wisata tidak ditemukan")
    return wisata

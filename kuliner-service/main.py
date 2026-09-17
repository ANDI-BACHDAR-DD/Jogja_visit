from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import datetime
import uvicorn
import os

# Konfigurasi Database SQLite Lokal
SQLALCHEMY_DATABASE_URL = "sqlite:///./kuliner.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Model Restoran
class Restoran(Base):
    __tablename__ = "restoran"

    id = Column(Integer, primary_key=True, index=True)
    place_id = Column(String, unique=True, index=True)
    nama = Column(String)
    kategori = Column(String)
    wilayah = Column(String)
    alamat = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    rating = Column(Float)
    jumlah_ulasan = Column(Integer)
    link_gmaps = Column(String)
    jenis_masakan = Column(String)
    rentang_harga = Column(String)
    sumber_data = Column(String)
    gambar = Column(String)
    terakhir_disinkron = Column(DateTime, default=datetime.datetime.utcnow)

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency untuk mendapatkan session DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health_check():
    return {"status": "Kuliner Service is running"}

@app.get("/api/kuliner")
def get_kuliner(wilayah: str = None, min_rating: float = None, db: Session = Depends(get_db)):
    query = db.query(Restoran)
    if wilayah:
        query = query.filter(Restoran.wilayah == wilayah)
    if min_rating:
        query = query.filter(Restoran.rating >= min_rating)
    
    return query.order_by(Restoran.rating.desc()).all()

# Endpoint Webhook dari Harvester
@app.post("/webhook/restoran-sync")
async def webhook_sync(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    
    # Upsert logic (Update jika ada, Insert jika belum ada)
    resto = db.query(Restoran).filter(Restoran.place_id == data.get("place_id")).first()
    
    if resto:
        # Update
        for key, value in data.items():
            setattr(resto, key, value)
        resto.sumber_data = "Google Places API"
        resto.terakhir_disinkron = datetime.datetime.utcnow()
    else:
        # Insert
        resto = Restoran(**data)
        resto.sumber_data = "Google Places API"
        resto.terakhir_disinkron = datetime.datetime.utcnow()
        db.add(resto)
        
    db.commit()
    print(f"Update dari Harvester via Webhook: {resto.nama}")
    return {"message": "Data tersinkronisasi"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8003))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)

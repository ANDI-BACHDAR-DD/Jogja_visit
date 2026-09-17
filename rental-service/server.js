require('dotenv').config();
const express = require('express');
const cors = require('cors');
const Datastore = require('nedb-promises');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 8002;

app.use(cors());
app.use(express.json());

// Inisialisasi NeDB (Database Lokal)
const dbPath = path.join(__dirname, 'rental.db');
const db = Datastore.create({ filename: dbPath, autoload: true });
console.log(`Terkoneksi ke NeDB di ${dbPath}`);

// Bikin index unique untuk place_id
db.ensureIndex({ fieldName: 'place_id', unique: true });

// REST Routes (Untuk Frontend)
app.get('/health', (req, res) => {
    res.json({ status: 'Rental Service is running' });
});

app.get('/api/rental', async (req, res) => {
    try {
        const { wilayah, jenis_kendaraan } = req.query;
        const filter = {};
        if (wilayah) filter.wilayah = wilayah;
        if (jenis_kendaraan) filter.jenis_kendaraan = jenis_kendaraan;

        // Ambil data dari NeDB dan urutkan rating menurun
        const rentals = await db.find(filter).sort({ rating: -1 });
        res.json(rentals);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
});

// Webhook Endpoint (Untuk Harvester Service)
// Menggantikan peran RabbitMQ consumer
app.post('/webhook/rental-sync', async (req, res) => {
    try {
        const data = req.body;
        console.log("Menerima update dari Harvester via Webhook:", data.nama);
        
        // Upsert di NeDB
        await db.update(
            { place_id: data.place_id },
            { $set: data },
            { upsert: true }
        );
        
        res.status(200).json({ message: "Data tersinkronisasi" });
    } catch (error) {
        console.error("Gagal sync Webhook:", error);
        res.status(500).json({ message: "Internal server error" });
    }
});

app.listen(PORT, () => {
    console.log(`Rental Service berjalan di port ${PORT}`);
});

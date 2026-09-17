const mongoose = require('mongoose');

const rentalSchema = new mongoose.Schema({
    place_id: { type: String, required: true, unique: true }, // Dari Google Places API
    nama: { type: String, required: true },
    kategori: { type: String, default: 'Rental Kendaraan' },
    wilayah: { 
        type: String, 
        enum: ['Sleman', 'Bantul', 'Gunungkidul', 'Kulon Progo', 'Kota Yogyakarta'],
        required: true 
    },
    alamat: String,
    latitude: Number,
    longitude: Number,
    rating: { type: Number, default: 0.0 },
    jumlah_ulasan: { type: Number, default: 0 },
    nomor_kontak: String, // Original dari Google
    nomor_wa_ternormalisasi: String, // Dikonversi ke 62xxx
    tautan_wa: String, // wa.me/62xxx
    link_gmaps: String,
    jam_operasional: [String],
    jenis_kendaraan: { type: String, enum: ['Motor', 'Mobil', 'Motor & Mobil', 'Lainnya'], default: 'Lainnya' },
    kisaran_harga_sewa: String,
    sumber_data: { type: String, default: 'Google Places API' },
    terakhir_disinkron: { type: Date, default: Date.now }
});

module.exports = mongoose.model('Rental', rentalSchema);

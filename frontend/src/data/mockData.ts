export type Wilayah = "Sleman" | "Bantul" | "Gunungkidul" | "Kulon Progo" | "Kota Yogyakarta";

export interface TempatWisata {
    id: number | string;
    nama: string;
    kategori_wisata: string;
    wilayah: Wilayah;
    deskripsi: string;
    alamat?: string;
    rating: number;
    jumlah_ulasan?: number;
    estimasi_harga_tiket?: string;
    jam_operasional?: string;
    link_gmaps?: string;
    gambar?: string;
}

export interface Rental {
    id: string;
    nama: string;
    wilayah: Wilayah;
    kategori?: string;
    rating: number;
    jumlah_ulasan: number;
    tautan_wa: string;
    jenis_kendaraan: string;
    harga: string;
    alamat?: string;
    link_gmaps?: string;
    gambar?: string;
}

export interface Kuliner {
    id: string;
    nama: string;
    wilayah: Wilayah;
    kategori?: string;
    rating: number;
    jumlah_ulasan: number;
    jenis_masakan: string;
    rentang_harga: string;
    alamat?: string;
    link_gmaps?: string;
    gambar?: string;
}

export const mockWisata: TempatWisata[] = [
    // Sleman
    { id: 1, nama: "Candi Prambanan", kategori_wisata: "Budaya/Heritage", wilayah: "Sleman", deskripsi: "Mahakarya arsitektur Hindu abad ke-9, Candi Prambanan merupakan candi Hindu terbesar di Indonesia yang menjulang setinggi 47 meter. Relief Ramayana terukir indah di dinding candi, menceritakan kisah epik legendaris.", rating: 4.8, link_gmaps: "#", gambar: "https://images.unsplash.com/photo-1596404981882-747d4e5ff012?auto=format&fit=crop&q=80&w=800" },
    { id: 6, nama: "Obelix Hills", kategori_wisata: "Buatan/Instagramable", wilayah: "Sleman", deskripsi: "Terletak di atas bukit batu purba, Obelix Hills menawarkan lebih dari 30 spot foto instagenic dengan pemandangan kota Jogja dari ketinggian, terutama saat matahari terbenam. Cocok untuk nongkrong santai.", rating: 4.4, link_gmaps: "#", gambar: "https://images.unsplash.com/photo-1516483638261-f40af5edca87?auto=format&fit=crop&q=80&w=800" },
    { id: 7, nama: "Museum Ullen Sentalu", kategori_wisata: "Edukasi", wilayah: "Sleman", deskripsi: "Museum seni dan budaya Jawa yang terletak di Kaliurang. Menyajikan koleksi peninggalan Keraton Mataram yang dikemas dengan tur berpemandu yang sangat interaktif dan eksklusif.", rating: 4.9, link_gmaps: "#", gambar: "https://images.unsplash.com/photo-1582236598555-5dc639434449?auto=format&fit=crop&q=80&w=800" },

    // Bantul
    { id: 2, nama: "Pantai Parangtritis", kategori_wisata: "Alam", wilayah: "Bantul", deskripsi: "Pantai ikonik Jogja yang terkenal dengan ombak besarnya, gumuk pasir pelangkus, dan pemandangan sunset magis. Pengunjung dapat menyewa ATV atau naik delman menyusuri garis pantai.", rating: 4.5, link_gmaps: "#", gambar: "https://images.unsplash.com/photo-1614713702517-8eeb960fcdbb?auto=format&fit=crop&q=80&w=800" },
    { id: 8, nama: "Hutan Pinus Mangunan", kategori_wisata: "Alam", wilayah: "Bantul", deskripsi: "Hutan pinus yang rimbun dan sejuk, menawarkan udara segar pegunungan. Dilengkapi dengan panggung alam, spot foto gardu pandang, dan area piknik yang tenang jauh dari hiruk-pikuk kota.", rating: 4.7, link_gmaps: "#", gambar: "https://images.unsplash.com/photo-1621538605286-9dc4b1b6f634?auto=format&fit=crop&q=80&w=800" },

    // Gunungkidul
    { id: 3, nama: "Goa Jomblang", kategori_wisata: "Alam", wilayah: "Gunungkidul", deskripsi: "Gua vertikal sedalam 60 meter yang terbentuk dari runtuhnya tanah (sinkhole). Keajaiban utamanya adalah 'cahaya surga' yang menyinari dasar gua yang dipenuhi hutan purba pada siang hari.", rating: 4.9, link_gmaps: "#", gambar: "https://images.unsplash.com/photo-1610486821360-64ab7f564dc7?auto=format&fit=crop&q=80&w=800" },
    { id: 9, nama: "Pantai Indrayanti", kategori_wisata: "Alam", wilayah: "Gunungkidul", deskripsi: "Salah satu pantai paling bersih di deretan pesisir selatan Gunungkidul. Memiliki pasir putih lembut, air laut kebiruan, dan deretan kafe serta gazebo nyaman di tepi pantai.", rating: 4.6, link_gmaps: "#", gambar: "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&q=80&w=800" },

    // Kulon Progo
    { id: 4, nama: "Kalibiru", kategori_wisata: "Alam", wilayah: "Kulon Progo", deskripsi: "Desa wisata di Perbukitan Menoreh yang menawarkan gardu pandang ikonik di atas pohon pinus. Dari sini, wisatawan dapat melihat panorama Waduk Sermo yang dikelilingi hutan hijau.", rating: 4.6, link_gmaps: "#", gambar: "https://images.unsplash.com/photo-1518182170546-076616fd4628?auto=format&fit=crop&q=80&w=800" },
    { id: 10, nama: "Air Terjun Kedung Pedut", kategori_wisata: "Alam", wilayah: "Kulon Progo", deskripsi: "Taman bermain air alami dengan air terjun dua warna (putih jernih dan tosca). Kolam-kolam alami bertingkat sangat cocok untuk berenang dan bermain air di tengah hutan yang asri.", rating: 4.7, link_gmaps: "#", gambar: "https://images.unsplash.com/photo-1433086966358-54859d0ed716?auto=format&fit=crop&q=80&w=800" },

    // Kota Yogyakarta
    { id: 5, nama: "Keraton Yogyakarta", kategori_wisata: "Budaya/Heritage", wilayah: "Kota Yogyakarta", deskripsi: "Jantung kebudayaan Jawa yang masih aktif. Sebagai istana resmi Kesultanan Ngayogyakarta Hadiningrat, tempat ini menyimpan pusaka keraton, kereta kencana, dan sejarah panjang Mataram Islam.", rating: 4.7, link_gmaps: "#", gambar: "https://images.unsplash.com/photo-1549473889-14f364a66e4a?auto=format&fit=crop&q=80&w=800" },
    { id: 11, nama: "Jalan Malioboro", kategori_wisata: "Buatan/Instagramable", wilayah: "Kota Yogyakarta", deskripsi: "Jalan paling legendaris di Jogja. Pusat perbelanjaan, oleh-oleh, dan seniman jalanan. Kini memiliki trotoar yang lebar dan nyaman untuk berjalan-jalan sore sambil menikmati suasana kota.", rating: 4.8, link_gmaps: "#", gambar: "https://images.unsplash.com/photo-1555899434-94d1368aa7af?auto=format&fit=crop&q=80&w=800" },
    { id: 12, nama: "Taman Sari", kategori_wisata: "Budaya/Heritage", wilayah: "Kota Yogyakarta", deskripsi: "Situs bekas taman istana (water castle) Keraton Yogyakarta yang dibangun abad ke-18. Menampilkan arsitektur perpaduan Jawa dan Portugis yang sangat indah untuk latar berfoto.", rating: 4.6, link_gmaps: "#", gambar: "https://images.unsplash.com/photo-1582559937861-12502df2f913?auto=format&fit=crop&q=80&w=800" }
];

export const mockRental: Rental[] = [
    { id: "r1", nama: "Jogja Trans (Mock)", wilayah: "Sleman", kategori: "Rental Kendaraan", rating: 4.8, jumlah_ulasan: 150, tautan_wa: "https://wa.me/628123456789", jenis_kendaraan: "Motor", harga: "Rp 70.000 / hari" },
    { id: "r2", nama: "Bantul Rent Car", wilayah: "Bantul", kategori: "Rental Kendaraan", rating: 4.7, jumlah_ulasan: 90, tautan_wa: "https://wa.me/628123456789", jenis_kendaraan: "Mobil", harga: "Rp 350.000 / hari" },
    { id: "r3", nama: "Gunungkidul Explorer", wilayah: "Gunungkidul", kategori: "Rental Kendaraan", rating: 4.9, jumlah_ulasan: 220, tautan_wa: "https://wa.me/628123456789", jenis_kendaraan: "Mobil", harga: "Rp 400.000 / hari" },
    { id: "r4", nama: "Kulon Progo Wheels", wilayah: "Kulon Progo", kategori: "Rental Kendaraan", rating: 4.5, jumlah_ulasan: 45, tautan_wa: "https://wa.me/628123456789", jenis_kendaraan: "Motor", harga: "Rp 80.000 / hari" },
    { id: "r5", nama: "Malioboro Bike Rent", wilayah: "Kota Yogyakarta", kategori: "Rental Kendaraan", rating: 4.6, jumlah_ulasan: 310, tautan_wa: "https://wa.me/628123456789", jenis_kendaraan: "Motor", harga: "Rp 90.000 / hari" },
    { id: "r6", nama: "Tugu Trans", wilayah: "Kota Yogyakarta", kategori: "Rental Kendaraan", rating: 4.9, jumlah_ulasan: 512, tautan_wa: "https://wa.me/628123456789", jenis_kendaraan: "Mobil", harga: "Rp 300.000 / hari" },
];

export const mockKuliner: Kuliner[] = [
    { id: "k1", nama: "Gudeg Yu Djum", wilayah: "Kota Yogyakarta", kategori: "Restoran", rating: 4.6, jumlah_ulasan: 4500, jenis_masakan: "Gudeg, Masakan Jawa", rentang_harga: "Rp 25.000 - Rp 50.000" },
    { id: "k2", nama: "Sate Klatak Pak Pong", wilayah: "Bantul", kategori: "Restoran", rating: 4.5, jumlah_ulasan: 3200, jenis_masakan: "Sate Kambing", rentang_harga: "Rp 30.000 - Rp 60.000" },
    { id: "k3", nama: "Tiwul Yu Tum", wilayah: "Gunungkidul", kategori: "Warung Makan", rating: 4.7, jumlah_ulasan: 1200, jenis_masakan: "Makanan Tradisional, Tiwul", rentang_harga: "Rp 15.000 - Rp 30.000" },
    { id: "k4", nama: "Kopi Klotok", wilayah: "Sleman", kategori: "Restoran", rating: 4.8, jumlah_ulasan: 5600, jenis_masakan: "Masakan Ndeso, Kopi", rentang_harga: "Rp 10.000 - Rp 35.000" },
    { id: "k5", nama: "Geblek Pari Nanggulan", wilayah: "Kulon Progo", kategori: "Warung Makan", rating: 4.6, jumlah_ulasan: 2100, jenis_masakan: "Geblek, Masakan Desa", rentang_harga: "Rp 10.000 - Rp 25.000" },
    { id: "k6", nama: "Oseng Mercon Bu Narti", wilayah: "Kota Yogyakarta", kategori: "Warung Makan", rating: 4.4, jumlah_ulasan: 3300, jenis_masakan: "Pedas, Daging Sapi", rentang_harga: "Rp 25.000 - Rp 45.000" }
];

export const ALL_WILAYAH: Wilayah[] = ["Kota Yogyakarta", "Sleman", "Bantul", "Gunungkidul", "Kulon Progo"];

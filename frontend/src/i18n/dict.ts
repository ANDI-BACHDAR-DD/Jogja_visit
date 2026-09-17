export const dict = {
  id: {
    title: "Eksplorasi Daerah Istimewa Yogyakarta",
    subtitle: "Jantung budaya dan sejarah Jawa. Temukan keindahan alam, peninggalan bersejarah, dan kuliner legendaris.",
    wisata_tab: "Destinasi Wisata",
    rental_tab: "Rental Kendaraan",
    kuliner_tab: "Kuliner & Resto",
    open_maps: "Buka di Maps",
    chat_wa: "Chat WA",
    price: "Harga",
    ticket: "Tiket",
    settings: "Pengaturan",
    theme: "Tema",
    language: "Bahasa",
    dark_mode: "Gelap",
    light_mode: "Terang",
    profile: "Profil Saya",
    login: "Masuk",
    logout: "Keluar",
    history: "Riwayat Kunjungan",
    no_history: "Belum ada riwayat kunjungan.",
    welcome: "Selamat datang,",
    login_desc: "Masuk untuk menyimpan riwayat penjelajahan Anda di Jogja.",
    close: "Tutup",
  },
  en: {
    title: "Explore Special Region of Yogyakarta",
    subtitle: "The heart of Javanese culture and history. Discover natural beauties, historical heritage, and legendary culinary spots.",
    wisata_tab: "Destinations",
    rental_tab: "Vehicle Rentals",
    kuliner_tab: "Culinary & Dining",
    open_maps: "Open Maps",
    chat_wa: "Chat WA",
    price: "Price",
    ticket: "Ticket",
    settings: "Settings",
    theme: "Theme",
    language: "Language",
    dark_mode: "Dark",
    light_mode: "Light",
    profile: "My Profile",
    login: "Login",
    logout: "Logout",
    history: "Visit History",
    no_history: "No visit history yet.",
    welcome: "Welcome,",
    login_desc: "Login to save your exploration history in Jogja.",
    close: "Close",
  }
};

export type Language = "id" | "en";
export type Theme = "light" | "dark";

export interface HistoryItem {
  id: string;
  name: string;
  category: string;
  timestamp: number;
}

"use client";

import { useState, useEffect } from "react";
import Navigation from "../components/Navigation";
import WisataTab from "../components/WisataTab";
import RentalTab from "../components/RentalTab";
import KulinerTab from "../components/KulinerTab";
import { ALL_WILAYAH, Wilayah } from "../data/mockData";
import { Map, Car, Coffee } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";
import { useAppContext } from "../context/AppContext";
import { dict } from "../i18n/dict";

type TabType = "wisata" | "rental" | "kuliner";

export default function Home() {
    const { language } = useAppContext();
    const t = dict[language];
    
    const [selectedWilayah, setSelectedWilayah] = useState<Wilayah>(ALL_WILAYAH[0]);
    const [activeTab, setActiveTab] = useState<TabType>("wisata");
    
    // State untuk data API
    const [dataWisata, setDataWisata] = useState([]);
    const [dataRental, setDataRental] = useState([]);
    const [dataKuliner, setDataKuliner] = useState([]);
    const [loading, setLoading] = useState(true);

    // Fetch data setiap kali wilayah berubah
    useEffect(() => {
        const fetchData = async () => {
            setLoading(true);
            try {
                const baseUrl = process.env.NEXT_PUBLIC_API_URL || "http://localhost:4000/api";
                
                const [resWisata, resRental, resKuliner] = await Promise.all([
                    fetch(`${baseUrl}/wisata?wilayah=${selectedWilayah}`).then(res => res.ok ? res.json() : []),
                    fetch(`${baseUrl}/rental?wilayah=${selectedWilayah}`).then(res => res.ok ? res.json() : []),
                    fetch(`${baseUrl}/kuliner?wilayah=${selectedWilayah}`).then(res => res.ok ? res.json() : [])
                ]);

                setDataWisata(resWisata);
                setDataRental(resRental);
                setDataKuliner(resKuliner);
            } catch (error) {
                console.error("Gagal mengambil data dari API Gateway:", error);
            } finally {
                setLoading(false);
            }
        };

        fetchData();
    }, [selectedWilayah]);

    // Deskripsi per wilayah
    const deskripsiWilayahId: Record<Wilayah, string> = {
        "Kota Yogyakarta": "Jantung budaya dan sejarah DIY. Temukan keraton yang megah, jalanan ikonik Malioboro, serta kuliner legendaris di setiap sudut kota.",
        "Sleman": "Kawasan utara yang sejuk di lereng Gunung Merapi. Terkenal dengan candi-candi purbakala, wisata alam pegunungan, dan kafe-kafe kekinian.",
        "Bantul": "Sentra kerajinan dan pesisir selatan yang eksotis. Nikmati deburan ombak di Parangtritis, hutan pinus yang tenang, hingga sate klatak yang menggugah selera.",
        "Gunungkidul": "Surga tersembunyi dengan deretan pantai pasir putih yang menawan, gua-gua vertikal, dan kuliner eksotis khas pesisir.",
        "Kulon Progo": "Perpaduan pegunungan Menoreh dan hamparan sawah. Destinasi tepat untuk mencari ketenangan alam, air terjun alami, dan wisata waduk."
    };

    const deskripsiWilayahEn: Record<Wilayah, string> = {
        "Kota Yogyakarta": "The cultural and historical heart of DIY. Discover the majestic palace, iconic Malioboro street, and legendary culinary spots in every corner.",
        "Sleman": "The cool northern area on the slopes of Mount Merapi. Famous for ancient temples, mountain nature tourism, and trendy cafes.",
        "Bantul": "The center of crafts and exotic southern coast. Enjoy the crashing waves at Parangtritis, serene pine forests, and appetizing sate klatak.",
        "Gunungkidul": "A hidden paradise with a stretch of charming white sand beaches, vertical caves, and exotic coastal culinary.",
        "Kulon Progo": "A blend of Menoreh mountains and rice fields. The right destination to find natural tranquility, natural waterfalls, and reservoir tourism."
    };

    const deskripsiWilayah = language === "en" ? deskripsiWilayahEn : deskripsiWilayahId;

    return (
        <main className="min-h-screen pb-20 relative">
            <Navigation selectedWilayah={selectedWilayah} onWilayahChange={setSelectedWilayah} />

            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-8">
                <header className="mb-10 text-center md:text-left">
                    <motion.h1 
                        key={selectedWilayah}
                        initial={{ opacity: 0, y: -20 }}
                        animate={{ opacity: 1, y: 0 }}
                        className="text-4xl md:text-5xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-indigo-600 mb-4 tracking-tight dark:from-blue-400 dark:to-indigo-400"
                    >
                        {language === "id" ? "Eksplorasi" : "Explore"} {selectedWilayah}
                    </motion.h1>
                    <motion.p 
                        key={`${selectedWilayah}-desc`}
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        transition={{ delay: 0.1 }}
                        className="text-slate-500 dark:text-slate-400 text-lg max-w-3xl leading-relaxed"
                    >
                        {deskripsiWilayah[selectedWilayah]}
                    </motion.p>
                </header>

                {/* Tab Navigation */}
                <div className="flex p-1 bg-white/60 dark:bg-slate-800/60 backdrop-blur-md rounded-2xl shadow-sm border border-slate-200/50 dark:border-slate-700/50 mb-8 max-w-2xl mx-auto md:mx-0">
                    {[
                        { id: "wisata", label: t.wisata_tab, icon: Map },
                        { id: "rental", label: t.rental_tab, icon: Car },
                        { id: "kuliner", label: t.kuliner_tab, icon: Coffee },
                    ].map((tab) => {
                        const Icon = tab.icon;
                        const isActive = activeTab === tab.id;
                        return (
                            <button
                                key={tab.id}
                                onClick={() => setActiveTab(tab.id as TabType)}
                                className={`flex-1 flex items-center justify-center gap-2 py-3 px-4 rounded-xl font-semibold text-sm transition-all duration-300 relative ${
                                    isActive ? "text-primary dark:text-blue-400" : "text-slate-500 dark:text-slate-400 hover:text-slate-800 dark:hover:text-slate-200 hover:bg-white/50 dark:hover:bg-slate-700/50"
                                }`}
                            >
                                {isActive && (
                                    <motion.div
                                        layoutId="active-main-tab"
                                        className="absolute inset-0 bg-white dark:bg-slate-700 rounded-xl shadow-sm border border-slate-100 dark:border-slate-600"
                                        transition={{ type: "spring", stiffness: 400, damping: 30 }}
                                    />
                                )}
                                <span className="relative z-10 flex items-center gap-2">
                                    <Icon size={18} />
                                    <span className="hidden sm:inline">{tab.label}</span>
                                </span>
                            </button>
                        );
                    })}
                </div>

                {/* Tab Content with Animation */}
                <div className="min-h-[500px] relative">
                    {loading ? (
                        <div className="absolute inset-0 flex flex-col items-center justify-center pt-20">
                            <div className="w-12 h-12 border-4 border-slate-200 dark:border-slate-700 border-t-primary dark:border-t-blue-500 rounded-full animate-spin mb-4"></div>
                            <p className="text-slate-500 dark:text-slate-400 font-medium">
                                {language === "id" ? "Memuat data terbaru dari server..." : "Loading latest data from server..."}
                            </p>
                        </div>
                    ) : (
                        <AnimatePresence mode="wait">
                            <motion.div
                                key={`${selectedWilayah}-${activeTab}`}
                                initial={{ opacity: 0, y: 10 }}
                                animate={{ opacity: 1, y: 0 }}
                                exit={{ opacity: 0, y: -10 }}
                                transition={{ duration: 0.2 }}
                            >
                                {activeTab === "wisata" && <WisataTab data={dataWisata} />}
                                {activeTab === "rental" && <RentalTab data={dataRental} />}
                                {activeTab === "kuliner" && <KulinerTab data={dataKuliner} />}
                            </motion.div>
                        </AnimatePresence>
                    )}
                </div>
            </div>
        </main>
    );
}

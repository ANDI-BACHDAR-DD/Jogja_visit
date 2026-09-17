import { TempatWisata } from "../data/mockData";
import { Star, MapPin, ExternalLink } from "lucide-react";
import { motion } from "framer-motion";
import { useAppContext } from "../context/AppContext";
import { dict } from "../i18n/dict";

export default function WisataTab({ data }: { data: TempatWisata[] }) {
    const { language, addHistory } = useAppContext();
    const t = dict[language];

    const sortedData = [...data].sort((a, b) => b.rating - a.rating);

    const handleVisit = (item: TempatWisata) => {
        addHistory({
            name: item.nama,
            category: t.wisata_tab
        });
    };

    if (sortedData.length === 0) {
        return <div className="text-center text-slate-500 dark:text-slate-400 py-10">Data tidak ditemukan.</div>;
    }

    return (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {sortedData.map((item, index) => (
                <motion.div 
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: index * 0.05 }}
                    key={item.id} 
                    className="glass-card rounded-2xl overflow-hidden group flex flex-col h-full"
                >
                    <div className="relative h-48 sm:h-56 overflow-hidden">
                        <img 
                            src={item.gambar} 
                            alt={item.nama} 
                            className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
                        />
                        <div className="absolute top-3 left-3 bg-white/90 dark:bg-slate-800/90 backdrop-blur-sm px-3 py-1 rounded-full text-xs font-bold text-slate-700 dark:text-slate-200">
                            {item.kategori_wisata}
                        </div>
                    </div>
                    <div className="p-5 flex-1 flex flex-col">
                        <div className="flex justify-between items-start mb-2 gap-2">
                            <h3 className="font-bold text-lg text-slate-800 dark:text-slate-100 leading-tight">{item.nama}</h3>
                            <div className="flex items-center bg-orange-50 dark:bg-orange-900/30 text-orange-600 dark:text-orange-400 px-2 py-1 rounded-lg shrink-0">
                                <Star size={14} className="fill-current mr-1" />
                                <span className="font-bold text-sm">{item.rating}</span>
                            </div>
                        </div>
                        <p className="text-slate-500 dark:text-slate-400 text-sm mb-4 line-clamp-2 flex-1">
                            {item.deskripsi}
                        </p>
                        <div className="flex items-center text-slate-400 dark:text-slate-500 text-sm mb-4">
                            <MapPin size={14} className="mr-1 shrink-0" />
                            <span className="truncate">{item.alamat}</span>
                        </div>
                        <div className="flex items-center justify-between mt-auto pt-4 border-t border-slate-100 dark:border-slate-700/50">
                            <div className="text-sm font-medium text-slate-600 dark:text-slate-300">
                                <span className="text-xs text-slate-400 dark:text-slate-500 block">{t.ticket}</span>
                                {item.estimasi_harga_tiket}
                            </div>
                            <a 
                                href={item.link_gmaps} 
                                target="_blank" 
                                rel="noopener noreferrer"
                                onClick={() => handleVisit(item)}
                                className="text-sm font-semibold text-primary dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 bg-blue-50 dark:bg-blue-900/30 hover:bg-blue-100 dark:hover:bg-blue-900/50 px-4 py-2 rounded-xl transition"
                            >
                                {t.open_maps} &rarr;
                            </a>
                        </div>
                    </div>
                </motion.div>
            ))}
        </div>
    );
}

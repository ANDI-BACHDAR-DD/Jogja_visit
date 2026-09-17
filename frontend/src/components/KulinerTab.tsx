import { Kuliner } from "../data/mockData";
import { Star, MapPin, Coffee } from "lucide-react";
import { motion } from "framer-motion";
import { useAppContext } from "../context/AppContext";
import { dict } from "../i18n/dict";

export default function KulinerTab({ data }: { data: Kuliner[] }) {
    const { language, addHistory } = useAppContext();
    const t = dict[language];

    const sortedData = [...data].sort((a, b) => b.rating - a.rating);

    const handleVisit = (item: Kuliner) => {
        addHistory({
            name: item.nama,
            category: t.kuliner_tab
        });
    };

    if (sortedData.length === 0) {
        return (
            <div className="flex flex-col items-center justify-center py-20 text-slate-400 dark:text-slate-500">
                <Coffee size={48} className="mb-4 opacity-20" />
                <p>Belum ada data tempat kuliner di wilayah ini.</p>
            </div>
        );
    }

    return (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {sortedData.map((item, index) => (
                <motion.div
                    initial={{ opacity: 0, scale: 0.95 }}
                    animate={{ opacity: 1, scale: 1 }}
                    transition={{ delay: index * 0.05 }}
                    key={item.id || (item as any).place_id || index}
                    className="glass-card rounded-2xl p-4 flex gap-4 items-center group"
                >
                    <div className="w-24 h-24 shrink-0 rounded-xl overflow-hidden shadow-sm bg-orange-100 dark:bg-orange-950/30 flex items-center justify-center">
                        {item.gambar ? (
                            <img src={item.gambar} alt={item.nama} className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" />
                        ) : (
                            <Coffee size={28} className="text-orange-500" />
                        )}
                    </div>
                    
                    <div className="flex-1 min-w-0">
                        <h3 className="font-bold text-slate-800 dark:text-slate-100 truncate">{item.nama}</h3>
                        <p className="text-sm text-slate-500 dark:text-slate-400 mb-2 truncate">{item.jenis_masakan}</p>
                        
                        <div className="flex items-center gap-3 text-sm">
                            <div className="flex items-center text-orange-500">
                                <Star size={14} className="fill-current mr-1 text-amber-500 fill-amber-500" />
                                <span className="font-semibold text-slate-700 dark:text-slate-300">{item.rating}</span>
                                <span className="text-slate-400 dark:text-slate-500 ml-1">({item.jumlah_ulasan})</span>
                            </div>
                            <div className="flex items-center text-slate-400 dark:text-slate-500">
                                <MapPin size={12} className="mr-1" />
                                <span className="truncate">{item.wilayah}</span>
                            </div>
                        </div>
                    </div>
                    
                    <div className="flex flex-col gap-2 items-end shrink-0">
                        <span className="text-sm font-semibold text-emerald-600 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-900/30 px-2 py-1 rounded-lg border border-emerald-100 dark:border-emerald-800/50">
                            {item.rentang_harga}
                        </span>
                        {item.link_gmaps && (
                            <a 
                                href={item.link_gmaps} 
                                target="_blank" 
                                rel="noopener noreferrer"
                                onClick={() => handleVisit(item)}
                                className="text-xs font-semibold text-primary dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 bg-blue-50 dark:bg-blue-950/50 hover:bg-blue-100 dark:hover:bg-blue-900/50 px-3 py-1.5 rounded-lg transition-colors"
                            >
                                {t.open_maps}
                            </a>
                        )}
                    </div>
                </motion.div>
            ))}
        </div>
    );
}

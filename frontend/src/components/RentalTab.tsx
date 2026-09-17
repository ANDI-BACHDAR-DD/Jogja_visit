import { Rental } from "../data/mockData";
import { Star, MessageCircle, MapPin, Car } from "lucide-react";
import { motion } from "framer-motion";
import { useAppContext } from "../context/AppContext";
import { dict } from "../i18n/dict";

export default function RentalTab({ data }: { data: Rental[] }) {
    const { language, addHistory } = useAppContext();
    const t = dict[language];

    const sortedData = [...data].sort((a, b) => b.rating - a.rating);

    const handleVisit = (item: Rental, isWa = false) => {
        addHistory({
            name: `${item.nama} ${isWa ? '(WA)' : '(Maps)'}`,
            category: t.rental_tab
        });
    };

    if (sortedData.length === 0) {
        return (
            <div className="flex flex-col items-center justify-center py-20 text-slate-400 dark:text-slate-500">
                <Car size={48} className="mb-4 opacity-20" />
                <p>Belum ada data rental kendaraan di wilayah ini.</p>
            </div>
        );
    }

    return (
        <div className="flex flex-col gap-4">
            {sortedData.map((item, index) => (
                <motion.div
                    initial={{ opacity: 0, x: -20 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ delay: index * 0.05 }}
                    key={item.id || (item as any)._id || index}
                    className="glass-card rounded-2xl p-5 sm:p-6 flex flex-col sm:flex-row sm:items-center justify-between gap-6 group"
                >
                    <div className="flex items-start gap-4 flex-1 min-w-0">
                        <div className="w-20 h-20 sm:w-24 sm:h-24 rounded-xl bg-blue-100 dark:bg-blue-900/30 flex items-center justify-center flex-shrink-0 overflow-hidden shadow-sm">
                            {(item as any).gambar ? (
                                <img src={(item as any).gambar} alt={item.nama} className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" />
                            ) : (
                                <Car size={24} className="text-blue-600 dark:text-blue-400" />
                            )}
                        </div>
                        <div className="flex-1 min-w-0">
                            <h3 className="text-lg font-bold text-slate-800 dark:text-slate-100 flex flex-wrap items-center gap-2">
                                <span className="truncate">{item.nama}</span>
                                <span className="px-2 py-0.5 rounded text-[10px] font-bold uppercase tracking-wider bg-slate-100 dark:bg-slate-700 text-slate-500 dark:text-slate-400 shrink-0">
                                    {item.jenis_kendaraan}
                                </span>
                            </h3>
                            
                            <div className="flex items-center gap-4 mt-2">
                                <div className="flex items-center gap-1.5 text-sm text-slate-600 dark:text-slate-300">
                                    <Star size={16} className="text-amber-500 fill-amber-500" />
                                    <span className="font-semibold">{item.rating}</span>
                                    <span className="text-slate-400 dark:text-slate-500">({item.jumlah_ulasan})</span>
                                </div>
                                <div className="flex items-center gap-1 text-sm text-slate-500 dark:text-slate-400 truncate">
                                    <MapPin size={14} className="shrink-0" />
                                    <span className="truncate">{item.wilayah}</span>
                                </div>
                            </div>
                            <div className="mt-3 text-sm font-medium text-slate-700 dark:text-slate-300 bg-slate-50 dark:bg-slate-700/50 inline-block px-3 py-1 rounded-lg border border-slate-100 dark:border-slate-600">
                                {t.price}: {item.harga}
                            </div>
                            {(item as any).link_gmaps && (
                                <div className="mt-2">
                                    <a 
                                        href={(item as any).link_gmaps} 
                                        target="_blank" 
                                        rel="noopener noreferrer"
                                        onClick={() => handleVisit(item)}
                                        className="inline-flex items-center gap-1 text-xs font-semibold text-primary dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300 transition-colors bg-blue-50 dark:bg-blue-900/30 hover:bg-blue-100 dark:hover:bg-blue-900/50 px-3 py-1.5 rounded-lg"
                                    >
                                        {t.open_maps}
                                    </a>
                                </div>
                            )}
                        </div>
                    </div>
                    
                    <a
                        href={item.tautan_wa}
                        target="_blank"
                        rel="noopener noreferrer"
                        onClick={() => handleVisit(item, true)}
                        className="group/btn flex items-center justify-center gap-2 bg-[#25D366] hover:bg-[#128C7E] text-white px-5 py-3 rounded-xl font-semibold transition-all shadow-md shadow-green-500/20 hover:shadow-lg hover:shadow-green-500/30 w-full sm:w-auto shrink-0"
                    >
                        <MessageCircle size={20} className="group-hover/btn:animate-bounce" />
                        {t.chat_wa}
                    </a>
                </motion.div>
            ))}
        </div>
    );
}

"use client";

import { MapPin } from "lucide-react";
import { ALL_WILAYAH, Wilayah } from "../data/mockData";
import { motion } from "framer-motion";
import Header from "./Header";

interface NavigationProps {
    selectedWilayah: Wilayah;
    onWilayahChange: (wilayah: Wilayah) => void;
}

export default function Navigation({ selectedWilayah, onWilayahChange }: NavigationProps) {
    return (
        <nav className="sticky top-0 z-50 glass-panel border-b border-slate-200 dark:border-slate-800">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex flex-col md:flex-row justify-between items-center h-auto md:h-16 py-4 md:py-0 gap-4">
                    
                    <div className="flex items-center justify-between w-full md:w-auto gap-4">
                        <div className="flex items-center gap-2">
                            <div className="bg-primary/10 dark:bg-blue-900/30 p-2 rounded-xl text-primary dark:text-blue-400">
                                <MapPin size={24} strokeWidth={2.5} />
                            </div>
                            <span className="text-xl font-bold text-slate-800 dark:text-slate-100 tracking-tight">JogjaVisit</span>
                        </div>
                        {/* Header untuk versi Mobile (muncul di sebelah kanan logo) */}
                        <div className="md:hidden">
                            <Header />
                        </div>
                    </div>

                    <div className="flex items-center gap-2 overflow-x-auto w-full md:flex-1 md:justify-center pb-2 md:pb-0 hide-scrollbar">
                        {ALL_WILAYAH.map((wilayah) => {
                            const isSelected = selectedWilayah === wilayah;
                            return (
                                <button
                                    key={wilayah}
                                    onClick={() => onWilayahChange(wilayah)}
                                    className={`relative px-4 py-2 rounded-full text-sm font-medium transition-all duration-300 whitespace-nowrap ${
                                        isSelected
                                            ? "text-primary dark:text-blue-400 shadow-sm"
                                            : "text-slate-500 dark:text-slate-400 hover:text-slate-800 dark:hover:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800"
                                    }`}
                                >
                                    {isSelected && (
                                        <motion.div
                                            layoutId="active-pill"
                                            className="absolute inset-0 bg-primary/10 dark:bg-blue-900/40 rounded-full"
                                            transition={{ type: "spring", stiffness: 400, damping: 30 }}
                                        />
                                    )}
                                    <span className="relative z-10">{wilayah}</span>
                                </button>
                            );
                        })}
                    </div>

                    {/* Header untuk versi Desktop (muncul di kanan ujung bar) */}
                    <div className="hidden md:flex items-center">
                        <Header />
                    </div>
                    
                </div>
            </div>
        </nav>
    );
}

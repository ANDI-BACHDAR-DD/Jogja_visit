"use client";

import React, { useState } from "react";
import { Settings, User, Globe, Moon, Sun, History, LogIn, LogOut, X } from "lucide-react";
import { useAppContext } from "../context/AppContext";
import { dict } from "../i18n/dict";
import { motion, AnimatePresence } from "framer-motion";

export default function Header() {
  const { theme, setTheme, language, setLanguage, user, login, logout, history } = useAppContext();
  const [showSettings, setShowSettings] = useState(false);
  const [showProfile, setShowProfile] = useState(false);

  const t = dict[language];

  return (
    <div className="flex items-center space-x-3 relative z-50">
      {/* Settings Button */}
      <div className="relative">
        <button
          onClick={() => {
            setShowSettings(!showSettings);
            setShowProfile(false);
          }}
          className="p-2 bg-white/80 dark:bg-slate-800/80 backdrop-blur-md rounded-full shadow-md text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-700 transition"
          title={t.settings}
        >
          <Settings size={20} />
        </button>

        <AnimatePresence>
          {showSettings && (
            <motion.div
              initial={{ opacity: 0, y: -10 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -10 }}
              className="absolute right-0 mt-2 w-48 bg-white dark:bg-slate-800 rounded-xl shadow-xl border border-slate-200 dark:border-slate-700 p-2"
            >
              <div className="text-sm font-semibold text-slate-500 dark:text-slate-400 p-2 border-b border-slate-100 dark:border-slate-700 mb-1">
                {t.settings}
              </div>
              
              <div className="flex flex-col space-y-1">
                {/* Language Toggle */}
                <button
                  onClick={() => setLanguage(language === "id" ? "en" : "id")}
                  className="flex items-center space-x-3 p-2 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-700 transition"
                >
                  <Globe size={16} />
                  <span className="text-sm">{t.language}: {language.toUpperCase()}</span>
                </button>

                {/* Theme Toggle */}
                <button
                  onClick={() => setTheme(theme === "light" ? "dark" : "light")}
                  className="flex items-center space-x-3 p-2 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-700 transition"
                >
                  {theme === "light" ? <Moon size={16} /> : <Sun size={16} />}
                  <span className="text-sm">{theme === "light" ? t.dark_mode : t.light_mode}</span>
                </button>
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </div>

      {/* Profile Button */}
      <div className="relative">
        <button
          onClick={() => {
            setShowProfile(!showProfile);
            setShowSettings(false);
          }}
          className="p-2 bg-white/80 dark:bg-slate-800/80 backdrop-blur-md rounded-full shadow-md text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-700 transition"
          title={t.profile}
        >
          <User size={20} />
        </button>

        <AnimatePresence>
          {showProfile && (
            <motion.div
              initial={{ opacity: 0, y: -10 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -10 }}
              className="absolute right-0 mt-2 w-72 bg-white dark:bg-slate-800 rounded-xl shadow-xl border border-slate-200 dark:border-slate-700 p-4"
            >
              <div className="flex justify-between items-center mb-4">
                <h3 className="font-bold text-lg dark:text-white">{t.profile}</h3>
                <button onClick={() => setShowProfile(false)} className="text-slate-400 hover:text-slate-600 dark:hover:text-slate-300">
                  <X size={18} />
                </button>
              </div>

              {!user.isLoggedIn ? (
                <div className="text-center py-4">
                  <User size={48} className="mx-auto text-slate-300 dark:text-slate-600 mb-3" />
                  <p className="text-sm text-slate-500 dark:text-slate-400 mb-4">{t.login_desc}</p>
                  <button
                    onClick={login}
                    className="w-full py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg flex items-center justify-center space-x-2 transition"
                  >
                    <LogIn size={16} />
                    <span>{t.login}</span>
                  </button>
                </div>
              ) : (
                <div>
                  <div className="flex items-center space-x-3 mb-4 p-3 bg-blue-50 dark:bg-blue-900/30 rounded-lg">
                    <div className="w-10 h-10 bg-blue-600 text-white rounded-full flex items-center justify-center font-bold">
                      {user.name.charAt(0)}
                    </div>
                    <div>
                      <div className="text-xs text-slate-500 dark:text-slate-400">{t.welcome}</div>
                      <div className="font-bold dark:text-white">{user.name}</div>
                    </div>
                  </div>

                  <div className="mb-4">
                    <h4 className="flex items-center space-x-2 text-sm font-semibold text-slate-700 dark:text-slate-300 mb-2 border-b border-slate-100 dark:border-slate-700 pb-1">
                      <History size={14} />
                      <span>{t.history}</span>
                    </h4>
                    <div className="max-h-48 overflow-y-auto space-y-2 pr-1">
                      {history.length === 0 ? (
                        <p className="text-xs text-slate-400 italic text-center py-2">{t.no_history}</p>
                      ) : (
                        history.map((h) => (
                          <div key={h.id} className="text-xs p-2 bg-slate-50 dark:bg-slate-700/50 rounded flex justify-between">
                            <div className="truncate pr-2 font-medium dark:text-slate-200">{h.name}</div>
                            <div className="text-slate-400 flex-shrink-0 text-[10px]">
                              {new Date(h.timestamp).toLocaleDateString()}
                            </div>
                          </div>
                        ))
                      )}
                    </div>
                  </div>

                  <button
                    onClick={logout}
                    className="w-full py-2 border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-700 text-slate-600 dark:text-slate-300 rounded-lg flex items-center justify-center space-x-2 transition"
                  >
                    <LogOut size={16} />
                    <span>{t.logout}</span>
                  </button>
                </div>
              )}
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </div>
  );
}

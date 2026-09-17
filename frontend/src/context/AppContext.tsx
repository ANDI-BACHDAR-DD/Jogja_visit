"use client";

import React, { createContext, useContext, useEffect, useState } from "react";
import { Language, Theme, HistoryItem } from "../i18n/dict";

interface User {
  name: string;
  isLoggedIn: boolean;
}

interface AppContextType {
  theme: Theme;
  setTheme: (theme: Theme) => void;
  language: Language;
  setLanguage: (lang: Language) => void;
  user: User;
  login: () => void;
  logout: () => void;
  history: HistoryItem[];
  addHistory: (item: Omit<HistoryItem, "id" | "timestamp">) => void;
  clearHistory: () => void;
}

const AppContext = createContext<AppContextType | undefined>(undefined);

export function AppProvider({ children }: { children: React.ReactNode }) {
  const [theme, setThemeState] = useState<Theme>("light");
  const [language, setLanguageState] = useState<Language>("id");
  const [user, setUser] = useState<User>({ name: "", isLoggedIn: false });
  const [history, setHistory] = useState<HistoryItem[]>([]);
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    // Load from localStorage on mount
    const savedTheme = localStorage.getItem("theme") as Theme;
    if (savedTheme) setThemeState(savedTheme);

    const savedLang = localStorage.getItem("language") as Language;
    if (savedLang) setLanguageState(savedLang);

    const savedUser = localStorage.getItem("user");
    if (savedUser) setUser(JSON.parse(savedUser));

    const savedHistory = localStorage.getItem("history");
    if (savedHistory) setHistory(JSON.parse(savedHistory));
    
    setMounted(true);
  }, []);

  const setTheme = (t: Theme) => {
    setThemeState(t);
    localStorage.setItem("theme", t);
  };

  const setLanguage = (l: Language) => {
    setLanguageState(l);
    localStorage.setItem("language", l);
  };

  const login = () => {
    const newUser = { name: "Traveler", isLoggedIn: true };
    setUser(newUser);
    localStorage.setItem("user", JSON.stringify(newUser));
  };

  const logout = () => {
    const newUser = { name: "", isLoggedIn: false };
    setUser(newUser);
    localStorage.setItem("user", JSON.stringify(newUser));
  };

  const addHistory = (item: Omit<HistoryItem, "id" | "timestamp">) => {
    if (!user.isLoggedIn) return; // Only track if logged in
    const newItem: HistoryItem = {
      ...item,
      id: Math.random().toString(36).substr(2, 9),
      timestamp: Date.now(),
    };
    
    setHistory((prev) => {
      // Don't add if the very last item visited is the exact same (prevent double clicks)
      if (prev.length > 0 && prev[0].name === item.name) return prev;
      
      const newHistory = [newItem, ...prev].slice(0, 50); // Keep last 50
      localStorage.setItem("history", JSON.stringify(newHistory));
      return newHistory;
    });
  };

  const clearHistory = () => {
    setHistory([]);
    localStorage.removeItem("history");
  };

  // Sync theme to HTML element
  useEffect(() => {
    if (mounted) {
      if (theme === "dark") {
        document.documentElement.classList.add("dark");
      } else {
        document.documentElement.classList.remove("dark");
      }
    }
  }, [theme, mounted]);

  if (!mounted) {
    // Prevent hydration mismatch by not rendering until mounted
    return null;
  }

  return (
    <AppContext.Provider
      value={{
        theme,
        setTheme,
        language,
        setLanguage,
        user,
        login,
        logout,
        history,
        addHistory,
        clearHistory,
      }}
    >
      {children}
    </AppContext.Provider>
  );
}

export function useAppContext() {
  const context = useContext(AppContext);
  if (context === undefined) {
    throw new Error("useAppContext must be used within an AppProvider");
  }
  return context;
}

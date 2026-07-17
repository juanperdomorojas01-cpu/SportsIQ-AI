"use client";

import { Bell, Search } from "lucide-react";

export default function AppHeader() {
  return (
    <header className="flex h-16 items-center justify-between border-b bg-white px-6 shadow-sm">
      <div className="relative w-96">
        <Search className="absolute left-3 top-3 h-4 w-4 text-slate-400" />

        <input
          className="w-full rounded-lg border border-slate-200 py-2 pl-10 pr-4 text-sm outline-none focus:border-green-500"
          placeholder="Buscar equipos, ligas o partidos..."
        />
      </div>

      <div className="flex items-center gap-5">
        <Bell className="h-5 w-5 text-slate-500" />

        <div className="h-10 w-10 rounded-full bg-gradient-to-r from-green-500 to-blue-600" />
      </div>
    </header>
  );
}
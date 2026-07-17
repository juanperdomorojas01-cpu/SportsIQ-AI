"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

import {
  BarChart3,
  BrainCircuit,
  CalendarDays,
  Home,
  Settings,
  Trophy,
  Users,
} from "lucide-react";

const menu = [
  {
    title: "Dashboard",
    href: "/dashboard",
    icon: Home,
  },
  {
    title: "Ligas",
    href: "/leagues",
    icon: Trophy,
  },
  {
    title: "Equipos",
    href: "/teams",
    icon: Users,
  },
  {
    title: "Partidos",
    href: "/fixtures",
    icon: CalendarDays,
  },
  {
    title: "Predicciones IA",
    href: "/predictions",
    icon: BrainCircuit,
  },
  {
    title: "Estadísticas",
    href: "/statistics",
    icon: BarChart3,
  },
  {
    title: "Configuración",
    href: "/settings",
    icon: Settings,
  },
];

export default function AppSidebar() {
  const pathname = usePathname();

  return (
    <aside className="w-72 bg-slate-950 text-white">
      <div className="border-b border-slate-800 p-6">
        <h1 className="bg-gradient-to-r from-green-400 to-blue-500 bg-clip-text text-2xl font-bold text-transparent">
          SportsIQ AI
        </h1>

        <p className="mt-1 text-sm text-slate-400">
          Sports Analytics Platform
        </p>
      </div>

      <nav className="p-4">
        <ul className="space-y-2">
          {menu.map((item) => {
            const Icon = item.icon;

            const active = pathname === item.href;

            return (
              <li key={item.title}>
                <Link
                  href={item.href}
                  className={`flex items-center gap-3 rounded-xl px-4 py-3 transition ${
                    active
                      ? "bg-gradient-to-r from-green-500 to-blue-600"
                      : "hover:bg-slate-800"
                  }`}
                >
                  <Icon size={20} />

                  {item.title}
                </Link>
              </li>
            );
          })}
        </ul>
      </nav>
    </aside>
  );
}
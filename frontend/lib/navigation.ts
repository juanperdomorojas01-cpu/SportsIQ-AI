import {
  BarChart3,
  BrainCircuit,
  CalendarDays,
  Home,
  Settings,
  ShieldCheck,
  Trophy,
  Users,
} from "lucide-react";

export const navigation = [
  {
    title: "Dashboard",
    url: "/dashboard",
    icon: Home,
  },
  {
    title: "Ligas",
    url: "/leagues",
    icon: Trophy,
  },
  {
    title: "Equipos",
    url: "/teams",
    icon: Users,
  },
  {
    title: "Partidos",
    url: "/fixtures",
    icon: CalendarDays,
  },
  {
    title: "Predicciones IA",
    url: "/predictions",
    icon: BrainCircuit,
  },
  {
    title: "Estadísticas",
    url: "/statistics",
    icon: BarChart3,
  },
  {
    title: "Administración",
    url: "/admin",
    icon: ShieldCheck,
  },
  {
    title: "Configuración",
    url: "/settings",
    icon: Settings,
  },
];
"use client";

import {
  CalendarDays,
  Trophy,
  Users,
  BarChart3,
} from "lucide-react";

import MetricCard from "@/components/dashboard/MetricCard";
import { useDashboard } from "../hooks/useDashboard";

export default function DashboardCards() {
  const {
    data,
    loading,
    error,
  } = useDashboard();

  if (loading) {
    return (
      <div className="text-slate-500">
        Cargando Dashboard...
      </div>
    );
  }

  if (error) {
    return (
      <div className="rounded-xl border border-red-200 bg-red-50 p-5 text-red-600">
        {error}
      </div>
    );
  }

  if (!data) return null;

  return (
    <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
      <MetricCard
        title="Ligas"
        value={data.leagues}
        icon={<Trophy size={28} />}
        description="Ligas sincronizadas"
      />

      <MetricCard
        title="Equipos"
        value={data.teams}
        icon={<Users size={28} />}
        description="Equipos registrados"
      />

      <MetricCard
        title="Partidos"
        value={data.fixtures}
        icon={<CalendarDays size={28} />}
        description="Partidos almacenados"
      />

      <MetricCard
        title="Standings"
        value={data.standings}
        icon={<BarChart3 size={28} />}
        description="Tablas de posiciones"
      />
    </div>
  );
}
"use client";

import { useEffect, useState } from "react";

import { getDashboard } from "@/services/dashboard.service";
import type { DashboardResponse } from "@/types/dashboard";

export function useDashboard() {
  const [data, setData] = useState<DashboardResponse | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const loadDashboard = async () => {
    try {
      setLoading(true);

      const response = await getDashboard();

      setData(response);

      setError(null);
    } catch (err) {
      console.error(err);

      setError("No fue posible cargar el Dashboard.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadDashboard();
  }, []);

  return {
    data,
    loading,
    error,
    reload: loadDashboard,
  };
}
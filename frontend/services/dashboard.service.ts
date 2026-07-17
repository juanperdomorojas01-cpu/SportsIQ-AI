import { apiFetch } from "./api";

import type { DashboardResponse } from "@/types/dashboard";

export async function getDashboard(): Promise<DashboardResponse> {
  return apiFetch<DashboardResponse>("/dashboard");
}
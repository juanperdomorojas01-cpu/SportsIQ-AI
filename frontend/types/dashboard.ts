export interface DashboardResponse {
  leagues: number;
  teams: number;
  fixtures: number;
  standings: number;
  last_sync: string | null;
}
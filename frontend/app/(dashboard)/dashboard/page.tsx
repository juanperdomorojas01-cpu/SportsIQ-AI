import DashboardCards from "@/features/dashboard/components/DashboardCards";

export default function DashboardPage() {
  return (
    <div className="space-y-8">

      <div>

        <h1 className="text-4xl font-bold text-slate-800">
          Dashboard
        </h1>

        <p className="mt-2 text-slate-500">
          Resumen general de SportsIQ AI
        </p>

      </div>

      <DashboardCards />

    </div>
  );
}
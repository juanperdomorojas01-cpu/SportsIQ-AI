import { ReactNode } from "react";

interface MetricCardProps {
  title: string;
  value: number;
  icon: ReactNode;
  description: string;
}

export default function MetricCard({
  title,
  value,
  icon,
  description,
}: MetricCardProps) {
  return (
    <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-xl">
      <div className="flex items-start justify-between">

        <div>

          <p className="text-sm font-medium text-slate-500">
            {title}
          </p>

          <h2 className="mt-3 text-5xl font-bold text-slate-800">
            {value.toLocaleString()}
          </h2>

          <p className="mt-4 text-sm text-slate-500">
            {description}
          </p>

        </div>

        <div className="rounded-2xl bg-gradient-to-br from-green-500 to-blue-600 p-4 text-white shadow-lg">
          {icon}
        </div>

      </div>
    </div>
  );
}
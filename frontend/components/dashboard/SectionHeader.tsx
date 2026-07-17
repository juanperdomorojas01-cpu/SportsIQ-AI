interface SectionHeaderProps {
  title: string;
  subtitle?: string;
}

export default function SectionHeader({
  title,
  subtitle,
}: SectionHeaderProps) {
  return (
    <div className="mb-8">
      <h1 className="text-4xl font-bold tracking-tight text-slate-800">
        {title}
      </h1>

      {subtitle && (
        <p className="mt-2 text-base text-slate-500">
          {subtitle}
        </p>
      )}
    </div>
  );
}
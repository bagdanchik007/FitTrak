type Props = { title: string; hint?: string };

export function EmptyState({ title, hint }: Props) {
  return (
    <div className="rounded-xl border border-dashed border-slate-700 bg-slate-900/30 px-4 py-8 text-center">
      <p className="text-sm font-medium text-slate-300">{title}</p>
      {hint && <p className="mt-1 text-xs text-slate-500">{hint}</p>}
    </div>
  );
}

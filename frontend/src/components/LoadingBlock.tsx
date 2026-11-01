export function LoadingBlock({ label = "Loading…" }: { label?: string }) {
  return (
    <div className="flex items-center gap-2 py-6 text-sm text-slate-400">
      <span
        className="inline-block h-4 w-4 animate-spin rounded-full border-2 border-slate-600 border-t-brand-500"
        aria-hidden
      />
      {label}
    </div>
  );
}

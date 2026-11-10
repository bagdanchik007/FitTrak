import { cn } from "../lib/cn";

type Props = { value: number; className?: string };

export function ProgressBar({ value, className }: Props) {
  const pct = Math.min(100, Math.max(0, value));
  return (
    <div className={cn("h-2 overflow-hidden rounded-full bg-slate-800", className)}>
      <div className="h-full rounded-full bg-brand-500 transition-all" style={{ width: `${pct}%` }} />
    </div>
  );
}

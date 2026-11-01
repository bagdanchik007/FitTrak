type Props = { children: React.ReactNode; tone?: "brand" | "muted" | "success" };

export function Badge({ children, tone = "brand" }: Props) {
  const tones = {
    brand: "bg-brand-600/20 text-brand-500",
    muted: "bg-slate-800 text-slate-400",
    success: "bg-emerald-900/40 text-emerald-400",
  };
  return (
    <span className={`rounded-full px-2 py-0.5 text-xs font-medium ${tones[tone]}`}>
      {children}
    </span>
  );
}

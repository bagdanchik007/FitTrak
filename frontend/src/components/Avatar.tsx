import { initials } from "../lib/initials";

type Props = { name?: string | null; size?: "sm" | "md" };

export function Avatar({ name, size = "md" }: Props) {
  const dim = size === "sm" ? "h-8 w-8 text-xs" : "h-10 w-10 text-sm";
  return (
    <span
      className={`inline-flex ${dim} items-center justify-center rounded-full bg-slate-800 font-semibold text-brand-500`}
      aria-hidden
    >
      {initials(name)}
    </span>
  );
}

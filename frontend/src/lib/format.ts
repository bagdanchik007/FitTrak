export function formatKg(value: number | null | undefined): string {
  if (value == null || Number.isNaN(value)) return "—";
  return `${Number(value).toFixed(1)} kg`;
}

export function formatMinutes(value: number | null | undefined): string {
  if (value == null) return "—";
  return `${value} min`;
}

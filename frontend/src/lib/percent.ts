export function percentOf(current: number, target: number): number | null {
  if (target <= 0) return null;
  return Math.round(Math.min(100, Math.max(0, (current / target) * 100)) * 10) / 10;
}

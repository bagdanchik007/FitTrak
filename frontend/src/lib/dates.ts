export function toInputDate(d: Date = new Date()): string {
  return d.toISOString().slice(0, 10);
}

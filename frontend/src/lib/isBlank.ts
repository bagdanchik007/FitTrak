export function isBlank(value: string | null | undefined): boolean {
  return !value || !value.trim();
}

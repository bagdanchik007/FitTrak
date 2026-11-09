export function initials(name?: string | null, maxChars = 2): string {
  const parts = (name || "").split(/\s+/).filter(Boolean);
  if (!parts.length) return "?";
  return parts
    .slice(0, maxChars)
    .map((p) => p[0]!.toUpperCase())
    .join("")
    .slice(0, maxChars);
}

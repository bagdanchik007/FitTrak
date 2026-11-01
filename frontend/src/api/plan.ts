import { apiFetch } from "./client";

export function fetchNextSplit(lastFocus?: string) {
  const q = lastFocus ? `?last_focus=${encodeURIComponent(lastFocus)}` : "";
  return apiFetch<{ focus: string; label: string }>(`/meta/next-split${q}`);
}

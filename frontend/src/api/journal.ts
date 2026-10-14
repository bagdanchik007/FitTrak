import { apiFetch } from "./client";

export type JournalEntry = {
  id: string;
  mood?: string | null;
  notes?: string | null;
  entry_date?: string | null;
  created_at?: string;
};

export function fetchJournal(): Promise<JournalEntry[]> {
  return apiFetch<JournalEntry[]>("/journal");
}

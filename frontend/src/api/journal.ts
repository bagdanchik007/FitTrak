import { apiFetch } from "./client";

export type JournalEntry = {
  id: string;
  title?: string;
  body?: string;
  mood?: string | null;
  created_at?: string;
};

export function fetchJournal(): Promise<JournalEntry[]> {
  return apiFetch<JournalEntry[]>("/journal");
}

export function createJournalEntry(body: {
  title: string;
  body: string;
  mood?: string | null;
}): Promise<JournalEntry> {
  return apiFetch<JournalEntry>("/journal", {
    method: "POST",
    body: JSON.stringify(body),
  });
}

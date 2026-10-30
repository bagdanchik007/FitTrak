import { apiFetch } from "./client";

export type RecoveryHint = {
  rest_recommended: boolean;
  reason: string;
};

export function fetchRecoveryHint(trainedLast7Days: number): Promise<RecoveryHint> {
  return apiFetch<RecoveryHint>(
    `/meta/recovery-hint?trained_last_7_days=${trainedLast7Days}`,
  );
}

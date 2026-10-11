export type TokenResponse = {
  access_token: string;
  refresh_token: string;
  token_type?: string;
  access_expires_in?: number;
  refresh_expires_in?: number;
};

export type UserMe = {
  id: string;
  email: string;
  full_name?: string | null;
  is_active?: boolean;
};

export type Dashboard = {
  total_workouts?: number;
  total_volume_kg?: number;
  active_goals?: number;
  current_streak?: number;
  [key: string]: unknown;
};

export type Workout = {
  id: string;
  title: string;
  performed_at: string;
  duration_minutes?: number | null;
  total_volume_kg?: number | null;
};

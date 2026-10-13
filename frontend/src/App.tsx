import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import { Layout } from "./components/Layout";
import { Dashboard } from "./pages/Dashboard";
import { Goals } from "./pages/Goals";
import { Home } from "./pages/Home";
import { Login } from "./pages/Login";
import { Notifications } from "./pages/Notifications";
import { LiveSession } from "./pages/LiveSession";
import { Streaks } from "./pages/Streaks";
import { Register } from "./pages/Register";
import { Workouts } from "./pages/Workouts";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="login" element={<Login />} />
          <Route path="register" element={<Register />} />
          <Route path="dashboard" element={<Dashboard />} />
          <Route path="workouts" element={<Workouts />} />
          <Route path="goals" element={<Goals />} />
          <Route path="notifications" element={<Notifications />} />
          <Route path="streaks" element={<Streaks />} />
          <Route path="live" element={<LiveSession />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

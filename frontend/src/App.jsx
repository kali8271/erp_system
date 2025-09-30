import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Accounts from "./pages/Accounts";
import Finance from "./pages/Finance";
import Attendance from "./pages/Attendance";
import Timetable from "./pages/Timetable";
import Notices from "./pages/Notices";
import Exams from "./pages/Exams";
import ProtectedRoute from "./api/ProtectedRoute";

function App() {
  return (
    <Router>
      <Routes>
        {/* Public Route */}
        <Route path="/" element={<Login />} />

        {/* Protected Routes */}
        <Route
          path="/dashboard"
          element={
            <ProtectedRoute allowedRoles={["admin", "teacher", "student"]}>
              <Dashboard />
            </ProtectedRoute>
          }
        />

        <Route
          path="/accounts"
          element={
            <ProtectedRoute allowedRoles={["admin"]}>
              <Accounts />
            </ProtectedRoute>
          }
        />

        <Route
          path="/finance"
          element={
            <ProtectedRoute allowedRoles={["admin"]}>
              <Finance />
            </ProtectedRoute>
          }
        />

        <Route
          path="/attendance"
          element={
            <ProtectedRoute allowedRoles={["admin", "teacher"]}>
              <Attendance />
            </ProtectedRoute>
          }
        />

        <Route
          path="/timetable"
          element={
            <ProtectedRoute allowedRoles={["admin", "teacher", "student"]}>
              <Timetable />
            </ProtectedRoute>
          }
        />

        <Route
          path="/notices"
          element={
            <ProtectedRoute allowedRoles={["admin", "teacher", "student"]}>
              <Notices />
            </ProtectedRoute>
          }
        />

        <Route
          path="/exams"
          element={
            <ProtectedRoute allowedRoles={["admin", "teacher"]}>
              <Exams />
            </ProtectedRoute>
          }
        />
      </Routes>
    </Router>
  );
}

export default App;

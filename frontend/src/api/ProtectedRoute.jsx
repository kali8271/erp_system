import { Navigate } from "react-router-dom";
import { getUserRole } from "./auth";

export default function ProtectedRoute({ children, allowedRoles }) {
  const role = getUserRole();

  if (!allowedRoles.includes(role)) {
    return <Navigate to="/dashboard" replace />;
  }

  return children;
}

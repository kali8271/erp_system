
import { jwtDecode } from "jwt-decode";



export function saveAuthTokens(data) {
  localStorage.setItem("access", data.access);
  localStorage.setItem("refresh", data.refresh);

  // Decode role from JWT access token
  const decoded = jwtDecode(data.access);
  localStorage.setItem("role", decoded.role || "student"); // fallback
}

export function getUserRole() {
  return localStorage.getItem("role");
}

export function logout() {
  localStorage.removeItem("access");
  localStorage.removeItem("refresh");
  localStorage.removeItem("role");
  window.location.href = "/login";
}

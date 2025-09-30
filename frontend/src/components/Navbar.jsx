import { logout } from "../utils/auth";

export default function Navbar() {
  return (
    <nav className="p-4 bg-gray-800 text-white flex justify-between">
      <h1>University ERP</h1>
      <button onClick={logout} className="bg-red-500 px-4 py-1 rounded">
        Logout
      </button>
    </nav>
  );
}

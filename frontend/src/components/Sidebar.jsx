import { Link } from "react-router-dom";
import { getUserRole } from "../utils/auth";

export default function Sidebar() {
  const role = getUserRole();

  return (
    <aside className="w-64 bg-gray-800 text-white min-h-screen p-6">
      <ul className="space-y-4">
        <li>
          <Link to="/dashboard" className="hover:text-yellow-400">
            Dashboard
          </Link>
        </li>

        {/* Accounts → only for Admin */}
        {role === "admin" && (
          <li>
            <Link to="/accounts" className="hover:text-yellow-400">
              Accounts
            </Link>
          </li>
        )}

        {/* Finance → only for Admin */}
        {role === "admin" && (
          <li>
            <Link to="/finance" className="hover:text-yellow-400">
              Finance
            </Link>
          </li>
        )}

        {/* Attendance → Teachers & Admin */}
        {(role === "teacher" || role === "admin") && (
          <li>
            <Link to="/attendance" className="hover:text-yellow-400">
              Attendance
            </Link>
          </li>
        )}

        {/* Timetable → All users */}
        <li>
          <Link to="/timetable" className="hover:text-yellow-400">
            Timetable
          </Link>
        </li>

        {/* Notices → All users */}
        <li>
          <Link to="/notices" className="hover:text-yellow-400">
            Notices
          </Link>
        </li>

        {/* Exams → Teachers & Admin */}
        {(role === "teacher" || role === "admin") && (
          <li>
            <Link to="/exams" className="hover:text-yellow-400">
              Exams
            </Link>
          </li>
        )}
      </ul>
    </aside>
  );
}

// src/pages/Dashboard.jsx
import { useEffect, useState } from "react";
import api from "../api/api";

function Dashboard() {
  const [accounts, setAccounts] = useState([]);

  useEffect(() => {
    async function fetchAccounts() {
      try {
        const res = await api.get("accounts/"); // Authorization auto-added
        setAccounts(res.data);
      } catch (err) {
        console.error("Error fetching accounts:", err);
      }
    }
    fetchAccounts();
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Dashboard</h1>
      <h2 className="text-lg font-semibold mb-2">Accounts</h2>
      <ul className="list-disc pl-6">
        {accounts.map((acc, i) => (
          <li key={i}>{acc.username || JSON.stringify(acc)}</li>
        ))}
      </ul>
    </div>
  );
}

export default Dashboard;

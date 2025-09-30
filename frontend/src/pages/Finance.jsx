import { useEffect, useState } from "react";
import API from "../api/api";

function Finance() {
  const [fees, setFees] = useState([]);

  useEffect(() => {
    API.get("finance/fees/")
      .then((res) => setFees(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="p-8">
      <h2 className="text-2xl mb-4">Finance</h2>
      <ul>
        {fees.map((fee) => (
          <li key={fee.id}>
            Student: {fee.student} — Amount: {fee.amount} — Status: {fee.status}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Finance;

import { useEffect, useState } from "react";
import API from "../api/api";

function Attendance() {
  const [records, setRecords] = useState([]);

  useEffect(() => {
    API.get("attendance/records/")
      .then((res) => setRecords(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="p-8">
      <h2 className="text-2xl mb-4">Attendance</h2>
      <ul>
        {records.map((rec) => (
          <li key={rec.id}>
            Student: {rec.student} — Date: {rec.date} — Present:{" "}
            {rec.present ? "Yes" : "No"}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Attendance;

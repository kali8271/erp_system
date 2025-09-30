import { useEffect, useState } from "react";
import API from "../api/api";

function Timetable() {
  const [entries, setEntries] = useState([]);

  useEffect(() => {
    API.get("timetable/timetables/")
      .then((res) => setEntries(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="p-8">
      <h2 className="text-2xl mb-4">Timetable</h2>
      <ul>
        {entries.map((entry) => (
          <li key={entry.id}>
            Course: {entry.course} — Room: {entry.room} — Day: {entry.day} — Time:{" "}
            {entry.start_time} to {entry.end_time}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Timetable;

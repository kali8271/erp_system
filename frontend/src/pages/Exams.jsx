import { useEffect, useState } from "react";
import API from "../api/api";

function Exams() {
  const [exams, setExams] = useState([]);

  useEffect(() => {
    API.get("exams/exams/")
      .then((res) => setExams(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="p-8">
      <h2 className="text-2xl mb-4">Exams</h2>
      <ul>
        {exams.map((exam) => (
          <li key={exam.id}>
            Course: {exam.course} — Date: {exam.date} — Marks: {exam.total_marks}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Exams;

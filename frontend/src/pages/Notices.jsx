import { useEffect, useState } from "react";
import API from "../api/api";

function Notices() {
  const [notices, setNotices] = useState([]);

  useEffect(() => {
    API.get("notices/notices/")
      .then((res) => setNotices(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="p-8">
      <h2 className="text-2xl mb-4">Notices</h2>
      <ul>
        {notices.map((notice) => (
          <li key={notice.id}>
            <strong>{notice.title}</strong> — {notice.content} (
            {new Date(notice.created_at).toLocaleDateString()})
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Notices;

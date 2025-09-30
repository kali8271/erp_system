import { useEffect, useState } from "react";
import API from "../api/api";

function Accounts() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    API.get("accounts/users/")
      .then((res) => setUsers(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="p-8">
      <h2 className="text-2xl mb-4">Accounts</h2>
      <ul>
        {users.map((user) => (
          <li key={user.id}>
            {user.username} ({user.role})
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Accounts;

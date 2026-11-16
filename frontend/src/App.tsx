import { useEffect, useState } from 'react';

interface User {
  id: number;
  name: string;
}

function App() {
  const [message, setMessage] = useState('');
  const [users, setUsers] = useState<User[]>([]);

  useEffect(() => {
    // Get message from the backend
    fetch('http://127.0.0.1:8000/')
      .then(response => response.json())
      .then(data => setMessage(data.message));

      // Get the list of users from the backend
      fetch('http://127.0.0.1:8000/api/users')
        .then(response => response.json())
        .then(data => setUsers(data));
  }, []);

  return (
    <div>
      <h1>My Application</h1>

      <h2>{message}</h2>

      <h3>Users</h3>

      {users.map(user => (
        <p key={user.id}>
          {user.id} - {user.name}
        </p>
      ))}
    </div>
  );
}

export default App;

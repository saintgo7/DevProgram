// API route: /api/users
export default function handler(req, res) {
  if (req.method === 'GET') {
    const users = [
      { id: 1, name: 'Alice', email: 'alice@example.com' },
      { id: 2, name: 'Bob', email: 'bob@example.com' },
      { id: 3, name: 'Charlie', email: 'charlie@example.com' }
    ];
    res.status(200).json(users);
  } else if (req.method === 'POST') {
    const newUser = req.body;
    res.status(201).json({ message: 'User created', user: newUser });
  } else {
    res.status(405).json({ error: 'Method not allowed' });
  }
}

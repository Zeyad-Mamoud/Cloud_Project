import { useEffect, useState } from 'react';

function Home() {
  const [loans, setLoans] = useState([]);

  useEffect(() => {
    // Fetch loans from API
    fetch('http://localhost:8000/loans')
      .then(res => res.json())
      .then(data => setLoans(data));
  }, []);

  return (
    <div>
      <h1>Loan Tracking System</h1>
      <ul>
        {loans.map(loan => (
          <li key={loan.id}>
            {loan.amount} - Due: {loan.due_date} - Status: {loan.status}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Home;

import React, { useState } from 'react';
import './App.css';

function App() {
  const [loan, setLoan] = useState({
    amount: '',
    dueDate: '',
    loanType: 'borrowed',
    contactId: ''
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:8000/loans', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          amount: parseFloat(loan.amount),
          due_date: loan.dueDate,
          loan_type: loan.loanType,
          contact_id: parseInt(loan.contactId),
          status: 'active',  
          remaining_balance: parseFloat(loan.amount)
        }),
      });
      if (response.ok) {
        alert('Loan added successfully!');
        setLoan({ amount: '', dueDate: '', loanType: 'borrowed', contactId: '' });
      } else {
        const errorData = await response.json();
        alert(`Error adding loan: ${response.status} - ${JSON.stringify(errorData)}`);
      }
    } catch (error) {
      console.error('Error:', error);
      alert(`Error adding loan: ${error.message}`);
    }
  };

  return (
    <div className="App">
      <h1>Loan Tracking System</h1>
      <h2>Add Loan</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Amount: </label>
          <input
            type="number"
            value={loan.amount}
            onChange={(e) => setLoan({ ...loan, amount: e.target.value })}
            required
          />
        </div>
        <div>
          <label>Due Date: </label>
          <input
            type="date"
            value={loan.dueDate}
            onChange={(e) => setLoan({ ...loan, dueDate: e.target.value })}
            required
          />
        </div>
        <div>
          <label>Loan Type: </label>
          <select
            value={loan.loanType}
            onChange={(e) => setLoan({ ...loan, loanType: e.target.value })}
          >
            <option value="borrowed">Borrowed</option>
            <option value="lent">Lent</option>
          </select>
        </div>
        <div>
          <label>Contact ID: </label>
          <input
            type="number"
            value={loan.contactId}
            onChange={(e) => setLoan({ ...loan, contactId: e.target.value })}
            required
          />
        </div>
        <button type="submit">Add Loan</button>
      </form>
    </div>
  );
}

export default App;

import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  // State for loan form
  const [amount, setAmount] = useState('');
  const [dueDate, setDueDate] = useState('');
  const [loanType, setLoanType] = useState('borrowed');
  const [contactId, setContactId] = useState('');
  const [message, setMessage] = useState('');

  // State for contacts form
  const [name, setName] = useState('');
  const [phone, setPhone] = useState('');
  const [email, setEmail] = useState('');

  // State for displaying contacts and loans
  const [contacts, setContacts] = useState([]);
  const [loans, setLoans] = useState([]);

  // State for partial payment
  const [partialPaymentAmount, setPartialPaymentAmount] = useState({});

  // Fetch contacts and loans on component mount
  useEffect(() => {
    fetchContacts();
    fetchLoans();
  }, []);

  const fetchContacts = async () => {
    try {
      const response = await fetch('http://localhost:8000/contacts/');
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Failed to fetch contacts');
      }
      const data = await response.json();
      setContacts(data);
    } catch (error) {
      console.error('Error fetching contacts:', error.message);
      setMessage(`Error fetching contacts: ${error.message}`);
    }
  };

  const fetchLoans = async () => {
    try {
      const response = await fetch('http://localhost:8000/loans/');
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Failed to fetch loans');
      }
      const data = await response.json();
      setLoans(data);
    } catch (error) {
      console.error('Error fetching loans:', error.message);
      setMessage(`Error fetching loans: ${error.message}`);
    }
  };

  const handleLoanSubmit = async (e) => {
    e.preventDefault();
    const loanData = {
      amount: parseFloat(amount),
      due_date: dueDate,
      loan_type: loanType.toUpperCase(), // تحويل لـ"BORROWED" أو "LENT"
      contact_id: parseInt(contactId),
    };

    try {
      const response = await fetch('http://localhost:8000/loans/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(loanData),
      });
      if (response.ok) {
        setMessage('Loan added successfully!');
        fetchLoans();
        // Reset form
        setAmount('');
        setDueDate('');
        setLoanType('borrowed');
        setContactId('');
      } else {
        const errorData = await response.json();
        const errorMessage = errorData.detail
          ? Array.isArray(errorData.detail)
            ? errorData.detail.map(d => d.msg).join(', ')
            : errorData.detail
          : 'Failed to add loan';
        setMessage(`Error: ${errorMessage}`);
        console.error('Error adding loan:', errorData);
      }
    } catch (error) {
      setMessage(`Error: ${error.message}`);
      console.error('Error:', error.message);
    }
  };

  const handleContactSubmit = async (e) => {
    e.preventDefault();
    const contactData = { name, phone, email };

    try {
      const response = await fetch('http://localhost:8000/contacts/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(contactData),
      });
      if (response.ok) {
        setMessage('Contact added successfully!');
        fetchContacts();
        // Reset form
        setName('');
        setPhone('');
        setEmail('');
      } else {
        const errorData = await response.json();
        const errorMessage = errorData.detail
          ? Array.isArray(errorData.detail)
            ? errorData.detail.map(d => d.msg).join(', ')
            : errorData.detail
          : 'Failed to add contact';
        setMessage(`Error: ${errorMessage}`);
        console.error('Error adding contact:', errorData);
      }
    } catch (error) {
      setMessage(`Error: ${error.message}`);
      console.error('Error:', error.message);
    }
  };

  const markAsPaid = async (loanId) => {
    try {
      const response = await fetch(`http://localhost:8000/loans/${loanId}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ status: 'PAID' }), // كابيتال لتطابق الـEnum
      });
      if (response.ok) {
        setMessage('Loan marked as paid!');
        fetchLoans();
      } else {
        const errorData = await response.json();
        setMessage(`Error: ${errorData.detail || 'Failed to update loan'}`);
      }
    } catch (error) {
      setMessage(`Error: ${error.message}`);
      console.error('Error:', error.message);
    }
  };

  const markAsPartiallyPaid = async (loanId) => {
    const paymentAmount = parseFloat(partialPaymentAmount[loanId] || 0);
    if (!paymentAmount || paymentAmount <= 0) {
      setMessage('Please enter a valid payment amount.');
      return;
    }

    try {
      const response = await fetch(`http://localhost:8000/loans/${loanId}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ status: 'PARTIALLY_PAID', payment_amount: paymentAmount }), // كابيتال لتطابق الـEnum
      });
      if (response.ok) {
        setMessage('Loan marked as partially paid!');
        fetchLoans();
        setPartialPaymentAmount({ ...partialPaymentAmount, [loanId]: '' }); // Reset payment amount
      } else {
        const errorData = await response.json();
        setMessage(`Error: ${errorData.detail || 'Failed to update loan'}`);
      }
    } catch (error) {
      setMessage(`Error: ${error.message}`);
      console.error('Error:', error.message);
    }
  };

  return (
    <div className="App">
      <h1>Loan Tracking System</h1>

      {/* Form to add a contact */}
      <h2>Add Contact</h2>
      <form onSubmit={handleContactSubmit}>
        <div>
          <label>Name:</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Phone:</label>
          <input
            type="text"
            value={phone}
            onChange={(e) => setPhone(e.target.value)}
          />
        </div>
        <div>
          <label>Email:</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
        <button type="submit">Add Contact</button>
      </form>

      {/* Table to display contacts */}
      <h2>Contacts</h2>
      {contacts.length > 0 ? (
        <table border="1">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Phone</th>
              <th>Email</th>
            </tr>
          </thead>
          <tbody>
            {contacts.map((contact) => (
              <tr key={contact.id}>
                <td>{contact.id}</td>
                <td>{contact.name}</td>
                <td>{contact.phone}</td>
                <td>{contact.email}</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>No contacts available.</p>
      )}

      {/* Form to add a loan */}
      <h2>Add Loan</h2>
      <form onSubmit={handleLoanSubmit}>
        <div>
          <label>Amount:</label>
          <input
            type="number"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Due Date:</label>
          <input
            type="date"
            value={dueDate}
            onChange={(e) => setDueDate(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Loan Type:</label>
          <select value={loanType} onChange={(e) => setLoanType(e.target.value)}>
            <option value="borrowed">Borrowed</option>
            <option value="lent">Lent</option>
          </select>
        </div>
        <div>
          <label>Contact ID:</label>
          <input
            type="number"
            value={contactId}
            onChange={(e) => setContactId(e.target.value)}
            required
          />
        </div>
        <button type="submit">Add Loan</button>
      </form>

      {/* Table to display loans */}
      <h2>Loans</h2>
      {loans.length > 0 ? (
        <table border="1">
          <thead>
            <tr>
              <th>ID</th>
              <th>Amount</th>
              <th>Due Date</th>
              <th>Loan Type</th>
              <th>Contact ID</th>
              <th>Status</th>
              <th>Remaining Balance</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {loans.map((loan) => (
              <tr key={loan.id}>
                <td>{loan.id}</td>
                <td>{loan.amount}</td>
                <td>{loan.due_date}</td>
                <td>{loan.loan_type}</td>
                <td>{loan.contact_id}</td>
                <td>{loan.status}</td>
                <td>{loan.remaining_balance}</td>
                <td>
                  {loan.status !== 'PAID' && (
                    <>
                      <button onClick={() => markAsPaid(loan.id)}>Mark as Paid</button>
                      <div>
                        <input
                          type="number"
                          placeholder="Payment Amount"
                          value={partialPaymentAmount[loan.id] || ''}
                          onChange={(e) =>
                            setPartialPaymentAmount({
                              ...partialPaymentAmount,
                              [loan.id]: e.target.value,
                            })
                          }
                        />
                        <button onClick={() => markAsPartiallyPaid(loan.id)}>
                          Partially Pay
                        </button>
                      </div>
                    </>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>No loans available.</p>
      )}

      {message && <p>{message}</p>}
    </div>
  );
}

export default App;
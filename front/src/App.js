import React, { useState, useEffect, useCallback } from 'react';
import { format, parseISO } from 'date-fns';
import './App.css';

function App() {
  const [amount, setAmount] = useState('');
  const [dueDate, setDueDate] = useState('');
  const [loanType, setLoanType] = useState('borrowed');
  const [contactId, setContactId] = useState('');
  const [message, setMessage] = useState('');
  const [name, setName] = useState('');
  const [phone, setPhone] = useState('');
  const [email, setEmail] = useState('');
  const [contacts, setContacts] = useState([]);
  const [loans, setLoans] = useState([]);
  const [filteredLoans, setFilteredLoans] = useState([]);
  const [sortBy, setSortBy] = useState('due_date');
  const [filterStatus, setFilterStatus] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [partialPaymentAmount, setPartialPaymentAmount] = useState({});
  const BACKEND_URL = process.env.REACT_APP_BACKEND_URL || 'https://4ce0-45-241-79-242.ngrok-free.app';

  const applyFiltersAndSort = useCallback((loansData) => {
    let updatedLoans = [...loansData];
    if (filterStatus) {
      updatedLoans = updatedLoans.filter((loan) => loan.status === filterStatus);
    }
    updatedLoans.sort((a, b) => {
      if (sortBy === 'due_date') {
        return new Date(a.due_date) - new Date(b.due_date);
      } else if (sortBy === 'status') {
        return a.status.localeCompare(b.status);
      } else if (sortBy === 'amount') {
        return a.amount - b.amount;
      }
      return 0;
    });
    setFilteredLoans(updatedLoans);
  }, [sortBy, filterStatus]);

  const fetchContacts = useCallback(async () => {
    setLoading(true);
    try {
      const response = await fetch(`${BACKEND_URL}/contacts/`, {
        headers: {
          'Content-Type': 'application/json',
          'ngrok-skip-browser-warning': 'true',
        },
      });
      if (!response.ok) {
        const text = await response.text();
        console.log('Contacts response:', text);
        try {
          const errorData = JSON.parse(text);
          throw new Error(errorData.detail || 'Failed to fetch contacts');
        } catch {
          throw new Error('Invalid response format: ' + text.substring(0, 100));
        }
      }
      const data = await response.json();
      setContacts(data);
    } catch (error) {
      console.error('Error fetching contacts:', error.message);
      setMessage(`Error fetching contacts: ${error.message}`);
    } finally {
      setLoading(false);
    }
  }, [BACKEND_URL]);

  const fetchLoans = useCallback(async () => {
    setLoading(true);
    try {
      const response = await fetch(`${BACKEND_URL}/loans/`, {
        headers: {
          'Content-Type': 'application/json',
          'ngrok-skip-browser-warning': 'true',
        },
      });
      if (!response.ok) {
        const text = await response.text();
        console.log('Loans response:', text);
        try {
          const errorData = JSON.parse(text);
          throw new Error(errorData.detail || 'Failed to fetch loans');
        } catch {
          throw new Error('Invalid response format: ' + text.substring(0, 100));
        }
      }
      const data = await response.json();
      setLoans(data);
      applyFiltersAndSort(data);
    } catch (error) {
      console.error('Error fetching loans:', error.message);
      setMessage(`Error fetching loans: ${error.message}`);
    } finally {
      setLoading(false);
    }
  }, [BACKEND_URL, applyFiltersAndSort]);

  const fetchData = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      await fetchContacts();
      await fetchLoans();
    } catch (err) {
      setError('Failed to load data. Please try again.');
    } finally {
      setLoading(false);
    }
  }, [fetchContacts, fetchLoans]);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  useEffect(() => {
    applyFiltersAndSort(loans);
  }, [loans, applyFiltersAndSort]);

  const handleLoanSubmit = async (e) => {
    e.preventDefault();
    const loanData = {
      amount: parseFloat(amount),
      due_date: dueDate,
      loan_type: loanType.toUpperCase(),
      contact_id: parseInt(contactId),
    };

    try {
      const response = await fetch(`${BACKEND_URL}/loans/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'ngrok-skip-browser-warning': 'true',
        },
        body: JSON.stringify(loanData),
      });
      if (response.ok) {
        setMessage('Loan added successfully!');
        fetchLoans();
        setAmount('');
        setDueDate('');
        setLoanType('borrowed');
        setContactId('');
      } else {
        const text = await response.text();
        console.log('Loan submit response:', text);
        try {
          const errorData = JSON.parse(text);
          const errorMessage = errorData.detail
            ? Array.isArray(errorData.detail)
              ? errorData.detail.map(d => d.msg).join(', ')
              : errorData.detail
            : 'Failed to add loan';
          setMessage(`Error: ${errorMessage}`);
        } catch {
          setMessage('Error: Invalid response format');
        }
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
      const response = await fetch(`${BACKEND_URL}/contacts/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'ngrok-skip-browser-warning': 'true',
        },
        body: JSON.stringify(contactData),
      });
      if (response.ok) {
        setMessage('Contact added successfully!');
        fetchContacts();
        setName('');
        setPhone('');
        setEmail('');
      } else {
        const text = await response.text();
        console.log('Contact submit response:', text);
        try {
          const errorData = JSON.parse(text);
          const errorMessage = errorData.detail
            ? Array.isArray(errorData.detail)
              ? errorData.detail.map(d => d.msg).join(', ')
              : errorData.detail
            : 'Failed to add contact';
          setMessage(`Error: ${errorMessage}`);
        } catch {
          setMessage('Error: Invalid response format');
        }
      }
    } catch (error) {
      setMessage(`Error: ${error.message}`);
      console.error('Error:', error.message);
    }
  };

  const markAsPaid = async (loanId) => {
    try {
      const response = await fetch(`${BACKEND_URL}/loans/${loanId}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
          'ngrok-skip-browser-warning': 'true',
        },
        body: JSON.stringify({ status: 'PAID' }),
      });
      if (response.ok) {
        setMessage('Loan marked as paid!');
        fetchLoans();
      } else {
        const text = await response.text();
        console.log('Mark as paid response:', text);
        try {
          const errorData = JSON.parse(text);
          setMessage(`Error: ${errorData.detail || 'Failed to update loan'}`);
        } catch {
          setMessage('Error: Invalid response format');
        }
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
      const response = await fetch(`${BACKEND_URL}/loans/${loanId}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
          'ngrok-skip-browser-warning': 'true',
        },
        body: JSON.stringify({ status: 'PARTIALLY_PAID', payment_amount: paymentAmount }),
      });
      if (response.ok) {
        setMessage('Loan marked as partially paid!');
        fetchLoans();
        setPartialPaymentAmount({ ...partialPaymentAmount, [loanId]: '' });
      } else {
        const text = await response.text();
        console.log('Mark as partially paid response:', text);
        try {
          const errorData = JSON.parse(text);
          setMessage(`Error: ${errorData.detail || 'Failed to update loan'}`);
        } catch {
          setMessage('Error: Invalid response format');
        }
      }
    } catch (error) {
      setMessage(`Error: ${error.message}`);
      console.error('Error:', error.message);
    }
  };

  const getContactName = (contactId) => {
    const contact = contacts.find(c => c.id === contactId);
    return contact ? contact.name : 'Unknown';
  };

  return (
    <div className="App">
      <h1>Loan Tracking System</h1>

      {loading && <p className="loading">Loading...</p>}
      {error && <p className="error">{error}</p>}

      <button onClick={fetchData} className="refresh-button">Refresh Data</button>

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

      <h2>Loans</h2>
      <div className="filters">
        <div>
          <label>Sort by: </label>
          <select value={sortBy} onChange={(e) => setSortBy(e.target.value)}>
            <option value="due_date">Due Date</option>
            <option value="status">Status</option>
            <option value="amount">Amount</option>
          </select>
        </div>
        <div>
          <label>Filter by Status: </label>
          <select value={filterStatus} onChange={(e) => setFilterStatus(e.target.value)}>
            <option value="">All</option>
            <option value="ACTIVE">Active</option>
            <option value="PARTIALLY_PAID">Partially Paid</option>
            <option value="PAID">Paid</option>
          </select>
        </div>
      </div>

      {filteredLoans.length > 0 ? (
        <table border="1">
          <thead>
            <tr>
              <th>ID</th>
              <th>Amount</th>
              <th>Due Date</th>
              <th>Loan Type</th>
              <th>Contact Name</th>
              <th>Status</th>
              <th>Remaining Balance</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {filteredLoans.map((loan) => (
              <tr key={loan.id}>
                <td>{loan.id}</td>
                <td>{loan.amount}</td>
                <td>{format(parseISO(loan.due_date), 'MMM dd, yyyy')}</td>
                <td>{loan.loan_type}</td>
                <td>{getContactName(loan.contact_id)}</td>
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

      {message && <p className="message">{message}</p>}
    </div>
  );
}

export default App;

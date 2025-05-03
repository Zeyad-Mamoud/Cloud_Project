import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './pages/Home';
import LoanForm from './components/LoanForm';

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/add-loan" component={LoanForm} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
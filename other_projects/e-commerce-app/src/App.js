import React from 'react';
import { Route, Switch } from 'react-router';
import './App.css';
import { Container } from 'reactstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import Navbar from './components/Navbar';
import { CartProvider } from './lib/cart.context';
import Category from './pages/Category';
import Checkout from './pages/Checkout';
import Home from './pages/Home';


function App() {
  return (
    <CartProvider>
      <Container>
    <Navbar />
    <Switch>
      <Route exact path="/">
        <Home />
      </Route>

      <Route exact path="/category/:id">
        <Category />
      </Route>

      <Route exact path="/checkout">
        <Checkout />
      </Route>
    </Switch>
    </Container>
    </CartProvider>
  )
}

export default App;

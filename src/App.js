import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import MyForm from './MyForm.js'


class App extends Component {
  /*constructor(props) {
    super(props);
    this.state ={
      items: [],
      isLoaded: false,
    }
  }

  componentDidMount(){
    fetch('https://jsonplaceholder.typicode.com/users')
      .then(res => res.json())
      .then(json => {
        this.setState({
          isLoaded: true,
          items: json,
        })
      });
  }*/

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={'logo-small.png'} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to Poirot</h1>
        </header>
        <p className="App-intro">
          Enter a political news article URL
        </p>
        <MyForm className="Form"> </MyForm>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
      </div>
    );
  }
}

export default App;

import React, { Component } from 'react';


class MyForm extends React.Component {
  constructor() {
    super();
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleSubmit(event) {
    event.preventDefault();
    const data = new FormData(event.target);
    
    fetch('/api/url=<url>', {
      method: 'POST',
      body: data,
    });
  }

  render() {
    
    return (
      <form onSubmit={this.handleSubmit}>
        <input id="url" name="url" type="text" />
        <button>Get Prediction</button>
      </form>
    );
  }
}

export default MyForm;
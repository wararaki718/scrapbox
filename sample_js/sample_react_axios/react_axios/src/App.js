import React, {Component, Fragment} from 'react';
import axios from 'axios'
import './App.css';


class App extends Component {
  constructor() {
    super();
    this.state = {
      message: 'none',
      accessTime: 'none'
    };
  }

  componentWillMount() {
    const request = axios.create({
      baseURL: 'http://localhost:5555'
    });
    request
      .get('/msg')
      .then(response => {
        console.log(response);
        this.setState({
          message: response.data.message,
          accessTime: response.data.time
        });
      });
  }

  render() {
    return (
      <Fragment>
        <div>server response message</div>
        <div>{this.state.message}</div>
        <div>{this.state.accessTime}</div>
      </Fragment>
    );
  }
}

export default App;

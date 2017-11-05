import React, { Component } from 'react';
import '../css/App.css';
import axios from 'axios';

class App extends Component {
   ledTrigger() {
      axios.post('https://p77rg9n9za.execute-api.us-west-2.amazonaws.com/stage1/control/1')
         .then(res => {
            console.log("API CALL - SUCCESS: led trigger")
         })
         .catch(res => {
            console.log("API CALL - FAIL: led trigger")
         })
   }
   render() {
      return (
         <div className="App">
            <div className="container-fluid">
               <div className="col">
                  <button type="button" className="btn btn-primary"
                     onClick={this.ledTrigger}>
                     LED Trigger
                  </button>
               </div>
            </div>
         </div>
      );
   }
}

export default App;

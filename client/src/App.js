import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import LocationTracker from "./nav.js";
import WebSocketComponent from "./WebSocketComponent.js";
import Map from "./Map.js";

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<WebSocketComponent />} />
          <Route path="/websocket" element={<WebSocketComponent />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;

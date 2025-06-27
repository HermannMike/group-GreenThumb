import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage';
import RemindersPage from './pages/RemindersPage';
import PlantsPage from './pages/PlantsPage';
import Navbar from './components/layout/Navbar';
import './App.css';

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/reminders" element={<RemindersPage />} />
        <Route path="/plants" element={<PlantsPage />} />
      </Routes>
    </Router>
  );
}

export default App;

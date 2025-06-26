import { Routes, Route } from "react-router-dom";
import Navbar from "./components/layout/Navbar";
import ProtectedRoute from "./components/layout/ProtectedRoute";
import HomePage from "./pages/HomePage";
import PlantsPage from "./pages/PlantsPage";
import RemindersPage from "./pages/RemindersPage";
import LoginForm from "./components/auth/LoginForm";
import RegisterForm from "./components/auth/RegisterForm";
import { AuthProvider } from "./context/AuthContext";
import NotFound from "./pages/NotFound";

const App = () => {
  return (
    <AuthProvider>
      <Navbar />
      <main className="container">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/login" element={<LoginForm />} />
          <Route path="/register" element={<RegisterForm />} />
          <Route
            path="/plants"
            element={
              <ProtectedRoute>
                <PlantsPage />
              </ProtectedRoute>
            }
          />
          <Route
            path="/reminders"
            element={
              <ProtectedRoute>
                <RemindersPage />
              </ProtectedRoute>
            }
          />
          <Route path="*" element={<NotFound />} /> 
        </Routes>
      </main>
    </AuthProvider>
  );
};

export default App;
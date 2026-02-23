import { useContext } from "react";
import { useNavigate } from "react-router-dom";
import { AuthContext } from "../context/AuthContext";
import "./Navbar.css";

function Navbar() {
  const { logout } = useContext(AuthContext);
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate("/");
  };

  return (
    <nav className="navbar">
      <div className="navbar-container">
        <h1 className="navbar-title">Health Tracker</h1>
        
        <div className="navbar-links">
          <button 
            onClick={() => navigate("/dashboard")}
            className="nav-button"
          >
            Dashboard
          </button>
          
          <button 
            onClick={() => navigate("/meals")}
            className="nav-button"
          >
            Meals
          </button>
          
          <button 
            onClick={() => navigate("/exercises")}
            className="nav-button"
          >
            Exercises
          </button>
          
          <button 
            onClick={() => navigate("/weight")}
            className="nav-button"
          >
            Weight
          </button>
          
          <button 
            onClick={handleLogout}
            className="nav-button logout-button"
          >
            Logout
          </button>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
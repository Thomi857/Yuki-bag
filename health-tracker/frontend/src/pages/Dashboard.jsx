// import { useEffect, useState } from "react";
// import api from "../api/axios";
// import Navbar from "../components/Navbar";

// function Dashboard() {
//   const [summary, setSummary] = useState(null);
//   const [loading, setLoading] = useState(true);
//   const [error, setError] = useState(null);

//   useEffect(() => {
//     let isMounted = true;

//     const fetchSummary = async () => {
//       try {
//         setLoading(true);
//         setError(null);
//         const res = await api.get("/dashboard/summary");
//         if (isMounted) {
//           setSummary(res.data);
//         }
//       } catch (err) {
//         if (isMounted) {
//           const status = err.response?.status;
//           const message = status === 401 
//             ? "Session expired. Please log in again."
//             : err.response?.data?.message || "Failed to load dashboard";
//           setError(message);
//         }
//       } finally {
//         if (isMounted) {
//           setLoading(false);
//         }
//       }
//     };

//     fetchSummary();

//     return () => {
//       isMounted = false;
//     };
//   }, []);

//   return (
//     <div>
//       <Navbar />
//       <h2>Dashboard</h2>

//       {loading && <p>Loading...</p>}
//       {error && <p style={{ color: "red" }}>Error: {error}</p>}
      
//       {summary && (
//         <div>
//           <p>Total Calories: {summary.total_calories}</p>
//           <p>Average Weight: {summary.average_weight}</p>
//           <p>Latest Weight: {summary.latest_weight}</p>
//           <p>Total Meals: {summary.total_meals}</p>
//           <p>Total Weight Entries: {summary.total_weight_entries}</p>
//         </div>
//       )}
//     </div>
//   );
// }

// export default Dashboard;

import { useEffect, useState, useContext } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/axios";
import Navbar from "../components/Navbar";
import { AuthContext } from "../context/AuthContext";  // 👈 add this

function Dashboard() {
  const { token, loading: authLoading } = useContext(AuthContext);  // 👈 add this
  const navigate = useNavigate();                                    // 👈 add this
  const [summary, setSummary] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (authLoading) return;        // ⏳ wait for AuthContext to initialize

    if (!token) {                   // 🚫 no token → send to login
      navigate("/");
      return;
    }

    let isMounted = true;

    const fetchSummary = async () => {
      try {
        setLoading(true);
        setError(null);
        const res = await api.get("/dashboard/summary");
        if (isMounted) setSummary(res.data);
      } catch (err) {
        if (isMounted) {
          const status = err.response?.status;
          const message = status === 401
            ? "Session expired. Please log in again."
            : err.response?.data?.message || "Failed to load dashboard";
          setError(message);
        }
      } finally {
        if (isMounted) setLoading(false);
      }
    };

    fetchSummary();
    return () => { isMounted = false; };

  }, [token, authLoading]);  // 👈 changed from [] to [token, authLoading]

   return (
    <div>
      <Navbar />
      <h2>Dashboard</h2>

      {loading && <p>Loading...</p>}
      {error && <p style={{ color: "red" }}>Error: {error}</p>}
      
      {summary && (
        <div>
          <p>Total Calories: {summary.total_calories}</p>
          <p>Average Weight: {summary.average_weight}</p>
          <p>Latest Weight: {summary.latest_weight}</p>
          <p>Total Meals: {summary.total_meals}</p>
          <p>Total Weight Entries: {summary.total_weight_entries}</p>
        </div>
      )}
    </div>
  );
}

export default Dashboard;
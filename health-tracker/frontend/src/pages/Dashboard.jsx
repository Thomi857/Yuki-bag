import { useEffect, useState } from "react";
import api from "../api/axios";
import Navbar from "../components/Navbar";

function Dashboard() {
  const [summary, setSummary] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let isMounted = true;

    const fetchSummary = async () => {
      try {
        setLoading(true);
        setError(null);
        const res = await api.get("/dashboard/summary");
        if (isMounted) {
          setSummary(res.data);
        }
      } catch (err) {
        if (isMounted) {
          setError(err.response?.data?.message || "Failed to load dashboard");
          console.error("Dashboard error:", err);
        }
      } finally {
        if (isMounted) {
          setLoading(false);
        }
      }
    };

    fetchSummary();

    return () => {
      isMounted = false;
    };
  }, []);

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
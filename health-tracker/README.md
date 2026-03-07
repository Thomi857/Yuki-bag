frontend/src/api/axios.js — Main configuration file that:

Creates an axios instance with base URL http://127.0.0.1:5000/api
Adds request interceptor to include Bearer token from localStorage
Includes response interceptor for error handling (401/403 redirects to home)
Files that use the axios API:

frontend/src/pages/Dashboard.jsx
frontend/src/pages/Login.jsx
frontend/src/pages/Register.jsx
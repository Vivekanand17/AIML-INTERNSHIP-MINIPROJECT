const API_BASE_URL =
  (typeof import.meta !== "undefined" &&
    import.meta.env &&
    import.meta.env.VITE_API_URL) ||
  "https://aiml-internship-miniproject-5.onrender.com";

export default API_BASE_URL;
export { API_BASE_URL };

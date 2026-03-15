import axios from "axios";
import { API_BASE_URL } from "./config";

export const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 15000
});

export function getErrorMessage(error) {
  if (error.response) {
    const status = error.response.status;
    const serverMsg =
      (error.response.data && error.response.data.detail) ||
      JSON.stringify(error.response.data);
    return `Server error (${status}): ${serverMsg}`;
  }

  if (error.request) {
    return `Cannot reach backend at ${API_BASE_URL}. Make sure it is running and accessible.`;
  }

  return `Unexpected error: ${error.message || String(error)}`;
}


import axios from "axios";

class ApiService {
  constructor(baseURL = "http://localhost:8000/api") {
    this.apiClient = axios.create({
      baseURL: baseURL,
      headers: {
        "Content-Type": "application/json",
      },
    });
  }

  async get(endpoint) {
    try {
      const response = await this.apiClient.get(endpoint);
      return response.data;
    } catch (error) {
      this.handleError(error);
    }
  }

  async post(endpoint, data) {
    try {
      const response = await this.apiClient.post(endpoint, data);
      return response.data;
    } catch (error) {
      this.handleError(error);
    }
  }

  async put(endpoint, data) {
    try {
      const response = await this.apiClient.put(endpoint, data);
      return response.data;
    } catch (error) {
      this.handleError(error);
    }
  }

  async delete(endpoint) {
    try {
      const response = await this.apiClient.delete(endpoint);
      return response.data;
    } catch (error) {
      this.handleError(error);
    }
  }

  handleError(error) {
    console.error("API Error:", error);
    throw error;
  }
}

export default ApiService;

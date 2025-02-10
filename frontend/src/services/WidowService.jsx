import ApiService from "./ApiService";

class WidowService {
  constructor() {
    this.apiService = new ApiService();
  }

  async getWidows() {
    try {
      const widows = await this.apiService.get(`/widows/`);
      //   console.log(widows);
      return widows;
    } catch (error) {
      console.error("Error fetching widows:", error);
    }
  }

  async getWidowById(widowID) {
    try {
      const widow = await this.apiService.get(`/widows.rel/${widowID}`);
      return widow;
    } catch (error) {
      console.error("Error fetching widow:", error);
    }
  }

  async createWidow(widowData) {
    try {
      const newWidow = await this.apiService.post(`/widows/`, widowData);
      return newWidow;
    } catch (error) {
      console.error("Error creating widow:", error);
    }
  }

  async updateWidow(widowID, widowData) {
    try {
      const updatedWidow = await this.apiService.put(
        `/widows/${widowID}`,
        widowData
      );
      //   console.log(updatedWidow);
      return updatedWidow;
    } catch (error) {
      console.error("Error updating widow:", error);
    }
  }

  async deleteWidow(widowID) {
    try {
      await this.apiService.delete(`/widows/${widowID}`);
    } catch (error) {
      console.error("Error deleting widow:", error);
    }
  }
}
export default WidowService;

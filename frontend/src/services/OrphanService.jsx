import ApiService from "./ApiService";

class OrphanService {
  constructor() {
    this.apiService = new ApiService();
  }

  async getOrphans() {
    try {
      const orphans = await this.apiService.get(`/orphans/`);
      //   console.log(orphans);
      return orphans;
    } catch (error) {
      console.error("Error fetching orphans:", error);
    }
  }

  async getOrphanById(orphanID) {
    try {
      const orphan = await this.apiService.get(`/orphans.rel/${orphanID}`);
      return orphan;
    } catch (error) {
      console.error("Error fetching orphan:", error);
    }
  }

  async createOrphan(orphanData) {
    try {
      const newOrphan = await this.apiService.post(`/orphans/`, orphanData);
      return newOrphan;
    } catch (error) {
      console.error("Error creating orphan:", error);
    }
  }

  async updateOrphan(orphanID, orphanData) {
    try {
      const updatedOrphan = await this.apiService.put(
        `/orphans/${orphanID}`,
        orphanData
      );
      //   console.log(updatedOrphan);
      return updatedOrphan;
    } catch (error) {
      console.error("Error updating orphan:", error);
    }
  }

  async deleteOrphan(orphanID) {
    try {
      await this.apiService.delete(`/orphans/${orphanID}`);
    } catch (error) {
      console.error("Error deleting orphan:", error);
    }
  }
}
export default OrphanService;

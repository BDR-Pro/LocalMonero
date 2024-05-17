import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  withCredentials: true,
});

export default {
  getUsers() {
    return apiClient.get('api/users/');
  },
  getTradeOffers() {
    return apiClient.get('api/trade_offers/');
  },
  getTransactions() {
    return apiClient.get('api/transactions/');
  },
  login(credentials) {
    return apiClient.post('/api-auth/login/', credentials);
  },
    signUp(credentials) {
        return apiClient.post('/api-auth/register/', credentials);
    },
  logout() {
    return apiClient.post('/api-auth/logout/');
  },
};

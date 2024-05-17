<template>
  <div>
    <h2>Trade Offers</h2>
    <b-table striped hover :items="tradeOffers"></b-table>
  </div>
</template>

<script>
import api from '../services/api';

export default {
  data() {
    return {
      tradeOffers: [],
    };
  },
  created() {
    this.fetchTradeOffers();
  },
  methods: {
    async fetchTradeOffers() {
      try {
        const response = await api.getTradeOffers();
        this.tradeOffers = response.data;
      } catch (error) {
        console.error('Error fetching trade offers:', error);
      }
    },
  },
};
</script>

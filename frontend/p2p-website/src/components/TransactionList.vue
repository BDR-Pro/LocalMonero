<template>
  <div>
    <h2>Transactions</h2>
    <b-table striped hover :items="transactions"></b-table>
  </div>
</template>

<script>
import api from '../services/api';

export default {
  data() {
    return {
      transactions: [],
    };
  },
  created() {
    this.fetchTransactions();
  },
  methods: {
    async fetchTransactions() {
      try {
        const response = await api.getTransactions();
        this.transactions = response.data;
      } catch (error) {
        console.error('Error fetching transactions:', error);
      }
    },
  },
};
</script>

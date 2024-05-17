<template>
  <div>
    <h2>Transaction Details</h2>
    <p><strong>Transaction ID:</strong> {{ transaction.id }}</p>
    <p><strong>Amount:</strong> {{ transaction.amount }}</p>
    <p><strong>Status:</strong> {{ transaction.status }}</p>

    <b-button @click="confirmPayment(transaction.id)" variant="primary">Confirm Payment</b-button>

    <div v-if="confirmationStatus" class="confirmation-status">
      {{ confirmationStatus }}
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Transaction',
  props: {
    transaction: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      confirmationStatus: '',
    };
  },
  methods: {
    async confirmPayment(transactionId) {
      try {
        const response = await axios.post(`http://localhost:8000/api/transactions/${transactionId}/confirm_payment/`);
        if (response.data.status === 'BTC payment confirmed' || response.data.status === 'Monero payment confirmed') {
          this.confirmationStatus = 'Payment confirmed';
        } else {
          this.confirmationStatus = 'Payment not confirmed';
        }
      } catch (error) {
        console.error('Error confirming payment:', error);
        this.confirmationStatus = 'Error confirming payment';
      }
    }
  }
};
</script>

<style scoped>
.confirmation-status {
  margin-top: 20px;
  font-weight: bold;
}
</style>

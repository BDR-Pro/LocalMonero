<template>
  <div>
    <h2>Login</h2>
    <b-form @submit.prevent="login">
      <b-form-group label="Username:" label-for="username">
        <b-form-input
          id="username"
          v-model="credentials.username"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group label="Password:" label-for="password">
        <b-form-input
          type="password"
          id="password"
          v-model="credentials.password"
          required
        ></b-form-input>
      </b-form-group>

      <b-button type="submit" variant="primary">Login</b-button>
    </b-form>
  </div>
</template>

<script>
import api from '../services/api';

export default {
  data() {
    return {
      credentials: {
        username: '',
        password: '',
      },
    };
  },
  methods: {
    async login() {
      try {
        await api.login(this.credentials);
        this.$router.push('/');
      } catch (error) {
        console.error('Error logging in:', error);
      }
    },
  },
};
</script>

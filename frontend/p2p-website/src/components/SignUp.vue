<template>
  <b-container class="mt-4">
    <b-row class="justify-content-md-center">
      <b-col md="6">
        <b-card title="Sign Up" class="text-center">
          <b-form @submit.prevent="onSubmit">
            <b-form-group label="Username" label-for="username">
              <b-form-input
                id="username"
                v-model="form.username"
                required
                placeholder="Enter your username"
              ></b-form-input>
            </b-form-group>

            <b-form-group label="Email" label-for="email">
              <b-form-input
                id="email"
                type="email"
                v-model="form.email"
                required
                placeholder="Enter your email"
              ></b-form-input>
            </b-form-group>

            <b-form-group label="Password" label-for="password">
              <b-form-input
                id="password"
                type="password"
                v-model="form.password"
                required
                placeholder="Enter your password"
              ></b-form-input>
            </b-form-group>

            <b-form-group label="Confirm Password" label-for="confirm-password">
              <b-form-input
                id="confirm-password"
                type="password"
                v-model="form.confirmPassword"
                required
                placeholder="Confirm your password"
              ></b-form-input>
            </b-form-group>

            <b-button type="submit" variant="primary">Sign Up</b-button>
          </b-form>
        </b-card>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import axios from 'axios';

export default {
  name: 'SignUp',
  data() {
    return {
      form: {
        username: '',
        email: '',
        password: '',
        confirmPassword: ''
      }
    };
  },
  methods: {
    async onSubmit() {
      if (this.form.password !== this.form.confirmPassword) {
        alert('Passwords do not match');
        return;
      }

      try {
        const response = await axios.post('http://localhost:8000/api/register/', {
          username: this.form.username,
          email: this.form.email,
          password: this.form.password
        });

        if (response.status === 201) {
          alert('User registered successfully');
          this.$router.push('/login');
        }
      } catch (error) {
        console.error('There was an error creating the user:', error);
        alert('There was an error creating your account. Please try again.');
      }
    }
  }
};
</script>

<style scoped>
/* Custom styles for the sign-up form */
.b-container {
  margin-top: 2rem;
}

.b-card {
  padding: 1.5rem;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
</style>

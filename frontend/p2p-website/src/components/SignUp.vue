<template>
  <div class="container mt-4">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="card text-center custom-card">
          <div class="card-body">
            <h3 class="card-title">Sign Up</h3>
            <form @submit.prevent="onSubmit" class="signup-form">
              <div class="form-group">
                <label for="username">Username</label>
                <input
                  type="text"
                  id="username"
                  v-model="form.username"
                  required
                  placeholder="Enter your username"
                  class="form-control"
                />
              </div>

              <div class="form-group">
                <label for="email">Email</label>
                <input
                  type="email"
                  id="email"
                  v-model="form.email"
                  required
                  placeholder="Enter your email"
                  class="form-control"
                />
              </div>

              <div class="form-group">
                <label for="password">Password</label>
                <input
                  type="password"
                  id="password"
                  v-model="form.password"
                  required
                  placeholder="Enter your password"
                  class="form-control"
                />
              </div>

              <div class="form-group">
                <label for="confirm-password">Confirm Password</label>
                <input
                  type="password"
                  id="confirm-password"
                  v-model="form.confirmPassword"
                  required
                  placeholder="Confirm your password"
                  class="form-control"
                />
              </div>

              <button type="submit" class="btn btn-primary">Sign Up</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
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
.container {
  margin-top: 2rem;
}

.custom-card {
  padding: 1.5rem;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.signup-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 1.5rem;
}

label {
  font-size: 1.1rem;
  color: #333;
  margin-bottom: 0.5rem;
  display: block;
}

.form-control {
  width: 100%;
  padding: 0.5rem;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.btn-primary {
  background-color: #343a40;
  color: #ffc107;
  padding: 0.75rem;
  font-size: 1.2rem;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 1rem;
}

.btn-primary:hover {
  background-color: #ffc107;
  color: #343a40;
}
</style>

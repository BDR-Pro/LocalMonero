<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="dark" class="custom-navbar">
      <b-navbar-brand href="#">
        <i class="fas fa-film mr-2"></i>P2P Website
      </b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-item to="/" exact>
            <i class="fas fa-users mr-2"></i>Users
          </b-nav-item>
          <b-nav-item to="/trade-offers" exact>
            <i class="fas fa-exchange-alt mr-2"></i>Trade Offers
          </b-nav-item>
          <b-nav-item to="/transactions" exact>
            <i class="fas fa-money-check-alt mr-2"></i>Transactions
          </b-nav-item>
          <b-nav-item to="/login" exact>
            <i class="fas fa-sign-in-alt mr-2"></i>Login
          </b-nav-item>
          <b-nav-item to="/sign-up" exact>
            <i class="fas fa-user-plus mr-2"></i>Sign Up
          </b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

    <b-container class="mt-4 custom-container">
      <router-view></router-view>
    </b-container>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style scoped>
/* Custom Navbar */
.custom-navbar {
  background-color: #FF4500 !important; /* Dark Orange */
  border-radius: 15px;
  padding: 0.5rem 1rem;
}

/* Navbar brand */
.b-navbar-brand {
  font-size: 1.5rem;
  font-weight: 600;
  color: #fff !important;
  font-family: 'Poppins', sans-serif;
}

/* Navbar items */
.b-nav-item {
  font-size: 1.1rem;
  margin: 0 10px;
  color: #fff !important;
  font-family: 'Poppins', sans-serif;
}

.b-nav-item:hover {
  text-decoration: underline;
  color: #FFD700 !important; /* Gold color for hover */
}

/* Container styles */
.custom-container {
  background-color: #f8f9fa;
  padding: 2rem;
  border-radius: 15px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Custom margin for top spacing */
.mt-4 {
  margin-top: 2rem !important;
}
</style>

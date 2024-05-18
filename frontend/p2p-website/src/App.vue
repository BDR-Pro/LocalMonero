<template>
  <div>
    <nav class="navbar custom-navbar">
      <a class="navbar-brand" href="#">
        <i class="fas fa-film mr-2"></i>Open-Monero Market
      </a>
      <button class="navbar-toggler" @click="toggleNavbar">
        <span class="navbar-toggler-icon">&#9776;</span>
      </button>
      <div class="navbar-collapse" :class="{ show: navbarOpen }">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <router-link to="/" class="nav-link" exact>
              <i class="fas fa-users mr-2"></i>Users
            </router-link>
          </li>
          <li class="nav-item">
            <router-link to="/trade-offers" class="nav-link" exact>
              <i class="fas fa-exchange-alt mr-2"></i>Trade Offers
            </router-link>
          </li>
          <li class="nav-item">
            <router-link to="/transactions" class="nav-link" exact>
              <i class="fas fa-money-check-alt mr-2"></i>Transactions
            </router-link>
          </li>
          <li class="nav-item">
            <router-link to="/login" class="nav-link" exact>
              <i class="fas fa-sign-in-alt mr-2"></i>Login
            </router-link>
          </li>
          <li class="nav-item">
            <router-link to="/sign-up" class="nav-link" exact>
              <i class="fas fa-user-plus mr-2"></i>Sign Up
            </router-link>
          </li>
        </ul>
      </div>
    </nav>

    <div class="container mt-4 custom-container">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      navbarOpen: false,
    };
  },
  methods: {
    toggleNavbar() {
      this.navbarOpen = !this.navbarOpen;
    },
  },
};
</script>

<style scoped>
/* Custom Navbar */
.custom-navbar {
  background-color: #343a40; /* Darker background for a modern look */
  border-radius: 15px;
  padding: 0.75rem 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.navbar-brand {
  font-size: 1.75rem;
  font-weight: 700;
  color: #ffc107; /* Gold color for brand text */
  font-family: 'Roboto', sans-serif;
}

.navbar-toggler {
  border: none;
  background: none;
  font-size: 1.5rem;
  color: #ffc107;
  cursor: pointer;
  display: none; /* Hide toggler by default */
}

.navbar-toggler-icon {
  font-size: 1.5rem;
}

.navbar-collapse {
  display: flex;
  flex-direction: row;
}

.navbar-collapse.show {
  flex-direction: column;
}

.navbar-nav {
  list-style: none;
  display: flex;
  flex-direction: row;
  padding-left: 0;
  margin: 0;
}

.nav-item {
  margin: 0 15px;
}

.nav-link {
  font-size: 1.2rem;
  color: #f8f9fa; /* Light color for links */
  font-family: 'Roboto', sans-serif;
  text-decoration: none;
}

.nav-link:hover {
  text-decoration: underline;
  color: #ffc107; /* Gold color for hover */
}

/* Container styles */
.custom-container {
  background-color: #ffffff;
  padding: 2.5rem;
  border-radius: 15px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

/* Custom margin for top spacing */
.mt-4 {
  margin-top: 2rem !important;
}

/* Responsive styling */
@media (max-width: 992px) {
  .navbar-toggler {
    display: block; /* Show toggler on smaller screens */
  }

  .navbar-collapse {
    display: none;
    flex-direction: column;
    width: 100%;
  }

  .navbar-collapse.show {
    display: flex;
  }

  .navbar-nav {
    flex-direction: column;
    width: 100%;
  }

  .nav-item {
    margin: 10px 0;
    text-align: center;
  }
}
</style>

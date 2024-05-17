<template>
  <div>
    <h2>Users</h2>
    <b-table striped hover :items="users"></b-table>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import api from '../services/api';

export default {
  setup() {
    const users = ref([]);

    const fetchUsers = async () => {
      try {
        const response = await api.getUsers();
        users.value = response.data;
      } catch (error) {
        console.error('Error fetching users:', error);
      }
    };

    onMounted(fetchUsers);

    return {
      users,
    };
  },
};
</script>

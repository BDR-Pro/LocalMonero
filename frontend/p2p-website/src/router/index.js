import { createRouter, createWebHistory } from 'vue-router';
import UserList from '../components/UserList.vue';
import TradeOfferList from '../components/TradeOfferList.vue';
import TransactionList from '../components/TransactionList.vue';
import Login from '../components/LoginUser.vue';
import SignUp from '../components/SignUp.vue';

const routes = [
  { path: '/', component: UserList },
  { path: '/trade-offers', component: TradeOfferList },
  { path: '/transactions', component: TransactionList },
  { path: '/login', component: Login },
  { path: '/sign-up', component: SignUp },
  { path: '/transaction/:id', component: Transaction, props: true },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

import { createRouter, createWebHashHistory } from 'vue-router';
const Structures = () => import('../pages/Structures.vue');
const Register = () => import('../pages/Register.vue');
const DataType = () => import('../pages/DataType.vue');
const Registration = () => import('../components/Registration.vue');
const Login = () => import('../components/Login.vue');

const routes = [
  { path: '/structures', component: Structures },
  { path: '/registers', component: Register },
  { path: '/datatypes', component: DataType },
  { path: '/registration', component: Registration },
  { path: '/login', component: Login }
];

export const router = createRouter({
  history: createWebHashHistory(),
  routes,
});
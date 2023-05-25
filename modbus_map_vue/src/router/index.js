import { createRouter, createWebHistory } from 'vue-router';
const StructureList = () => import('../pages/StructureList.vue');
const Register = () => import('../pages/Register.vue');
const DataType = () => import('../pages/DataType.vue');
const Registration = () => import('../components/Registration.vue');
const Login = () => import('../pages/Login.vue');
const StructureDetail = () => import('../pages/StructureDetail.vue');
const SubStructureList = () => import('../pages/SubStructureList.vue');
const MapList = () => import('../pages/MapList.vue');

const routes = [
  { path: '/structures', component: StructureList },
  { path: '/registers', component: Register },
  { path: '/datatypes', component: DataType },
  { path: '/registration', component: Registration },
  { path: '/login', component: Login },
  { path: '/structures/:id', name: 'structure-detail', component: StructureDetail },
  { path: '/sub_structures', component: SubStructureList },
  { path: '/maps', component: MapList },
];

export const router = createRouter({
  history: createWebHistory(),
  routes,
});
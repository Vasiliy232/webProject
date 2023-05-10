import { createApp } from 'vue';
import { BootstrapVue } from 'bootstrap-vue';
import './style.css';
import App from './App.vue';
import { router } from './router/index.js';
import { store } from './store/index.js';
import 'bootstrap-vue/dist/bootstrap-vue.css';

const app = createApp(App);

app.use(BootstrapVue);
app.use(router);
app.use(store);

app.mount('#vue');

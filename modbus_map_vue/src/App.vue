<script setup>
  import Logout from './components/Logout.vue';
  import { useStore } from 'vuex';

  const store = useStore();
</script>

<template>
  <ul class="nav nav-tabs">
    <li class="nav-item">
      <router-link to='/sub_structures' class='nav-link'>Substructures</router-link>
    </li>
    <li class="nav-item">
      <router-link to='/structures' class='nav-link'>Structures</router-link>
    </li>
    <li class="nav-item">
      <router-link to='/registers' class='nav-link'>Registers</router-link>
    </li>
    <li class="nav-item">
      <router-link to='/datatypes' class='nav-link'>Data types</router-link>
    </li>
  </ul>
  <ul class="nav nav-tabs top-right-corner" v-if='store.state.isAuthenticated'>
    <li class="nav-item">
      <Logout />
    </li>
  </ul>
  <ul class="nav nav-tabs top-right-corner" v-else>
    <li class="nav-item">
      <router-link to='/registration' class='nav-link'>Sign up</router-link>
    </li>
    <li class="nav-item">
      <router-link to='/login' class='nav-link'>Log in</router-link>
    </li>
  </ul>
  <router-view></router-view>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}

.top-right-corner {
  position: fixed;
  top: 0;
  right: 0;
}
</style>

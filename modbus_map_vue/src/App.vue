<script setup>
    import { computed } from 'vue';
    import Logout from './components/Logout.vue';

    const isAuthenticated = computed(() => {
        return localStorage.getItem('access_token') !== null;
    });
</script>

<template>
    <ul class="nav nav-tabs">
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
    <ul class="nav nav-tabs top-right-corner">
        <li class="nav-item" v-if='!isAuthenticated'>
            <router-link to='/registration' class='nav-link'>Sign up</router-link>
        </li>
        <li class="nav-item" v-if='isAuthenticated'>
            <Logout />
        </li>
        <li class="nav-item" v-else>
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

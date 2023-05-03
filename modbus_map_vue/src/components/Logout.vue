<script setup>
  import { useStore } from 'vuex';

  const store = useStore()

  const logout = async () => {
    await store.dispatch('logoutUser');
  };
</script>

<template>
    <button class='nav-link' v-on:click='logout'>Log out</button>
</template>
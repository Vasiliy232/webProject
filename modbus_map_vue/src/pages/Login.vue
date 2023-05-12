<script setup>
  import { reactive } from 'vue';
  import { useStore } from 'vuex';
  import { useRouter } from 'vue-router';

  const router = useRouter()
  const store = useStore()

  const user = reactive({
    username: '',
    password: ''
  });

  const login = async () => {
    await store.dispatch('loginUser', user);

    user.username = '';
    user.password = '';

    await router.push({
      path: '/'
    });
  };
</script>

<template>
  <div class="container">
    <form v-on:submit.prevent='login'>

      <div class="flex-row align-items-center">
        <i class="fas fa-user fa-lg me-3 fa-fw"></i>
        <div class="form-outline flex-fill mb-0">
          <input type="text" id="username" class="form-control" v-model='user.username' />
          <label class="form-label" for="username">Your Name</label>
        </div>
      </div>

      <div class="flex-row align-items-center">
        <i class="fas fa-lock fa-lg me-3 fa-fw"></i>
        <div class="form-outline flex-fill mb-0">
          <input type="password" id="password" class="form-control" v-model='user.password' />
          <label class="form-label" for="password">Password</label>
        </div>
      </div>

      <div class="justify-content-center">
        <button type="submit" class="btn btn-primary btn-lg">Login</button>
      </div>
    </form>
  </div>
</template>
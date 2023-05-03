<script setup>
  import { reactive } from 'vue';

  const user = reactive({
    username: '',
    password: '',
    password2: ''
  });

  const register = async () => {
    const resp = await fetch('http://127.0.0.1:8000/api/user/register/', {
      method: 'POST',
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        username: user.name,
        password: user.password,
        password2: user.password2
      })
    });
    user.name = '';
    user.password = '';
    user.password2 = '';
  };
</script>

<template>
  <div class="container">
    <form v-on:submit.prevent='register'>

      <div class="flex-row align-items-center">
        <i class="fas fa-user fa-lg me-3 fa-fw"></i>
        <div class="form-outline flex-fill mb-0">
          <input type="text" id="username" class="form-control" v-model='user.name' />
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

      <div class="flex-row align-items-center">
        <i class="fas fa-key fa-lg me-3 fa-fw"></i>
        <div class="form-outline flex-fill mb-0">
          <input type="password" id="password2" class="form-control" v-model='user.password2' />
          <label class="form-label" for="password2">Repeat your password</label>
        </div>
      </div>

      <div class="justify-content-center">
        <button type="submit" class="btn btn-primary btn-lg">Register</button>
      </div>
    </form>
  </div>
</template>
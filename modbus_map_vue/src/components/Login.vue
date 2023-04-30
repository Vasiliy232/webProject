<script setup>
    import { reactive } from 'vue';
    import { useRouter } from 'vue-router';

    const router = useRouter()

    const user = reactive({
        username: '',
        password: ''
    });

    const login = async () => {
        const resp = await fetch('http://127.0.0.1:8000/user/login/', {
            method: 'POST',
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(user)
        });
        const data = await resp.json();
        localStorage.setItem('access_token', data.token);

        user.username = '';
        user.password = '';

        router.push({
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
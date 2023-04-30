<script setup>
    const logout = async () => {
        const accessToken = localStorage.getItem('access_token');
        const resp = await fetch('http://127.0.0.1:8000/user/logout/', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
                Authorization: `Token ${ accessToken }`
            }
        });
        localStorage.removeItem('access_token');
    };
</script>

<template>
    <button class='nav-link' v-on:click='logout'>Log out</button>
</template>
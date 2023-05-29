import { createStore } from 'vuex';

export const store = createStore({
  state () {
    const token = localStorage.getItem('access_token');
    return {
      isAuthenticated: token !== null && token !== 'undefined'
    }
  },
  mutations: {
    setIsAuthenticated(state, value) {
      state.isAuthenticated = value;
    }
  },
  actions: {
    async loginUser ({ commit }, user) {
      const resp = await fetch('http://127.0.0.1:8000/user/login/', {
        method: 'POST',
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(user)
      });
      const data = await resp.json();
      localStorage.setItem('access_token', data.token);
      if (data.detail !== 'Invalid credentials.') {
        commit('setIsAuthenticated', true);
      }
    },
    async logoutUser ({ commit }) {
      const accessToken = localStorage.getItem('access_token');
      await fetch('http://127.0.0.1:8000/user/logout/', {
        method: 'POST',
        headers: {
          "Content-Type": "application/json",
          'Authorization': `Token ${ accessToken }`
        }
      });
      localStorage.removeItem('access_token');
      commit('setIsAuthenticated', false)
    }
  }
});
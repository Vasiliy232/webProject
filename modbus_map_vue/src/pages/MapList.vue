<script setup>
  import { onMounted, reactive, ref } from 'vue';
  import { useStore } from 'vuex';

  const store = useStore();

  const url = ref('http://127.0.0.1:8000/api/structure/');

  const mapList = reactive({
    maps: []
  });
  const substructureList = reactive({
    substructures: []
  });
  const newMap = reactive({
    name: "",
    substructures: []
  });

  onMounted(() => {
    loadMaps();
    loadSubstructures();
  });

  const loadMaps = async () => {
    const url = 'http://127.0.0.1:8000/api/map/';
    const resp = await fetch(url);
    mapList.maps = await resp.json();
  };

  const loadSubstructures = async () => {
    const resp = await fetch('http://127.0.0.1:8000/api/substructure/?no_pagination=true');
    substructureList.substructures = await resp.json();
  };

  const submitForm = async () => {
    const accessToken = localStorage.getItem('access_token');
    await fetch("http://127.0.0.1:8000/api/map/", {
      method: 'POST',
      headers: {
        "Content-Type": "application/json",
        'Authorization': `Token ${ accessToken }`
      },
      body: JSON.stringify({
        name: newMap.name,
        sub_structure: newMap.substructures
      })
    });
    newMap.name = '';
    await loadMaps();
  };

  const deleteMap = async (id) => {
    const url = 'http://127.0.0.1:8000/api/map/';
    const accessToken = localStorage.getItem('access_token');
    await fetch(url + `${ id }`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Token ${ accessToken }`
      },
    });
    await loadMaps(url);
  };
</script>

<template>
  <div>
    <div class='container'>
      <h2>Map list</h2>
      <table class="table" style='width: 60rem;'>
        <thead>
          <tr>
            <th scope="col">Map</th>
            <th scope="col">Structures</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="map in mapList.maps">
            <th scope='row'>
              <router-link :to="{ name: 'structure-detail', params: { id: map.id } }">
                {{ map.name }}
              </router-link>
            </th>
            <td>{{ map.structures_number }}</td>
            <button v-if='store.state.isAuthenticated' v-on:click.prevent='deleteMap(map.id)'>
              Delete
            </button>
          </tr>
        </tbody>
      </table>
      <div v-if='store.state.isAuthenticated'>
        <h2>Add new map</h2>
        <div class='card' style='width: 55rem;'>
          <form class="row g-3" v-on:submit.prevent='submitForm'>
            <div class="col-12">
              <label class="form-label me-3">Name</label>
              <p><input v-model="newMap.name" placeholder="Name"></p>
            </div>
            <div class="col-12">
              <label class="form-label me-3">Substructures</label>
              <select v-model="newMap.substructures" class='form-select' multiple>
                <option v-for='substructure in substructureList.substructures' :key='substructure.id' v-bind:value="substructure">
                  {{ substructure.name }}
                </option>
              </select>
            </div>
            <div class="col-12">
              <button type='submit' class='btn btn-primary'>Add</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
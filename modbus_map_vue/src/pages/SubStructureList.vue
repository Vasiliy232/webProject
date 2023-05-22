<script setup>
  import { onMounted, reactive, ref } from 'vue';
  import { useStore } from 'vuex';
  import Pagination from '../components/Pagination.vue';

  const store = useStore();

  const url = ref('http://127.0.0.1:8000/api/substructure/');
  const pagination = ref();

  const subStructureList = reactive({
    data: [],
    subStructures: []
  });
  const structureList = reactive({
    structures: []
  });
  const newSubStructure = reactive({
    name: "",
    description: "",
    structure: 'Select structure'
  });

  onMounted(() => {
    loadSubStructures();
    loadStructures();
  });

  const loadSubStructures = async (pageURL) => {
    const url = pageURL || 'http://127.0.0.1:8000/api/substructure/';
    const resp = await fetch(url);
    const subStructures = await resp.json();

    subStructureList.data = subStructures;
    subStructureList.subStructures = subStructures.results;
  };

  const loadStructures = async () => {
    const resp = await fetch('http://127.0.0.1:8000/api/structure/?no_pagination=true');
    structureList.structures = await resp.json();
  };

  const submitForm = async () => {
    const accessToken = localStorage.getItem('access_token');
    await fetch("http://127.0.0.1:8000/api/substructure/", {
      method: 'POST',
      headers: {
        "Content-Type": "application/json",
        'Authorization': `Token ${ accessToken }`
      },
      body: JSON.stringify({
        name: newSubStructure.name,
        description: newSubStructure.description,
        structure: newSubStructure.structure
      })
    });
    newSubStructure.name = '';
    newSubStructure.description = '';
    newSubStructure.structure = 'Select structure';
    await loadSubStructures();
  };

  const deleteSubStructure = async (id) => {
    const url = 'http://127.0.0.1:8000/api/substructure/';
    const accessToken = localStorage.getItem('access_token');
    await fetch(url + `${ id }`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Token ${ accessToken }`
      },
    });
    await loadSubStructures(url);
  };
</script>

<template>
  <div>
    <div class='container'>
      <h2>Substructure list</h2>
      <Pagination
        ref='pagination'
        :url='url'
        :next='subStructureList.data.next'
        :previous='subStructureList.data.previous'
        :count=subStructureList.data.count
        @page-changed='loadSubStructures'
      />
      <table class="table" style='width: 60rem;'>
        <thead>
          <tr>
            <th scope="col">Name</th>
            <th scope="col">Description</th>
            <th scope="col">Structure</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="subStructure in subStructureList.subStructures">
            <th scope='row'>{{ subStructure.name }}</th>
            <td>{{ subStructure.description }}</td>
            <td>
              <router-link :to="{ name: 'structure-detail', params: { id: subStructure.structure.id } }">
                {{ subStructure.structure.name }}
              </router-link>
            </td>
            <button v-if='store.state.isAuthenticated' v-on:click.prevent='deleteSubStructure(subStructure.id)'>
              Delete
            </button>
          </tr>
        </tbody>
      </table>
      <div v-if='store.state.isAuthenticated'>
        <h2>Add new substructure</h2>
        <div class='card' style='width: 55rem;'>
          <form class="row g-3" v-on:submit.prevent='submitForm'>
            <div class="col-12">
              <label class="form-label me-3">Name</label>
              <p><input v-model="newSubStructure.name" placeholder="Name"></p>
            </div>
            <div class="col-12">
              <label class="form-label me-3">Description</label>
              <textarea class='form-control' v-model="newSubStructure.description"></textarea>
            </div>
            <div class="col-12">
              <label class="form-label me-3">Structure</label>
              <select v-model="newSubStructure.structure" class='form-select'>
                <option selected>Select structure</option>
                <option v-for='structure in structureList.structures' :key='structure.id' v-bind:value="structure">
                  {{ structure.name }}
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
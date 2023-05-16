<script setup>
  import { onMounted, reactive, ref } from 'vue';
  import { useStore } from 'vuex';
  import Pagination from '../components/Pagination.vue';
  import EditStructure from '../components/EditStructure.vue';
  import Draggable from 'vuedraggable';

  Draggable.compatConfig = { MODE: 3 };

  const store = useStore();

  const url = ref('http://127.0.0.1:8000/api/structure/');
  const editStructure = ref();
  const pagination = ref();

  const structureList = reactive({
    data: [],
    structures: []
  });
  const registerList = reactive({
    registers: []
  });
  const newStructure = reactive({
    name: "",
    registers: []
  });
  const selectedStructure = reactive({
    structure: {}
  });

  onMounted(() => {
    loadStructures();
    loadRegisters();
  });

  const loadStructures = async (pageURL) => {
    const url = pageURL || 'http://127.0.0.1:8000/api/structure/';
    const resp = await fetch(url);
    const structures = await resp.json();

    structureList.data = structures;
    structureList.structures = structures.results;
  };

  const loadRegisters = async () => {
    const resp = await fetch('http://127.0.0.1:8000/api/register/?no_pagination=true');
    registerList.registers = await resp.json();
  };

  const submitForm = async () => {
    const accessToken = localStorage.getItem('access_token');
    await fetch("http://127.0.0.1:8000/api/structure/", {
      method: 'POST',
      headers: {
        "Content-Type": "application/json",
        'Authorization': `Token ${ accessToken }`
      },
      body: JSON.stringify({
        name: newStructure.name,
        registers: newStructure.registers
      })
    });
    newStructure.name = '';
    await loadStructures();
  };

  const deleteStructure = async (id) => {
    const url = 'http://127.0.0.1:8000/api/structure/';
    const accessToken = localStorage.getItem('access_token');
    await fetch(url + `${ id }`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Token ${ accessToken }`
      },
    });
    await loadStructures(url);
  };

  const openEditWindow = (structure) => {
    editStructure.value.props.structureData.value = { ...structure };
    editStructure.value.props.registersData.value = registerList.registers;
    editStructure.value.show();
  };

  const updateStructure = async (newStructure) => {
    const url = 'http://127.0.0.1:8000/api/structure/'
    const accessToken = localStorage.getItem('access_token');
    await fetch(url + `${ newStructure.value.id }/`, {
      method: 'PATCH',
      headers: {
        "Content-Type": "application/json",
        'Authorization': `Token ${ accessToken }`
      },
      body: JSON.stringify({
        name: newStructure.value.name,
        registers: newStructure.value.registers
      })
    });
    await loadStructures(url + '?page=' + `${ pagination.value.currentPage }`);
  };
</script>

<template>
  <div>
    <div class='container'>
      <h2>Structure list</h2>
      <Pagination
        ref='pagination'
        :url='url'
        :next='structureList.data.next'
        :previous='structureList.data.previous'
        :count=structureList.data.count
        @page-changed='loadStructures'
      />
      <table class="table" style='width: 60rem;'>
        <thead>
          <tr>
            <th scope="col">Structure</th>
            <th scope="col">Input</th>
            <th scope="col">Holding</th>
          </tr>
        </thead>
        <Draggable :list="structureList.structures" tag="tbody" item-key="id" >
          <template #item="{ element }">
            <tr class="drag-item">
              <th scope='row'>
                <router-link :to="{ name: 'structure-detail', params: { id: element.id } }">
                  {{ element.name }}
                </router-link>
              </th>
              <td>{{ element.input_registers_number }}</td>
              <td>{{ element.holding_registers_number }}</td>
              <button v-if='store.state.isAuthenticated' v-on:click.prevent='openEditWindow(element)'>
                Edit
              </button>
              <button v-if='store.state.isAuthenticated' v-on:click.prevent='deleteStructure(element.id)'>
                Delete
              </button>
            </tr>
          </template>
        </Draggable>
      </table>
      <div v-if='store.state.isAuthenticated'>
        <h2>Add new structure</h2>
        <div class='card' style='width: 55rem;'>
          <form class="row g-3" v-on:submit.prevent='submitForm'>
            <div class="col-12">
              <label class="form-label me-3">Name</label>
              <p><input v-model="newStructure.name" placeholder="Name"></p>
            </div>
            <div class="col-md-6">
              <label class="form-label me-3">Registers</label>
              <select v-model="newStructure.registers" class='form-select' multiple>
                <option v-for='register in registerList.registers' :key='register.id' v-bind:value="register.id">
                  {{ register.name }}
                </option>
              </select>
            </div>
            <div class="col-12">
              <button type='submit' class='btn btn-primary'>Add</button>
            </div>
          </form>
        </div>
        <EditStructure ref='editStructure' v-on:structure-update='updateStructure' />
      </div>
    </div>
  </div>
</template>
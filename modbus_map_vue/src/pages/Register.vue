<script setup>
  import { ref, reactive, onMounted, computed } from 'vue';
  import { useStore } from 'vuex';
  import Pagination from '../components/Pagination.vue';

  const store = useStore();
  const url = ref('http://127.0.0.1:8000/api/register/')

  const registerList = reactive({
    data: [],
    registers: []
  });

  const dataTypeList = reactive({
    data_types: []
  });

  const levelList = reactive ({
    name: ['INPUT', 'HOLDING']
  });

  const newRegister = reactive({
    name: "",
    description: "",
    level: 'Select level',
    data_type: 'Select data type'
  });

  const loadRegisters = async (pageURL) => {
    const url = pageURL || 'http://127.0.0.1:8000/api/register/'
    const resp = await fetch(url);
    const registers = await resp.json();

    registerList.data = registers;
    registerList.registers = registers.results;
  };

  const loadDataTypes = async () => {
    const resp = await fetch('http://127.0.0.1:8000/api/data_type/');
    const data_types = await resp.json();

    dataTypeList.data_types = data_types;
  };

  onMounted(() => {
    loadRegisters();
    loadDataTypes();
  });

  const submitForm = async () => {
    const accessToken = localStorage.getItem('access_token');
    const resp = await fetch("http://127.0.0.1:8000/api/register/", {
      method: 'POST',
      headers: {
        "Content-Type": "application/json",
        'Authorization': `Token ${ accessToken }`
      },
      body: JSON.stringify({
        name: newRegister.name,
        description: newRegister.description,
        level: newRegister.level,
        data_type: newRegister.data_type
      })
    });
    newRegister.name = '';
    newRegister.description = '';
    newRegister.level = 'Select level';
    newRegister.data_type = 'Select data type';
    loadRegisters();
  };

  const deleteRegister = async (id) => {
    const url = 'http://127.0.0.1:8000/api/register/';
    const accessToken = localStorage.getItem('access_token');
    await fetch(url + `${id}`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Token ${ accessToken }`
      },
    });
    loadRegisters(url);
  };
</script>

<template>
  <div>
    <div class='container'>
      <h2>Register list</h2>
      <Pagination
        :url='url'
        :next='registerList.data.next'
        :previous='registerList.data.previous'
        :count=registerList.data.count
        @page-changed='loadRegisters'
      />
      <table class="table" style='width: 60rem;'>
        <thead>
          <tr>
            <th scope="col">Register</th>
            <th scope="col">Data Type</th>
            <th scope="col">Description</th>
            <th scope="col">Level</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for='register in registerList.registers' :key='register.id'>
            <th scope='row'>{{ register.name }}</th>
            <td v-if='register.data_type === 1'>INT</td>
            <td v-else-if='register.data_type === 2'>WORD</td>
            <td v-else='register.data_type === 3'>REAL</td>
            <td>{{ register.description }}</td>
            <td v-if="register.level === 'I'">INPUT</td>
            <td v-else="register.level === 'H'">HOLDING</td>
            <button v-if='store.state.isAuthenticated' v-on:click='deleteRegister(register.id)'>Delete</button>
          </tr>
        </tbody>
      </table>
      <div v-if='store.state.isAuthenticated'>
        <h2>Add new register</h2>
        <div class='card' style='width: 55rem;'>
          <form class="row g-3" v-on:submit.prevent='submitForm'>
            <div class="col-12">
              <label class="form-label me-3">Name</label>
              <p><input v-model="newRegister.name" placeholder="Name"></p>
            </div>
            <div class="col-md-4">
              <label class="form-label me-3">Data Type</label>
              <select v-model="newRegister.data_type" class='form-select'>
                <option selected>Select data type</option>
                <option v-for='data_type in dataTypeList.data_types' :key='data_type.id' v-bind:value="data_type.id">
                  {{ data_type.name }}
                </option>
              </select>
            </div>
            <div class="col-12">
              <label class="form-label me-3">Description</label>
              <textarea class='form-control' v-model="newRegister.description"></textarea>
            </div>
            <div class="col-12">
              <label class="form-label me-3">Level</label>
              <select v-model="newRegister.level" class='form-select'>
                <option selected>Select level</option>
                <option v-for='level in levelList.name' v-bind:value="level.slice(0, 1)">
                  {{ level }}
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
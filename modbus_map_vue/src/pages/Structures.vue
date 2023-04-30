<script setup>
    import { ref, reactive, onMounted, computed } from 'vue';
    import Pagination from '../components/Pagination.vue'

    const url = ref('http://127.0.0.1:8000/api/structure/')

    const structureList = reactive({
        data: [],
        structures: []
    });

    const registerList = reactive({
        registers: []
    });

    const newStructure = reactive({
        name: "",
        input_registers_number: 0,
        holding_registers_number: 0,
        registers: []
    });

    const loadStructures = async (pageURL) => {
        const url = pageURL || 'http://127.0.0.1:8000/api/structure/';
        const resp = await fetch(url);
        const structures = await resp.json();

        structureList.data = structures;
        structureList.structures = structures.results;
    };

    const loadRegisters = async () => {
        const resp = await fetch('http://127.0.0.1:8000/api/register/');
        const registers = await resp.json();

        registerList.registers = registers.results;
    };

    created: () => loadStructures();

    onMounted(() => {
        loadStructures();
        loadRegisters();
    });

    const submitForm = async () => {
        const accessToken = localStorage.getItem('access_token');
        const resp = await fetch("http://127.0.0.1:8000/api/structure/", {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
                Authorization: `Token ${ accessToken }`
            },
            body: JSON.stringify({
                name: newStructure.name,
                input_registers_number: newStructure.input_registers_number,
                holding_registers_number: newStructure.holding_registers_number,
                registers: newStructure.registers
            })
        });
        newStructure.name = '';
        newStructure.input_registers_number = 0;
        newStructure.holding_registers_number = 0;
        loadStructures();
    };

    const deleteStructure = (id) => {
        fetch(`http://127.0.0.1:8000/api/structure/${id}`, {
            method: 'DELETE'
        });
        loadStructures();
    };

    const totalPages = computed(() => {
        return Math.ceil(structureList.data.count / 5);
    });

    const isAuthenticated = computed(() => {
        return localStorage.getItem('access_token') !== null;
    });
</script>

<template>
    <div>
        <div class='container'>
            <h2>Structure list</h2>
            <Pagination
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
                <tbody>
                    <tr v-for='structure in structureList.structures' :key='structure.id'>
                        <th scope='row'>{{ structure.name }}</th>
                        <td>{{ structure.input_registers_number }}</td>
                        <td>{{ structure.holding_registers_number }}</td>
                        <button v-if='isAuthenticated' v-on:click='deleteStructure(structure.id)'>Delete</button>
                    </tr>
                </tbody>
            </table>
            <div v-if='isAuthenticated'>
                <h2>Add new structure</h2>
                <div class='card' style='width: 55rem;'>
                    <form class="row g-3" v-on:submit.prevent='submitForm'>
                        <div class="col-12">
                            <label class="form-label me-3">Name</label>
                            <p><input v-model="newStructure.name" placeholder="Name"></p>
                        </div>
                        <div class="col-md-4">
                            <label class="form-label me-3">Input</label>
                            <p><input v-model="newStructure.input_registers_number"></p>
                        </div>
                        <div class="col-md-4">
                            <label class="form-label me-3">Holding</label>
                            <p><input v-model="newStructure.holding_registers_number"></p>
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
            </div>
        </div>
    </div>
</template>
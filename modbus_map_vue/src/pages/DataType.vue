<script setup>
    import { reactive, onMounted, computed } from 'vue';

    const dataTypeList = reactive({
        data_types: []
    });

    const newDataType = reactive({
        name: "",
        bytes: 0,
    });

    const loadDataTypes = async () => {
        const resp = await fetch('http://127.0.0.1:8000/api/data_type/');
        const data_types = await resp.json();

        dataTypeList.data_types = data_types;
    };

    onMounted(() => {
        loadDataTypes();
    });

    const submitForm = async () => {
        const resp = await fetch("http://127.0.0.1:8000/api/data_type/", {
            method: 'POST',
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                name: newDataType.name,
                bytes: newDataType.bytes,
            })
        });
        loadDataTypes();
    };

    const isAuthenticated = computed(() => {
        return localStorage.getItem('access_token') !== null;
    });
</script>

<template>
    <div>
        <div class='container'>
            <h2>Data type list</h2>
            <table class="table" style='width: 60rem;'>
                <thead>
                    <tr>
                        <th scope="col">Data type</th>
                        <th scope="col">Bytes</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for='data_type in dataTypeList.data_types' :key='data_type.id'>
                        <th scope='row'>{{ data_type.name }}</th>
                        <td>{{ data_type.bytes }}</td>
                    </tr>
                </tbody>
            </table>
            <div v-if='isAuthenticated'>
                <h2>Add new data type</h2>
                <div class='card' style='width: 55rem;'>
                    <form class="row g-3" v-on:submit.prevent='submitForm'>
                        <div class="col-12">
                            <label class="form-label me-3">Name</label>
                            <p><input v-model="newDataType.name" placeholder="Name"></p>
                        </div>
                        <div class="col-12">
                            <label class="form-label me-3">Bytes</label>
                            <p><input v-model="newDataType.bytes"></p>
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
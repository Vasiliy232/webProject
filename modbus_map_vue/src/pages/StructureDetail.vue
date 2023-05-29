<script setup>
  import Draggable from 'vuedraggable';
  import { onMounted, reactive, toRaw } from "vue";
  import { useRoute } from 'vue-router';

  Draggable.compatConfig = { MODE: 3 };

  const route = useRoute();

  const structureDetail = reactive({
    structure: {},
    registers: []
  });

  const loadStructure = async () => {
    const url =  `http://127.0.0.1:8000/api/structure/${ route.params.id }`;
    const resp_struct = await fetch(url);
    structureDetail.structure = await resp_struct.json();
    const structure = toRaw(structureDetail.structure)

    const resp_reg = await fetch('http://127.0.0.1:8000/api/register/?no_pagination=true');
    const registers = await resp_reg.json();
    for (const index in registers) {
      if (structure.registers.some(elem => elem.id === registers[index].id)) {
        structureDetail.registers.push(registers[index])
      }
    }
  };

  onMounted(() => {
    loadStructure();
  });
</script>

<template>
  <div class="container">
    <h2>{{ structureDetail.structure.name }}</h2>
    <table class="table" style='width: 60rem;'>
      <thead>
        <tr>
          <th scope="col">Register</th>
          <th scope="col">Data Type</th>
          <th scope="col">Description</th>
          <th scope="col">Level</th>
        </tr>
      </thead>
      <Draggable :list="structureDetail.registers" tag="tbody" item-key="id" >
        <template #item="{ element }">
          <tr class="drag-item">
            <th scope='row'>{{ element.name }}</th>
            <td v-if='element.data_type === 1'>INT</td>
            <td v-else-if='element.data_type === 2'>WORD</td>
            <td v-else-if='element.data_type === 3'>REAL</td>
            <td>{{ element.description }}</td>
            <td v-if="element.level === 'I'">INPUT</td>
            <td v-else-if="element.level === 'H'">HOLDING</td>
          </tr>
        </template>
      </Draggable>
    </table>
    <router-link class="btn btn-primary" to="/structures">Back to the list</router-link>
  </div>
</template>
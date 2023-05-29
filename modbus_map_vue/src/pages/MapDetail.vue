<script setup>
  import Draggable from 'vuedraggable';
  import { onMounted, reactive, toRaw } from "vue";
  import { useRoute } from 'vue-router';

  Draggable.compatConfig = { MODE: 3 };

  const route = useRoute();

  const mapDetail = reactive({
    map: {},
    substructures: []
  });

  const loadMap = async () => {
    const url =  `http://127.0.0.1:8000/api/map/${ route.params.id }`;
    const resp_map = await fetch(url);
    mapDetail.map = await resp_map.json();
    const map = toRaw(mapDetail.map)

    const resp_sub = await fetch('http://127.0.0.1:8000/api/substructure/?no_pagination=true');
    const substructures = await resp_sub.json();
    for (const index in substructures) {
      if (map.sub_structure.some(elem => elem.id === substructures[index].id)) {
        mapDetail.substructures.push(substructures[index])
      }
    }
  };

  onMounted(() => {
    loadMap();
  });
</script>

<template>
  <div class="container">
    <h2>{{ mapDetail.map.name }}</h2>
    <table class="table" style='width: 60rem;'>
      <thead>
        <tr>
          <th scope="col">Name</th>
          <th scope="col">Description</th>
          <th scope="col">Structure</th>
        </tr>
      </thead>
      <Draggable :list="mapDetail.substructures" tag="tbody" item-key="id" >
        <template #item="{ element }">
          <tr class="drag-item">
            <th scope='row'>{{ element.name }}</th>
            <td>{{ element.description }}</td>
            <td>
              <router-link :to="{ name: 'structure-detail', params: { id: element.structure.id } }">
                {{ element.structure.name }}
              </router-link>
            </td>
          </tr>
        </template>
      </Draggable>
    </table>
    <router-link class="btn btn-primary" to="/maps">Back to the list</router-link>
  </div>
</template>
<script setup>
  import { ref, reactive, watch } from 'vue';

  const props = defineProps({
    structureData: {
      type: Object,
      default: () => ({})
    }
  });

  const modalShow = ref(false);

  const emits = defineEmits(['structure-update']);

  const newStructure = reactive({
    structure: {}
  });

  const editModal = ref();

  watch(
    () => props.structureData,
    () => {
      newStructure.structure = { ...props.structureData };
    },
    { immediate: true }
  );

  const show = () => {
    modalShow.value = true;
  };
  const hide = () => {
    modalShow.value = false;
  };
  const resetForm = () => {
    newStructure.id = 0;
    newStructure.name = '';
    newStructure.registers = [];
  };
  const submitForm = async () => {
    const accessToken = localStorage.getItem('access_token');
    const resp = await fetch("http://127.0.0.1:8000/api/structure/" + `${ newStructure.id }`, {
      method: 'PATCH',
      headers: {
        "Content-Type": "application/json",
        'Authorization': `Token ${ accessToken }`
      },
      body: JSON.stringify({
        name: newStructure.name,
        registers: newStructure.registers
      })
    });
    emits('structure-update', resp.json());
    modalShow.value = false;
  };

  defineExpose({
    show
  });
</script>

<template>
  <b-modal
    v-model='modalShow'
    ref='editModal'
    title='Edit'
    v-on:ok='submitForm'
    v-on:hidden='resetForm'
  >
    {{ props.structureData }}
    <b-form v-on:submit.stop.prevent='submitForm'>
      <b-form-group label='Name'>
        <b-form-input v-model='newStructure.name'></b-form-input>
      </b-form-group>
    </b-form>
  </b-modal>
</template>
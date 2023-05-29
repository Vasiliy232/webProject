<script setup>
  import { ref, toRaw, toRefs } from 'vue';

  const props = defineProps({
    structureData: {
      type: Object,
      default: () => ({})
    },
    registersData : {
      type: Object,
      default: () => ({})
    }
  });

  const modalShow = ref(false);
  const editModal = ref();

  let newStructure = ({});

  const emits = defineEmits(['structure-update']);

  const show = () => {
    newStructure = Object.assign({}, props.structureData);
    modalShow.value = true;
  };
  const hide = () => {
    modalShow.value = false;
  };
  const resetForm = () => {
    newStructure = {};
  };
  const submitForm = () => {
    emits('structure-update', newStructure);
    modalShow.value = false;
  };

  defineExpose({
    props,
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
    <b-form v-on:submit.stop.prevent='submitForm()'>
      <b-form-group label='Name'>
        <b-form-input v-model='newStructure.value.name'></b-form-input>
      </b-form-group>
      <b-form-group v-if="newStructure.value.registers" label='Registers'>
        <b-form-select v-model="newStructure.value.registers" style='width: 29rem;' multiple>
          <b-form-select-option v-for='register in registersData.value' :key='register.id' v-bind:value="register">
            {{ register.name }}
          </b-form-select-option>
        </b-form-select>
      </b-form-group>
      <b-form-group v-else-if="newStructure.value.sub_structure" label='Substructures'>
        <b-form-select v-model="newStructure.value.sub_structure" style='width: 29rem;' multiple>
          <b-form-select-option v-for='register in registersData.value' :key='register.id' v-bind:value="register">
            {{ register.name }}
          </b-form-select-option>
        </b-form-select>
      </b-form-group>
    </b-form>
  </b-modal>
</template>
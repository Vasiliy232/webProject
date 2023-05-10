<script setup>
  import { computed } from 'vue';

  const props = defineProps({
    url: String,
    next: String,
    previous: String,
    count: {
      type: Number,
      default: 0
    }
  });

  const emits = defineEmits(['page-changed']);

  const totalPages = computed(() => {
    return Math.ceil(props.count / 5);
  });

  const currentPage = computed(() => {
    if (!props.previous) return 1;
    const pageParam = new URL(props.previous).searchParams.get("page");
    if (!pageParam) return 2;
    return parseInt(pageParam, 10) + 1;
  });

  const getPrevious = () => {
    emits('page-changed', props.previous)
  };

  const getNext = () => {
    emits('page-changed', props.next)
  };

  const gotoPage = (page) => {
    emits('page-changed', props.url + '?page=' + `${ page }`)
  };

  defineExpose({
    currentPage
  });
</script>

<template>
  <nav>
    <ul class='pagination'>
      <li class='page-item' :class='{ disabled: !props.previous }'>
        <a class='page-link' href='#' v-on:click.prevent='getPrevious'>Previous</a>
      </li>
      <li class='page-item' v-for='page in totalPages' :key='page' :class='{ active: page === currentPage }'>
        <a class='page-link' href='#' v-on:click.prevent='gotoPage(page)'>{{ page }}</a>
      </li>
      <li class='page-item' :class='{ disabled: !props.next }'>
        <a class='page-link' href='#' v-on:click.prevent='getNext'>Next</a>
      </li>
    </ul>
  </nav>
</template>
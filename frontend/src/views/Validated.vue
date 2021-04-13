<template>
  <div class="home">
    <item-list msg="Vue.js App" :validateView="false"/>
  </div>
</template>

<script>
// @ is an alias to /src
import ItemList from '@/views/ItemList.vue'

export default {
  name: 'Validated',
  components: {
    ItemList
  }
}
</script>

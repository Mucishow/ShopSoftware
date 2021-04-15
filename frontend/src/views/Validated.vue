<template>
  <div class="home">
    <h6 @click="clearList">Clear</h6>
    <h6 @click="showList">Show</h6>
    <item-list msg="Vue.js App" :validateView="false"/>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios';
import ItemList from '@/views/ItemList.vue'
export default {
  name: 'Validated',
  components: {
    ItemList
  },
  data() {
    return {
      backend_url: "http://localhost:8000/",
      image_url: "",
      itens: [],
    };
  },
  methods: {
    clearList() {
      const self = this;
      axios.get(self.backend_url+'list/clear/')
      .then((response) => {
          return response;
      });
    },
    showList() {
      const self = this;
      axios.get(self.backend_url+'list/')
      .then((response) => {
          return response;
      });
    }
  },
  created: function(){
  }
}
</script>

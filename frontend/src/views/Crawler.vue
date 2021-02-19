<template>
  <div class="home">
    <input v-model="crawlerObject"/>
    <button @click="crawler">
      Get products
    </button>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios';

export default {
  
  name: 'Home',
  components: {
  },
  data() {
    return {
      backend_url: "http://localhost:8000/",
      crawlerObject: "",
      itens: [],
    };
  },
  methods: {
    crawler() {

      var self = this;
      console.log(this.crawlerObject)
      axios.post(self.backend_url+'products/crawl/',{itens:[this.crawlerObject]})
      .then((response) => {
        console.log(response);
      });
      }
  },
}
</script>

<template>
  <div class="border">
    <img style="padding-top:5px" :src="image_url+item.picture" />
    <div>
        <span class="product-name">
            {{item.name}}
        </span>
        <div class="price">
          € {{item.price}}
          <br>
          <div class="amount">
            {{item.size}}
          </div>
        </div> 
        <div v-if="validateView">
          <div class="inline" @click="validate">
            V
          </div>
          <div class="inline" @click="deleteProduct">
            X
          </div>
        </div>
        <div v-else>
          +
        </div>
    </div>
  </div>
</template>

<script>

import axios from 'axios';

export default {
  name: 'Product',
  props: {
    image_url: String,
    item: Object,
    validateView: Boolean
  },
  data() {
    return {
      backend_url: "http://localhost:8000/"
    };
  },
  methods: {
    validate() {
      var self = this;
      axios.post(self.backend_url+'products/'+self.item.id+"/")
      .then((response) => {
        this.$emit('validated');
        return response;
      });
    },
    deleteProduct() {
      var self = this;
      axios.delete(self.backend_url+'products/'+self.item.id+"/")
      .then((response) => {
        this.$emit('delete');
        return response;
      });
    },
    addToList() {
      console.log(this.crawlerObject)
      //axios.post(self.backend_url+'products/crawl/',{itens:[this.crawlerObject]})
      //.then((response) => {
      //  console.log(response);
      //});
    },
    removeToList() {
      var self = this;
      console.log(this.crawlerObject)
      axios.post(self.backend_url+'products/crawl/',{itens:[this.crawlerObject]})
      .then((response) => {
        console.log(response);
      });
    }
  },
  created: function(){
    console.log(this.item);
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.price {
  padding: 5px;
  font-weight: 700;
  color: #1e5bc6;
}

.amount {
  font-size: 7px;
}

.product-name {
  font-weight: 600;
  padding: 2px;
}

.border {
  display: inline-block;
}
ul {
  list-style-type: none;
  padding: 0;
}
.inline {
  padding: 5px;
  display: inline-block;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>

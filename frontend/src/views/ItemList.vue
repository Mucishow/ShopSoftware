<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
      <product-component class='element' v-for="(item,index) in itens" :key="index" :ref="'item-'+index"
        :image_url="image_url"
        :item="item"
        :validateView="validateView"
        @validated="vanish(index)"
        @delete="vanish(index)" />
  </div>
</template>

<script>
import axios from 'axios';
import ProductComponent from '@/components/Product.vue';

export default {
  name: 'ItemList',
  components:{
    ProductComponent
  },
  props: {
    msg: String,
    validateView: Boolean
  },
  data() {
    return {
      backend_url: "http://localhost:8000/",
      image_url: "",
      itens: [],
    };
  },
  methods: {
    vanish(index) {
      var self = this;
      setTimeout(function(){ console.log(self.itens.splice(index,1)); }, 50);
    }
  },
  created: function(){
    var self = this;
    const command = this.validateView ? "" : "shopList/";
    axios.get(self.backend_url+'products/'+command)
    .then((response) => {
      self.image_url = self.backend_url+"img/"
      self.itens = response.data;
    });
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.element {
  display: inline-block;
  box-shadow: 0 10px 16px 0 rgba(0,0,0,0.2),0 6px 20px 0 rgba(0,0,0,0.19);
  border-radius: 5px;
  margin-left: 10px;
  margin-right: 10px;
  width: 230px;
  height: 300px;
  margin: 25px;
}

h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>

<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ItemList',
  components:{
  },
  props: {
    msg: String,
    validateView: Boolean
  },
  data() {
    return {
      backend_url: "http://localhost:8000/",
      image_url: "",
    };
  },
  methods: {
  },
  created: function(){
    var self = this;
    axios.post(self.backend_url+'list/new/')
    .then((response) => {
      console.log(response);
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

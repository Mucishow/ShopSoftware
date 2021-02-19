<template>
  <div class="border">
    <img style="padding-top:5px" :src="image_url+item.picture" />
    <div>
        <span>
            {{item.name}}
        </span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Product',
  props: {
    image_url: String,
    item: Object
  },
  data() {
    return {
    };
  },
  methods: {
  },
  created: function(){
    
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.border {
  display: inline-block;
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

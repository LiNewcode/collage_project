<template>
  <div id="v-model-radiobutton" >
    <span>{{qst}}</span>
    <el-radio class="radio" v-model="picked" label="A" size="large"  ></el-radio>

    <el-radio class="radio" v-model="picked" label="B" size="large"  ></el-radio>

    <el-radio class="radio" v-model="picked" label="C" size="large"  ></el-radio>

    <el-radio class="radio" v-model="picked" label="D" size="large"  ></el-radio>

    <el-radio class="radio" v-model="picked" label="E" size="large"  ></el-radio>

    <el-radio class="radio" v-model="picked" label="F" size="large"  ></el-radio>

    <el-radio class="radio" v-model="picked" label="G" size="large"  ></el-radio>

    <!--    <span>{{indexSelected}}</span>-->
    <br/>

    <br/>
  </div>
</template>

<script>
export default {
  name: "Question2",
  props:{
    indexSelected:String,
    qst:String,
  },
  emits: ['update:indexSelected'],
  data () {
    return {
      picked:'',
    };
  },
  methods:{
    getAns(){
      this.$emit('update:indexSelected', this.picked)
    }
  },
  watch: {
    async picked(newVal, oldVal) {
      this.getAns();
    }
  },
}
</script>

<style scoped>
#v-model-radiobutton{
  margin-bottom: 10vh;
}
.radio{
  border: white;
}
</style>
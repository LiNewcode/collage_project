<template>
<div id="test">

<!--  <el-page-header v-if="page=='1'" :icon="ArrowLeft" content="detail" style="margin-top: 2.5vh" @back="backToList()"/>-->
  <test-list v-if="page=='1'" v-model:testPageSelected="indexSelected">

  </test-list>
  <test-page v-if="page=='2'" v-model:testPageSelected="indexSelected">

  </test-page>
</div>
</template>

<script>


import TestList from "../TestList/TestList.vue";
import TestAnalysis from "../TestAnalysis/TestAnalysis.vue";
import TestPage from "../TestPage/TestPage.vue";
export default {
  name: "Test",
  components: {TestPage, TestAnalysis, TestList},

  data() {
    return {
      page:'1',
      indexSelected:'',
      activeIndex:'3',
    }
  },
  props: ['indexShow'],
  emits: ['update:indexShow'],
  watch:{
    indexSelected(newVal ,oldVal){

      if(newVal==-1){
        this.page = '1';
      }else{
        this.page = '2';
      }

    }
  },
  methods:{

    backToList(){
      this.$emit('update:indexShow', '');
    }
  }

}
</script>

<style scoped>
#test{
  overflow: hidden;
}
test-page{

}
</style>
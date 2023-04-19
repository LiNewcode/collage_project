<template>
<div id="wd-cz">
  <div class="wd-cz-box">
  <div class="wd-cz-item" v-for="item in phrase">
    <span class="wd-cz-item-en">{{item.en}}</span>
    <el-divider direction="vertical"></el-divider>
    <span>{{item.ch}}</span>
  </div>
  </div>
</div>
</template>

<script>
export default {
  name: "WDCz",
  data(){
    return{

    }
  },
  props:{
    phrase:{
      type:Array,
      default:[]
    }
    }

}
</script>

<style scoped>
#wd-cz{
  height: 20vh;
  overflow: scroll;

}
.wd-cz-box{
  width: 32vw;
  padding-left: 1.5vw;
  display: flex;
  flex-direction: column;
  height: 20vh;
  margin-top: 0vh;
  overflow: scroll;
  justify-content: center;
  padding-top: 0vh;
}
.wd-cz-item{
  min-height: 3vh;
  padding: 1vh;
  /*overflow: scroll;*/
  /*width: auto;*/
  /*justify-content: center;*/
  text-align: center;
}
.wd-cz-item-en{
  font-family: "Times New Roman";
  font-size: 1.15vw;

}
</style>
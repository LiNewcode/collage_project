<template>
<div id="user-info">
  你今天真好看
  <el-divider></el-divider>
</div>
</template>

<script>
export default {
  name: "Info"
}
</script>

<style scoped>
#user-info{
  width: 30vw;
  height: 10vh;
  top: 35vh;
  left: 35vw;
  font-family: 'FangSong_GB2312';
  /*margin-left: 50vw;*/
  text-shadow: 1px 1px 2vh #dcdcdc;
  text-align: center;
  line-height: 10vh;
  font-size: 3vw;
  position: relative;

}
#user-info:hover{
  font-size: 3.1vw;
}
</style>
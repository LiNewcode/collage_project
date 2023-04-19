<template>
  <el-card class="box-card bcard">
<p>{{testContent}}</p>
  </el-card>
</template>

<script>
export default {
  name: "questionContent",
  props:['testContent']
}
</script>

<style scoped>
el-card{
  margin-left: 1vh;
  margin-right: 1vh;
}
p{
  font-family: "Times New Roman";
  font-weight: 550;
  margin-left: 0.5vh;
  text-indent: 2vw;
  margin-right: 0.3vh;
  font-size: 1.35vw;
  line-height: 2.1vw;
  padding: 0 0;
}
.bcard{
  border: None;
  padding: 0 0;
}
</style>
<template>
  <div id="fdb">我是反馈页面
    <el-steps :space="200" :active="1" finish-status="success">
    <el-step title="Done"></el-step>
    <el-step title="Processing"></el-step>
    <el-step title="Step 3"></el-step>
  </el-steps></div>
</template>

<script>
export default {
  name: "FDB"
}
</script>

<style scoped>
#fdb{
  width: 90vw;
  height: 88vh;
  margin-top: 8vh;
}
</style>
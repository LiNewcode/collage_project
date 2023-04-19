<template>
  <div id="wd-js">
    <div v-for="item in explain" style="display: flex;flex-direction: row;padding: 1vh;height: auto">
      <div v-for="i in item" style="height: 100%">
        <span v-if="i!=='|'" >{{ i }}</span>
        <el-divider v-if="i=='|'" direction="vertical"></el-divider>
      </div>
    </div>
<!--    <p>{{explain}}</p>-->
  </div>
</template>

<script>
export default {
  name: "WDJs",
  data() {
    return {
      explains:Array
    }
  },
  props: {
    explain: []
  },
  created() {

    // this.explains = this.explain;
    // console.log(this.explains)
    // for (let i = 0; i < this.explain.length; i++) {
    //
    //
    //   let exp = this.explain[i];
    //   exp = exp.split(';')
    //   let tmp = []
    //   for (let j = 0; j < exp.length; j++) {
    //     tmp.push(exp[j])
    //     if (j + 1 < exp.length) {
    //       tmp.push('|')
    //     }
    //   }
    //   this.explains[i] = tmp
    // }
  }
}
</script>

<style scoped lang="less">
#wd-js {
  width: 35vw;
  height: 20vh;
  overflow: scroll;
  display: flex;
  flex-direction: column;
  font-size: 0.95vw;
  color: #535252;
  padding-left: 0.1vh;
  span:hover{

    cursor: default;
    font-size: 1vw;
    color: #2c6afc;
    text-shadow: 1px 1px 2vh rgb(72, 158, 224);
  }

}

.el-carousel__item h3 {
  color: #475669;
  /*font-size: 18px;*/
  opacity: 0.75;
  line-height: 20vh;
  margin: 0;
  text-align: center;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}

.el-carousel__container {
  /*height: 456px;*/
  height: 100% !important;
}
</style>
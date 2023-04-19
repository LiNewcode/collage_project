<template>
  <div class="Hom">
    <div class="fix">{{ ft }}{{ fc }}</div>
    <div v-for="item in col" style="display: flex;flex-direction: column;margin-left: 20px">
      <div style="max-width: 70%;height:auto;padding:0vh 0.25vw"><p style="margin-top: 2.2vh;margin-bottom: 0.5vh">{{ item.nature }}</p></div>
      <div class="example" v-for="example in item.example"
           style="">
        <span class="item en">{{ example.en }}</span><span class="item ch">{{ example.ch }}</span></div>
    </div>

  </div>

</template>

<script>
export default {
  name: "itemHom",
  data() {
    return {
    }
  },
  props:['Homonym','ft','fc','col']
}
</script>

<style scoped lang="less">
.Hom{
  position: relative;
}
.fix{
  margin-top: 2vh;
  margin-left: 20px;

}
.title{
  position: absolute;
  top:1.2vh;
  right: 1.2vw;
  background-color: #efeeee;
  border-radius: 0.3vw;
  padding: 0 0.3vw;
}
.example{
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  width:auto;
  padding-bottom: 1vh;
}
.item{
  width: auto;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  height:30*0.115vh;
  padding: 0 6*0.115vw;
  margin-right: 1*0.115vw;
  line-height: 30*0.115vh;
  font-size: 14*0.115vh;
  align-content: center;
}
.en{
  border-radius: 5*0.115vw;
  border: #efefef 1*0.115vw solid;
  box-shadow: 0 0 8*0.117vw #f8f8f8;
  font-weight: bold;
}
.ch{
  background-color: rgba(251,251,251,0.5);

}
</style>
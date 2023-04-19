<template>
  <div class="Box">
    <table border="0">
      <tr class="eachBox" v-for="item in phrase" style="">
        <th class="item en"><p>{{ item.en }}</p></th>
        <th class="item ch"><p>{{ item.ch }}</p></th>
      </tr>
    </table>
<!--  <ul style="">-->
<!--    <li class="eachBox" v-for="item in phrase" style="">-->
<!--      <span class="item en" >{{ item.en }}</span>-->
<!--      <span class="item ch" >{{ item.ch }}</span>-->
<!--    </li>-->
<!--  </ul>-->
  </div>
</template>

<script>
export default {
  name: "itemPhr",
  data() {
    return {
    }
  },
  props:['phrase']
}
</script>

<style scoped lang="less">
.title{
  position: absolute;
  top:1.2vh;
  right: 1.2vw;
  background-color: #efeeee;
  border-radius: 0.3vw;
  padding: 0 0.3vw;
}
.Box{
  position: relative;
}
.eachBox{
  display: flex;
  flex-direction: row;
  margin-left: 12*0.115vw;
    padding: 4*0.115vw 0*0.115vw;

}
ul{
  padding: 0;
  height: auto;
  overflow: hidden;
  margin-top: 1vh;
  width: auto;
}
.item{

  height: auto;
  max-height: 84*0.115vh;
  padding: 0 6*0.115vw;
  margin-right: 0.2*0.115vw;


  align-content: center;
  p{
    width: auto;
    height: auto;
    line-height: 20*0.115vh;
    font-size: 15*0.115vh;
    //height:22*0.115vh;
  }
 }

.en{
  width: 35%;
  height: auto;
  border-radius: 5*0.115vw;
  border: #efefef 1*0.115vw solid;
  box-shadow: 0 0 8*0.115vw #f8f8f8;
  font-weight: bold;

}
.ch{
  width: 65%;
  height: auto;
  background-color: #fbfbfb;
  margin-left: 2vw;
}
</style>
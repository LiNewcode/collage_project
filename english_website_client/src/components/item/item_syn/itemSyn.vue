<template>
  <div class="syn">

    <ul>
    <li class="synBox" v-for="item in Syn" style="">
        <span class="item en" v-for="word in item.word" style="">{{ word }}</span>
      <span class="item ch" style="">{{ item.description }}</span>

    </li>
    </ul>

  </div>

</template>

<script>
export default {
  name: "itemSyn",
  data() {
    return {
      // Syn: [{description: 'description', word: ['w1', 'w2']}]
    }
  },
  props:['Syn']
}
</script>

<style scoped lang="less">
.syn{
  position: relative;
}
.title{
  position: absolute;
  top:1.2vh;
  right: 1.2vw;
  background-color: #efeeee;
  border-radius: 0.3vw;
  padding: 0 0.3vw;
}
ul{
  padding: 0;
  height: auto;
  overflow: hidden;
  margin-top: 1vh;
  width: auto;
}
.synBox{
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  margin-left: 12*0.115vw;
  padding: 4*0.115vw 0*0.115vw;
}
.item{
  width: auto;
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
  padding-top: 0.2vh;
  background-color: rgba(251,251,251,0.5);
  padding-bottom: 0.6vh;
}
</style>
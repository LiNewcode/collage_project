<template>
<div id="wd-real-box">
<div id="wd-rb-head"></div>
  <div id="wd-rb-body">
    <span id="wd-rb-w">{{word}}</span>
     <div class="wd-rb-phs"><span class="wd-rb-phs-p">{{phs_1.slice(1,-1)}}</span><span class="wd-rb-phs-t">听</span></div>

    <div class="wd-rb-phs"><span class="wd-rb-phs-t">听</span><span class="wd-rb-phs-p">{{phs_2.slice(1,-1)}}</span></div>
  </div>
</div>
</template>

<script>
export default {
  name: "WDRealBox",
  props:{
    word:String,
    phs_1:String,
    phs_2:String,
    mp3_usa:String,
    mp3_bt:String
  },
}
</script>

<style scoped lang="less">
#wd-real-box{
  width: 13vw;
  display: flex;
  flex-direction: column;
  margin-top: 2vh;
  height: 16vh;
  border-radius: 3px;
  overflow: hidden;
  color: white;
  font-weight: bold;
}
#wd-rb-head{
  width: 13vw;
  height: 1vh;
  background-color: rgba(2, 119, 245, 0.7);
}
#wd-rb-body{
  width: 13vw;
  height: 16vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  background-color: rgba(2, 119, 245, 0.2);
  overflow: hidden;
}
#wd-rb-w{
  width: 13vw;
  text-align: center;
  font-size: 2.5vw;
  font-family: "Indie Flower";
}
.wd-rb-phs {
  display: flex;
  flex-direction: row;
  width: 13vw;
  //background-color: #b4c8ea;
  justify-content: center;
  text-align: center;
  .wd-rb-phs-p{
    font-size: 1.3vw;
  }
.wd-rb-phs-t{
  width: 1.2vw;
  height: 1.2vw;
  margin-left: 0.5vw;
  margin-right: 0.5vw;
  margin-top: 0.5vh;
  background-color: #4f93e5;
  color: white;
  font-weight: normal;
  text-align: center;
  line-height: 1.2vw;
}

}
</style>
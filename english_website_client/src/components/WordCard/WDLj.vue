<template>
  <div id="wd-lj" @mouseover="showPoint=true" @mouseleave="showPoint=false">
    <div class="wd-lj-main-box">
      <img :class="showPoint?'showP':'notP'" src="/last.png"  @click="change('last')" style="margin-left: 0.85vw;margin-right: 0.2vw"/>
      <div class="wd-lj-box">
        <p> {{ now_sentence.en }}</p>
        <div> {{ now_sentence.ch }}</div>
      </div>
      <img :class="showPoint?'showP':'notP'"  src="/next.png" @click="change('next')" style=""/>
    </div>
  </div>
</template>

<script>
export default {
  name: "WDLj",
  data() {
    return {
      now_sentence: {
        'en': '',
        'ch': ''
      },
      now_index: 0,
      showPoint:false

    }
  },
  props: {
    sentence: {
      type: Array,
      default: [{}]
    }
  },
  created() {

  },
  watch: {
    async sentence(newVal, oldVal) {
      this.now_sentence = this.sentence[0];
      this.now_index = 0
    }
  },
  methods:{
    change(direction){
      if(direction=='next'){
        if(this.now_index<this.sentence.length-1){
          this.now_index++;
        }
        else {
          this.now_index = 0;
        }
      }else if(direction=='last'){
        if(this.now_index>0){
          this.now_index--;
        }else{
          this.now_index=this.sentence.length-1;
        }
      }
      console.log(this.now_index,this.sentence.length)
      console.log(this.sentence)
      this.now_sentence=this.sentence[this.now_index]

    }
  }

}
</script>

<style scoped lang="less">
#wd-lj {



}

.wd-lj-main-box {
  width: 35vw;
  height: 20vh;
  display: flex;
  flex-direction: row;
  overflow: scroll !important;
  img {
    width: 1.6vw;
    height: 1.6vw;
    //position: relative;
    background-color: #f3f3f3;
    border-radius: 50%;
    margin-top: 8vh;
    transition-duration: 0.9s;
  }
  img:hover{
    transition-duration: 0.2s;
    background-color: #ffffff;
    box-shadow: 1px 1px 4vh rgba(205, 203, 203, 0.8);
  }
}

.wd-lj-box {
  width: 30vw;
  display: flex;
  flex-direction: column;
  justify-content: center;

  p {
    text-align: center;
    color: #323131;
    font-size: 1.3vw;
    text-shadow: 1px 1.2px 1vh white;
    font-family: "Times New Roman";
  }

  div {
    text-align: center;
    color: #717070;
  }

}
.showP{

}
.notP{
  opacity: 0.1;
}
</style>
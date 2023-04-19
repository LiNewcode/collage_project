<template>
<div id="wc-box" style="">
<span id="wc-word">{{word}}</span>
  &nbsp;&nbsp;<el-divider direction="vertical"></el-divider>
  <span id="wc-phs-des">英：</span><span id="wc-phs">{{phs}}</span>
  <el-divider>
    <div id="wc-des">解释</div>
  </el-divider>
  <div id="wc-exp">
    <span v-for="exp in explain">{{exp}}</span>
  </div>

</div>
</template>

<script>
export default {
name: "WC",
  data(){
  return{
    explain_first:'',
    explain: '',
    Homonym: '',
    mp3_usa: '',
    mp3_bt: '',
    ft: '',
    fc: '',
    hom_col: '',
    phrase: '',
    phs: '',
    sentence: '',
    simWor: [],
    wordDiscrimination: '',
    explain_exist: 0,
    phsUsa_exist: 0,
    phsBt_exist: 0,
    phrase_exist: 0,
    sentence_exist: 0,
    simWor_exist: 0,
    Homonym_exist: 0,
    wordDiscrimination_exist: 0,
    isPee: 0,
    phr_view: true,
    syn_view: true,
    hom_view: true,
    sen_view: true,
    item_view: 'fold',
    cv: false,
    ov: false,
    checked_box: 'phr',
    index: 0,
    mp3_src:null
  }
  },
  props:{
  word:String
  },
  created(){
    this.getDetail()
  },
  watch:{
  async word(newVal,oldVal){
    this.getDetail()
  }
  },
  methods:{
    async getDetail(){
      const res = await this.$http.get('/Reader/getWord', {
        params: {
          word: this.word,
          userId: localStorage.getItem('userId'),
        }
      })


      this.explain = res.data.explain
      this.mp3_bt = res.data.mp3_bt
      this.mp3_usa = res.data.mp3_usa
      this.phrase = res.data.phrase.phrase
      this.Homonym = res.data.Homonym

      this.hom_col = res.data.Homonym.col
      this.phs = res.data.phs
      this.phs = this.phs[0].slice(1,-1)
      this.sentence = res.data.sentence
      this.simWor = res.data.simWor
      this.wordDiscrimination = res.data.wordDiscrimination
      this.explain_exist = res.data.explain_exist
      this.phsUsa_exist = res.data.phsUsa_exist
      this.phsBt_exist = res.data.phsBt_exist
      this.phrase_exist = res.data.phrase_exist
      this.sentence_exist = res.data.sentence_exist
      this.simWor_exist = res.data.simWor_exist
      this.Homonym_exist = res.data.Homonym_exist
      this.wordDiscrimination_exist = res.data.wordDiscrimination_exist
      this.isPee = res.data.isPee
      this.ft = res.data.Homonym.fix.ft
      this.fc = res.data.Homonym.fix.fc
    }
  }
}
</script>

<style scoped lang="less">
#wc-box{
  padding-top: 1vh;
  transition-duration: .3s;
  box-shadow:1px 1px 15px #f1f1f1;
  background-color: #fefefe;
  cursor: pointer;
  font-size: 0.95vw;
  width: 14vw;
  height: 22vh;
  margin: 1vh 0.5vw 1vh 1vw;
  overflow: hidden;
}
#wc-word{
  margin-left: .65vw;
  //margin-top: 10vh;
  font-family: "Times New Roman";
  font-size: 1.25vw;
  font-weight: 600;
}
#wc-phs-des{
  color: #959595;
  font-size: 0.8vw;
}
#wc-phs{
  font-size: 0.88vw;
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
}
#wc-exp{
  margin-top: 1.6vh;
  width: 12.8vw;
  margin-left: 0.6vw;
  height: 14.5vh;
  overflow: scroll;
  display: flex;
  flex-direction: column;
  font-family: "Indie Flower";
span{
  margin-bottom: 1.3vh;

}
}
#wc-des{
  font-size: 0.9vw;
}
#wc-box:hover{
  box-shadow:2px 2px 15px #e7e8ea;
  background-color: #ffffff;
}
</style>
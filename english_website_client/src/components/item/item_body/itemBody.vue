<template>

  <div class="hr" v-show='item_view==="unfold"' @mouseover='ov=true' @mouseleave="ov=false">
<!--    <img alt="" class="icon icon_unfold" src="/open.png" v-show="ov" @click='item_view="fold"'>-->
    <div class="icon icon_unfold "  v-show="ov" @click='item_view="fold"'><div class="icon-line"></div></div>
    <item-tit ref="tit" id="tit" v-model:mp3_src="mp3_src" :isPee="isPee" :word="word" :explain="explain" :phs="phs" :mp3_usa="mp3_usa" :mp3_bt="mp3_bt" :wordSignal="wordSignal" :filename="filename"></item-tit>
    <div class="choice_box">
      <div v-show="true" @click='checked_box="phr"' class="choice_signal">
        <p>词组</p>
        <div v-show='checked_box==="phr"' class="signal"></div>
      </div>
      <div v-show="true" @click='checked_box="syn"' class="choice_signal"><p>近义词</p>
        <div v-show='checked_box==="syn"' class="signal"></div>
      </div>
      <div v-show="true" @click='checked_box="hom"' class="choice_signal"><p>同根词</p>
        <div v-show='checked_box==="hom"' class="signal"></div>
      </div>
      <div v-show="true" @click='checked_box="sen"' class="choice_signal"><p>例句</p>
        <div v-show='checked_box==="sen"' class="signal"></div>
      </div>
    </div>
    <div class="hr_body">
      <item-phr v-if="phrase_exist==1" v-show='checked_box==="phr"' id="phr" class="box" :class='phr_view?"unfold":"fold"' :phrase="phrase"
      ></item-phr>
      <item-syn v-if="simWor_exist==1" v-show='checked_box==="syn"' class="box" :class='syn_view?"unfold":"fold"' :Syn="simWor"
      ></item-syn>
      <item-hom v-if="Homonym_exist==1" v-show='checked_box==="hom"' class="box" :class='hom_view?"unfold":"fold"' :Homonym="Homonym" :ft="ft"
                :fc="fc" :col="hom_col"
      ></item-hom>
      <item-sen v-if="sentence_exist==1" v-show='checked_box==="sen"' class="box" :class='sen_view?"unfold":"fold"' :sentence="sentence"
      ></item-sen>
    </div>
  </div>
  <div class="hr_fake" v-show='item_view==="fold"' @mouseover='cv=true' @mouseleave="cv=false"
       @click='item_view="unfold"'>
    <!--    <img alt="" class="icon icon_fold" src="/close.png" v-show="cv">-->
    <span>{{ word }}</span>
    <audio id="aua" controls="controls" autoplay="autoplay" :src="mp3_src" hidden></audio>
  </div>
</template>

<script>
import ItemTit from "../item_title/itemTit.vue";
import ItemPhr from "../item_phr/itemPhr.vue";
import ItemSyn from "../item_syn/itemSyn.vue";
import ItemHom from "../item_hom/itemHom.vue";
import ItemSen from "../item_sen/itemSen.vue";

export default {
  name: "itemBody",
  data() {
    return {
      word: '',
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
      mp3_src:null,

    }
  },
  components: {ItemSen, ItemHom, ItemSyn, ItemPhr, ItemTit},
  props: ['id', 'stateItem', 'nowWord','wordSignal','filename'],
  created() {
    this.item_view = "unfold"
    this.getInfo(this.id)

    // this.getInfo('chap')
  },
  watch:{
    async mp3_src(newVal,oldVal){

      document.getElementById('aua').play();
    }
  },
  methods: {
    async getInfo(s) {
      const res = await this.$http.get('/Reader/getWord', {
        params: {
          word: s,
          userId: localStorage.getItem('userId'),
        }
      })

      this.word = s
      this.explain = res.data.explain
      this.mp3_bt = res.data.mp3_bt
      this.mp3_usa = res.data.mp3_usa
      this.phrase = res.data.phrase.phrase
      this.Homonym = res.data.Homonym

      this.hom_col = res.data.Homonym.col
      this.phs = res.data.phs
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

      if(this.fc!=null&&this.fc!=''){
        this.fc=this.fc[0]
      }


    },
    playAudio(){
      this.mp3_src=this.mp3_bt
    },
    changeNext() {
      this.index++;
      if (this.index == 4) {
        this.index = 0;
      }
      if (this.index === 0) {
        this.checked_box = 'phr';
      } else if (this.index === 1) {
        this.checked_box = 'syn';
      } else if (this.index === 2) {
        this.checked_box = 'hom';
      } else if (this.index === 3) {
        this.checked_box = 'sen';
      }

    },
    changeDesView(){
      this.$refs.tit.changeDesView();
    },
  }

}
</script>

<style scoped lang="less">
#tit {
  height: auto;
  width: 100%;
  margin-right: 0;
  padding-bottom: 2vh;
}

.choice_box {
  width: 100%;
  height: 3vh;
  border-top: #f1f1f1 1px solid;
  padding-top: 1vh;
  overflow: hidden;
  display: flex;
  flex-direction: row;
  position: relative;

  .choice_signal {

    padding-left: 1.6vw;
    padding-right: 1.2vw;
    width: 20%;
    height: 100%;
    //background-color: #b4c8ea;

    position: relative;

    p {
      font-size: 2vh;
      line-height: 3vh;
      max-height: 3vh;
      text-align: center;
      margin: 0;
      z-index: 2 !important;
    }

    p:hover {
      cursor: pointer;
    }

    .signal {
      border-radius: 1vh;
      position: absolute;
      bottom: 0.4vh;
      left: 0.9vw;
      content: '';
      width: 80%;
      height: 1vh;
      z-index: 0;
      background-color: rgba(2, 119, 245, 0.7);
    }

    .signal:hover {
      cursor: pointer;
    }
  }
}

.hr_body {
  width: 100%;
  height: auto;
}

#phr {
  padding-top: 0*0.115vw;
}

.hr {
  border-radius: 0.115*8vw;
  box-shadow: 0 0 0.115*12vw #F4F4F4;
  position: relative;
  background-color: white;
  margin-top: 5vh;
  margin-bottom: 5vh;
}

.hr_fold {
  height: 13.8vh;
  overflow: hidden;
}

.hr.unfold {

}

.box {
  width: 100%;
  margin-top: 1%;
  border-top: 1*0.115vw seashell solid;
  overflow: hidden;
}


.hr_fake {
  display: flex;
  flex-direction: row;
  position: relative;
  width: 100%;
  background-color: white;
  height: 5vh;
  border-radius: 1.2vw;
  border: #f6f6f6 solid;
  padding: 1vh 0;
  margin-bottom: 1vw;
  cursor: pointer;

  span {
    position: relative;
    margin-left: 11%;
    height: 3vw;
    line-height: 3vw;
    font-size: 1.5vw;

    top: 2.5vh;
    margin-top: -1.6vw;
    cursor: pointer;
  }
}

.hr_fake:hover {
  background-color: #2c6afc;
  color: white;
  font-family: "Times New Roman";
  font-weight: bold;
}

.icon {
  position: absolute;
  cursor: pointer;
  max-width: 1.5vw;
  max-height: 1.5vw;
}

.icon_unfold {
  top: 3.2vh;
  left: 1.2%;
  width: 1.2vw;
  height: 1.2vw;
  background-color: #2c6afc;
  display: flex;
  flex-direction: column;
  justify-content: center;
  border-radius: 0.2vw;
}
.icon-line{
  width: 0.6vw;
  height: 0.2vw;
  margin-left: 0.3vw;
  background-color: white;
  border-radius: 0.07vw;
}
.fold {
  height: 6vh;
  overflow: hidden;
}

.icon_fold {
  top: 50%;
  margin-top: -0.75vw;
  left: 2%;

}

.unfold {
  height: auto;
}
</style>
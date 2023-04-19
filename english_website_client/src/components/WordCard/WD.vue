<template>
  <div id="wd-box">
    <w-dmenu v-model:selected_menu="selected_menu"></w-dmenu>
    <el-divider direction="vertical" style="height: 16vh;margin-top: 2vh"></el-divider>
    <!--{{word}}-->
    <div id="wd-word-box">
      <p id="wd-word">{{ word }}</p>
      <div class="wd-word-yb" style="" @click="mp3_src=mp3_bt;playAudio()">美&nbsp;{{ phs[1] }}</div>
    </div>
    <div class="yb" writing-mode="tb-rl"><img src="/taiyang.png" class="yb-img" @click="mp3_src=mp3_usa;playAudio()"/>英&nbsp;{{
        phs[0]
      }}
    </div>
    <div id="wd-choice-box">
      <div
          :class="state=='zh'?'al-zhaohua':'no-zhaohua'"
          @click="changeState('addZH')"
          v-if="(state=='jx'||state=='no'||state=='zh')&&(selectedMenu!='zh')&&(selectedMenu!='xs')"
          style="margin-bottom: 3vh; width:3.4vw;font-size: 0.98vw;padding: 0.2vh 0vh;border-radius: 0.5vh;margin-left: 1.2vw;">
        朝花
      </div>
      <div
          :class="state=='xs'?'al-xishi':'no-xishi'"
          @click="changeState('addXS')"
          v-if="(state=='zh'&&selectedMenu=='zh')"
          style="margin-bottom: 3vh; width:3.4vw;font-size: 0.98vw;padding: 0.2vh 0vh;border-radius: 0.5vh;margin-left: 1.2vw;">
        夕拾
      </div>
      <div
          :class="state=='xs'?'al-xishi':'no-xishi'"
          v-if="(state=='xs'&&selectedMenu!=='zh'&&selectedMenu!=='xs')"
          style="margin-bottom: 3vh; width:3.4vw;font-size: 0.98vw;padding: 0.2vh 0vh;border-radius: 0.5vh;margin-left: 1.2vw;">
        夕拾
      </div>
      <div
          :class="state=='xs'?'al-xishi':'no-xishi'"
          @click="changeState('addJX')"
          v-if="state=='xs'&&selectedMenu=='xs'"
          style="margin-bottom: 3vh; width:3.4vw;font-size: 0.98vw;padding: 0.2vh 0vh;border-radius: 0.5vh;margin-left: 1.2vw;">
        过
      </div>
      <div style="background-color: #e6f5dc;padding: 0.4vh 1.5vh;padding-bottom: 0.8vh;">
        <div style="font-size: 0.95vw">已背次数: <span
            style=" width: 1vw;padding: 1px;background-color:  #d3f1d8;color: #5cbd37">{{ num }}</span></div>
        <div class="zjzw" style="font-size: 0.88vw;cursor: pointer;" @click="delete_word()">直接掌握</div>
      </div>

    </div>
    <w-d-js :explain="this.explains" class="wd-main-box"
            :class="selected_menu=='js'?'wd-main-box-show':'wd-main-box-none'"></w-d-js>
    <w-d-cz :phrase="this.phrase" class="wd-main-box"
            :class="selected_menu=='cz'?'wd-main-box-show':'wd-main-box-none'"></w-d-cz>
    <w-d-lj :sentence="this.sentence" class="wd-main-box"
            :class="selected_menu=='lj'?'wd-main-box-show':'wd-main-box-none'"></w-d-lj>
    <audio id="audio" :src="mp3_src" autoplay/>
  </div>
</template>

<script>
import WDmenu from "./WDMenu.vue";
import WDRealBox from "./WDRealBox.vue";
import WDJs from "./WDJs.vue";
import WDCz from "./WDCz.vue";
import WDLj from "./WDLj.vue";

export default {
  name: "WD",
  components: {WDLj, WDCz, WDJs, WDRealBox, WDmenu},
  data() {
    return {
      selected_menu: 'js',
      explain_first: '',
      explain: [],
      Homonym: '',
      mp3_usa: '',
      mp3_bt: '',
      ft: '',
      fc: '',
      hom_col: '',
      phrase: [],
      phs: '',
      sentence: [],
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
      mp3_src: null,
      explains: [],
      showMe: '',
      zhaohua: false,
      state: '',
      num: '',

    }
  },
  props: {
    word: String,
    selectedMenu: String,

  },
  created() {
    this.getDetail();
    this.getState();
  },
  watch: {
    async word(newVal, oldVal) {
      await this.getDetail();
      this.zhaohua = false;
      await this.getState();
    },
    async state(newVal, oldVal) {

      const res1 = await this.$http.get('/User/Accumulate', {
        params: {
          word: this.word,
          choice: 'getNum',
          userId: localStorage.getItem('userId'),
        }
      })
      this.num = res1.data.data

    }
  },
  methods: {
    async getState() {
      const res = await this.$http.get('/User/Accumulate', {
        params: {
          word: this.word,
          choice: 'getState',
          userId: localStorage.getItem('userId'),
        }
      })
      if (res.data.state == 'true') {
        this.state = res.data.data;
      }
      if (this.state != 'no') {
        const res1 = await this.$http.get('/User/Accumulate', {
          params: {
            word: this.word,
            choice: 'getNum',
            userId: localStorage.getItem('userId'),
          }
        })
        this.num = res1.data.data
      } else {
        this.num = 0
      }
    },
    async getDetail() {
      const res = await this.$http.get('/Reader/getWord', {
        params: {
          word: this.word,
          userId: localStorage.getItem('userId'),
        }
      })


      this.explain = res.data.explain
      this.explains = this.explain;
      this.mp3_bt = res.data.mp3_bt
      this.mp3_usa = res.data.mp3_usa
      this.phrase = res.data.phrase.phrase
      this.Homonym = res.data.Homonym

      this.hom_col = res.data.Homonym.col
      this.phs = res.data.phs
      // this.phs = this.phs[0].slice(1,-2)
      this.sentence = res.data.sentence.example
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
      if (this.fc != null && this.fc != '') {
        this.fc = this.fc[0]
      }
      this.separateJs();

    },
    async changeState(state) {

      if (this.state == state) {

      } else {
        const res = await this.$http.get('/User/Accumulate', {
          params: {
            word: this.word,
            choice: state,
            userId: localStorage.getItem('userId'),
          }
        })

        this.state = res.data.data
        if (state == 'addZW' || state == 'addXS' || state == 'addJX') {
          this.$emit('fatherMethod2');
        }

      }
    },
    separateJs() {
      this.explains = this.explain;

      for (let i = 0; i < this.explain.length; i++) {


        let exp = this.explain[i];
        exp = exp.split('；')
        let tmp = []
        for (let j = 0; j < exp.length; j++) {
          tmp.push(exp[j])
          if (j + 1 < exp.length) {
            tmp.push('|')
          }
        }
        this.explains[i] = tmp
      }

    },
    playAudio() {
      document.getElementById("audio").play();
    },
    delete_word() {

      this.changeState('addZW');
      if (this.state == 'zw') {
        this.$emit('fatherMethod');
      }

    }
  }

}
</script>

<style scoped lang="less">
#wd-box {
  width: 76vw;
  height: 20vh;
  margin-left: 1vw;
  margin-top: 2vh;
  display: flex;
  flex-direction: row;
  border: 1px solid #efeeee;
  box-shadow: 2px 2px 15px #f3f4f6;
  overflow: hidden;
  position: relative;
}

#wd-word {
  font-size: 4vw;
  font-family: "Times New Roman";
  margin-top: 2.8vh;
  margin-left: 1vw;
  width: auto;
  text-align: center;
}

.wd-main-box {
  width: 35vw;
  height: 20vh;
  background-color: #fdfdfd;
  position: absolute;
  transition-duration: .9s;
  bottom: 0;

}

.yb {
  //width: 2vh;
  //height: 15vh;
  font-size: 0.8vw;
  font-family: "Indie Flower";
  margin-top: -2vh;
  margin-left: 1vh;
  //word-wrap: break-word;/*英文的时候需要加上这句，自动换行*/
  /*自测了这句话没啥用*/
  //writing-mode: vertical-rl;/*从左向右 从右向左是 writing-mode: vertical-rl;*/
  writing-mode: tb-rl; /*IE浏览器的从左向右 从右向左是 writing-mode: tb-rl；*/
  text-align: center;
  padding: 0px;
  display: flex;
  -webkit-display: flex;
  flex-direction: column;
  /* align-content: center; */
  /* vertical-align: middle; */
  justify-content: center;

  .yb-img {
    width: 2vw;
    height: 2vw;
  }
}

.wd-main-box-show {
  z-index: 10;
  right: 0;
}

.wd-main-box-none {
  z-index: 3;
  right: -36vw;
}

#wd-word-box {
  display: flex;
  flex-direction: column;
  width: auto;
}

.wd-word-yb {
  margin-top: -6vh;
  margin-left: 8vw;
  font-family: "Indie Flower";
}

#wd-choice-box {
  color: #656464;
  text-align: center;
  padding-left: 1vw;
  display: flex;
  flex-direction: column;
  justify-content: center;

  div {
    margin-top: 1vh;

  }

  div:hover {

  }

  .al-zhaohua {
    //background-color: #d3f1d8;
    //color: #52c228;
    color: #bf3939;
    background-color: #eccdcd;
    cursor: default;
  }

  .al-xishi {
    color: #396fbf;
    background-color: #cde0ec;
    cursor: default;
  }

  .no-xishi {
    color: #626b72;
    background-color: #ededee;
    cursor: default;
  }

  .zjzw {

  }

  .zjzw:hover {
    color: #4fb429;
  }

  .zjzw:active {
    text-shadow: 1px 1px 1vh #e3e3e3;
    background-color: #c7c5c5;
  }

  .no-zhaohua {
    background-color: #dbdbdb;
    cursor: pointer;
  }
}
</style>
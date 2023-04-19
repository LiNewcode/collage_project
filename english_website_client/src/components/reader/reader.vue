<template>
  <div id="catalogue" style="" @mouseout='iconv=true' @mouseover="iconv=false">
    <img alt="" src="/public/open-blue-left.png" v-show="iconv">
    <div id="catalogue_title">
      Catalogue
    </div>
    <div id="catalogue_title_box">
      <span :class="catalogue_choice=='all'?'catalogue_choice':''" @click="getCatalogue('all')">全部</span>
      <el-divider direction="vertical"></el-divider>
      <span :class="catalogue_choice=='ztyd'?'catalogue_choice':''" @click="getCatalogue('ztyd')">真题阅读</span>
      <el-divider direction="vertical"></el-divider>
      <span :class="catalogue_choice=='tjyd'?'catalogue_choice':''" @click="getCatalogue('tjyd')">推荐阅读</span>
    </div>
    <div id="catalogue_content">
      <ul>
        <li v-for="item in catalogue" @click="getArticle(item._id,item.clock)" style="position: relative"><a
            :title="item.title"
        >{{ item.title }}</a>
          <div class="catalogue_clock" v-if="item.clock=='y'"
               style="">
            <img src="/already_clock.png"/>
          </div>
        </li>
      </ul>
    </div>
  </div>
  <img id="bigImg" v-if='page==""' src="/pablita-remote-education.png">
  <div v-if='page!==""' id="box" tabindex="1"
       style="" @keyup.tab="changeModel" @keyup.tab.prevent="">
    <div id="article" style="width: 68%;margin: 0;color:white;" tabindex="200" @keyup.tab="changeNext">
      <h1>{{ title }}</h1>
      <div id="content">
        <ul>
          <li class="paragraph" v-for="paragraph in article">
            <div class="paragraph-box">
              <div v-for="word in paragraph.content">
                <button @keyup.q="changeNext" @keyup.w="changeDesView" v-if="word.signal=='en'" :class='word.signal==="en"?"word":"noword"'
                        @click='put_word(word.word)'>{{ word.word }}
                </button>
                <span v-if="word.signal!=='en'" class="noword">{{ word.word }}</span>
              </div>
            </div>
            <p>{{ paragraph.des }}</p>
          </li>
          <div style="height: 8vh;margin-left: 26vw;padding-bottom: 5vh;cursor: pointer">
            <div v-if="daka"
                 style="display: flex;flex-direction: row;margin-top: 2vh;position: relative;width: 8vw;background-color: #f5f5f5;padding: 1vh 0.2vh;border-radius: 2vh;box-shadow: 1px 1px 2vh #e0dfdf">
              <img style="width: 2.3vw;height: 2.3vw;margin-left:0.6vh;border-radius: 50%;background-color: #d4dece;"
                   src="/success.png"/>
              <div style="margin-top: .7vh;margin-left: 1vw;color: #6be54f">已打卡</div>
            </div>
            <div v-if="!daka"
                 style="display: flex;flex-direction: row;margin-top: 2vh;position: relative;width: 8vw;background-color: #f5f5f5;padding: 1vh 0.2vh;border-radius: 2vh;box-shadow: 1px 1px 2vh #e0dfdf">
              <img style="width: 2vw;height: 2vw;margin-left:2vh;border-radius: 50%;"
                   src="/daka.png"/>
              <div style="margin-top: .7vh;margin-left: 1vw;color: #44a3ef" @click="clockIn()">打卡</div>
            </div>
          </div>
          <li class="paragraph annotation" v-for="anno in annotation">
            <p>{{ anno }}</p>
          </li>
        </ul>
      </div>

    </div>
    <f-b ref="funtionBook" v-if='fb_flush' :hr_word="hr_word" :newWord="newWord" :page="page"></f-b>
  </div>
</template>

<script>
import FB from "../functionBoard/FB.vue";

export default {
  name: "reader",
  data() {
    return {
      dir: ['1', '2', '3'],
      page: '',
      catalogue: [],
      iconv: true,
      article: [],
      title: '',
      catalogue_choice:'all',
      newWord: '',
      fb_flush: false,
      hr_word: '',
      annotation: [],
      daka: false


    }
  },
  components: {FB},
  props: ['indexShow'],
  emits: ['update:indexShow'],
  created() {
    this.getCatalogue('all');

  },
  mounted() {

  },
  watch: {
    async page(newVal, oleVal) {

    }
  },
  methods: {
    toPage(item) {
      this.page = item
    },
    async clockIn() {
      const res = await this.$http.get('/Reader/getArticle', {
        params: {
          choice: 'clockIn',
          _id: this.page,
          userId: localStorage.getItem('userId')
        }
      })
      let state = res.data.state
      // console.log('state', state)
      if (state == 'success') {
        this.daka = true
        for (let i = 0; i < this.catalogue.length; i++) {
          if (this.catalogue[i]._id == this.page) {
            this.catalogue[i].clock = 'y'
            break;
          }
        }

      }
    },
    async getCatalogue(choice) {
      this.catalogue = [];
      const res = await this.$http.get('/Reader/getCatalog', {
        params: {
          choice: choice,
          userId: localStorage.getItem('userId')
        }
      })
      this.catalogue = res.data.catalog;
      this.catalogue_choice=choice;
    },
    backToList() {
      this.$emit('update:indexShow', '');
    },
    async getArticle(id, clock) {
      // this.page = "";
      this.fb_flush = false;
      this.page = id;
      const res = await this.$http.get('/Reader/getArticle', {
        params: {
          _id: id,
          choice: 'content'
        },
        headers: {
          'Content-Type': 'text/plain;charset=UTF-8',
        },
      })

      this.article = res.data.article
      this.title = res.data.title
      this.annotation = res.data.annotation
      // console.log(this.annotation)
      this.fb_flush = true
      if (clock == 'n') {
        this.daka = false;
      } else {
        this.daka = true;
      }
    },
    put_word(word) {
      this.newWord = word
    },
    changeNext(event) {
      this.$refs.funtionBook.changeNext();
    },
    changeDesView(event){
      this.$refs.funtionBook.changeDesView();
    },
    changeModel() {
      // console.log('xxxxxxxxxxxxxxxxxxxxx')
    }


  }
}
</script>

<style scoped lang="less">
#catalogue {
  width: 15%;
  height: 90vh;
  position: absolute;
  margin-left: -13.7%;
  margin-top: 7vh;
  background-color: rgba(208, 211, 215, 0.3);

  transition-duration: 1s;

  padding-top: 5vh;

  img {
    position: absolute;
    max-width: 2vw;
    top: 45%;
    right: 1%;
  }

  #catalogue_title {
    width: 90%;
    height: 5%;
    margin-left: 5%;
    font-size: 1.2vw;
  }

  #catalogue_title_box {
    margin-left: 5%;
    font-size: 1vw;
    padding-bottom: 1px;

    span {
      cursor: pointer;
    }
  }

  #catalogue_content {
    width: 100%;
    height: 85%;
    overflow: scroll;

    ul {
      li {
        height: auto;
        max-height: 3.6vh;
        width: 86%;
        padding-top: 1.3vh;
        padding-bottom: .1vh;
        font-size: 1.4vh;
        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        border-bottom: #E0E0E0 1px solid;
        margin-bottom: 0.3vh;
        margin-top: 0.6vh;
        transition-duration: .3s;
        position: relative;

      }

      li:hover {
        cursor: pointer;
        max-height: 5vh;
        background-color: #2c6afc;
        font-size: 1vw;
      }
    }
  }

}

.catalogue_clock {


  position: absolute;
  top: 50%;
  margin-top: -0.5vw;
  right: 0.5vh;
  text-align: center;
  font-size: 0.8vw;
  font-weight: bold;
  border-radius: 1vh;
  img{
    width: 1vw;
    height: 1vw;
  }

}

#bigImg {
  width: 48vw;
  height: 90vh;
  margin-left: 20vw;
  margin-top: 5vh;
}

.annotation {
  padding-top: 0.2vh;
  padding-bottom: 0.2vh;
  margin-top: 0;
  margin-bottom: 0;

  p {
    font-size: 1.4vw;
    line-height: 1.4vw;
    padding: 0;
    margin-bottom: 0;
    margin-top: 0;
    color: #5a8ee7;
  }
}

#box {

  width: 98%;
  height: 90vh;
  margin-top: 1%;
  margin-left: 1.8%;
  margin-top: 8vh;
  display: flex;
  flex-direction: row;
  overflow: visible;
  background-color: #ffffff;

  #article {
    h1 {
      color: #35689a;
    }

    background-color: rgba(243, 232, 221, 0.9);
    padding-left: 1vw;
    box-shadow: 0 0 1vw rgba(199, 197, 197, 0.8);

    #content {
      .paragraph {
        color: #959595;
        font-size: 1.4vw;
      }
    }

    overflow: scroll;

    h1 {
      padding-left: 1.2vw;
      font-size: 2.5vw;
      padding-bottom: 3.8vh;
    }

    ul {
      max-width: 85%;
      margin-left: 7.5%;
      padding: 0;
      overflow: scroll;
      margin-top: 1vh;
      padding-top: .8vh;
      position: relative;

      li {
        padding-left: 2vw;

        transition-duration: .8s;
        position: relative;

        button {
          border: none;

        }

        span {
          position: relative;
        }

        p {
          padding-bottom: 5vh;
        }
      }
    }
  }
}
.catalogue_choice{
  border-bottom: 2px solid #ffab51;
  font-weight: bold;
}

.paragraph-box {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}

.word {
  transition-duration: .2s;
  font-size: 1.4vw;
  padding: 0.2vw;
  background-color: rgba(255, 255, 255, 0);
  color: #2c3e50;
  border-bottom:1px solid rgba(243, 232, 221, 0.9)!important;
}

.noword {
  font-size: 1.2vw;
  padding: 0.05vw;
  background-color: rgba(255, 255, 255, 0);
  color: #2c3e50;
}

.word:hover {
  cursor: pointer;
  //background-color: #2c3e50;
  //color: #ffffff;
  //font-weight: bold;
  border-bottom: 1px solid #f54fa6!important;
  //padding: 1vh 1vw;
  //position: fixed;
  //overflow: hidden;
  //margin-left: -.1vw;
}

.word:active {
  font-weight: bold;
  background-color: #2c3e50;
  color: #ffffff;
  padding: .2vh .2vw;
}

#catalogue:hover {
  margin-left: -1vw;
  background-color: #6396ee;
  color: white;
  z-index: 5;
}
</style>
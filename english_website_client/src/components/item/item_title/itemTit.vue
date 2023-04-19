<template>
  <div id="head" style="width: 95%;margin-right: 0">
    <div id="wad">
      <span id="word" :class='view?"up":"down"' >{{ word }}</span>
      <div id="description" :class='view?"s":"v"' @click="view=!view">
        <ul style="">
          <li class="des_item" v-for="item in explain">{{ item }}</li>
        </ul>
      </div>
    </div>
    <div class="phsBox" style="">
      <span class="tag" style="">英:</span>
      <span class="phs" style="">{{ phs[0] }}</span>
      <img src="/voice.png" class="icon" style="" @click="audio_play('au1')">

      <span class="tag" style="">美:</span>
      <span class="phs" style="">{{ phs[1] }}</span>
      <img src="/voice.png" class="icon" style="" @click="audio_play('au2')">
      <img id="collection" :src='!isCollect?"/collect_before.png":"/collect_after.png"' @click="changeCollect()"
           style=""/>
      <div v-if="isPee==1" id="peeSignal">研</div>
    </div>
  </div>

</template>

<script>
export default {
  name: "itemTit",
  data() {
    return {
      isCollect: false,
      view: true
    }
  },
  props: ['word', 'explain', 'phs','mp3_usa','mp3_bt','isPee','mp3_src','filename','wordSignal'],
  emits: ['update:mp3_src'],
  created(){
    if(this.wordSignal==='y'){
      this.isCollect=true
    }

  },
  methods:{
    audio_play(au){
      // document.getElementById(au).play()

      switch (au){
        case 'au1':
          this.$emit('update:mp3_src', this.mp3_usa);
          break;
        default:
          this.$emit('update:mp3_src', this.mp3_bt);
          break;
      }

    },
    changeDesView(){
      this.view=!this.view;
    },
    async changeCollect(){
      this.isCollect=!this.isCollect
      let choice;
      if(this.isCollect){
        choice = 'collect'
      }else{
        choice = 'not_collect'
      }
      let filename =  this.filename
      const res = await this.$http.get('/Reader/hr', {
        params: {
          _id: filename,
          choice: choice,
          word:this.word,
          userId: localStorage.getItem('userId'),
        },
        headers: {
          'Content-Type': 'text/plain;charset=UTF-8',
        },
      })
    }

  }
}
</script>

<style scoped lang="less">
ul, li {
  margin-block: 0;
  padding-inline: 0;
  padding-left: 2%;
  margin: 0;
  list-style: none
}
.des_item{
  margin-block:2vh;
}
#head {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: column;
}

#wad {
  display: flex;
  height: auto;
  flex-direction: row;
  overflow: hidden;
}

#word {
  border-radius: 1%;

  padding: 0% 2%;
  padding-top: 1.5%;

  margin-left: 5%;
  width: auto;
  content-align: center;
  font-weight: bold;
  font-size: 18*0.115vw;
  height: 30*0.115vw;
}
.up{
  margin-top: 2%;
}
.down{
  margin-top: 2%;
}
#collection {
  position: absolute;
  right: 2vw;
  max-width: 13*0.115vw;
  max-height: 13*0.115vw;

}

#collection:hover {
  cursor: pointer;
}

#description {
  padding-left: 2%;
  width: 73%;
  padding-bottom: 2%;

  ul {

    max-height: 100%;
    padding-right: 2%;
    padding-bottom: 0.4vh;


    li {
      width: 100%;
      margin-right: 10vh;
    }
  }

  :hover {
    cursor: pointer;
  }
}

.v {
  overflow: visible;
  height: auto;
}

.s {
  height: 36*0.115vw;
  overflow: scroll;
}
#peeSignal{
  width: 1.6vw;
  height: 1.5vw;
  font-size: 0.9vw;
  font-weight: bold;
  line-height: 1.5vw;
  color: #e0e0e0;
  border-radius: 3px;
  background-color: #d43f3f;
  text-align: center;
  position: absolute;
  right: 3.9vw;
  margin-top: .22vh;
}
::-webkit-scrollbar {
  width: 0vw;
}

#description::after {
  display: table;
  content: '';
  clear: both;
  margin-top: -6%;
  margin-left: 90%;

  background-color: #ffffff;

}

.tag {
  margin-right: 6*0.115vw;
  margin-left: 5*0.115vw;
  font-size: 7*0.115vw;
}

.phsBox {
  width: 100%;
  margin-left: 3%;
  margin-top: 2%;
  display: flex;
  flex-direction: row;
}

.phs {
  font-size: 8*0.115vw;
}
.icon{
  margin-left: 0.85*0.115vw;
  margin-right: 5*0.115vw;
  max-width: 10*0.115vw;
  max-height: 10*0.115vw;
  margin-top: 1*0.115vw;
}
</style>
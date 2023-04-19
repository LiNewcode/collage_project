<template>
  <div id="hr_box" v-if="wordList!==[]">


      <div>
    <item-body :ref="item.word" v-for="item in wordList" :filename="page" :wordSignal="item.signal" :id="item.word" v-bind:key="item.word"
               :stateItem='select===item.word?"unfold":"fold"'></item-body>
      </div>

  </div>
</template>

<script>


import ItemBody from "../item/item_body/itemBody.vue";

export default {
  name: "HR",
  data() {
    return {
      select: 'wrap',
      wordList: []
    }
  },
  props: ['page', 'newWord'],
  components: {ItemBody},
  created() {
    this.showHr(this.page);
  },
  watch: {
    async page(newVal, oldVal) {
      await this.showHr(newVal);
    },
    async newWord(newVal, oldVal) {
      let wl =this.wordList;

      if(wl===[]){
        this.wordList.unshift({'word':newVal,'signal':'n'})
      }else{
        let index = -1;
        for(let i=0;i<wl.length;i++){
          if(wl[i].word===newVal){
            index = i;
            break;
          }
        }

        if (index != -1) {
          this.wordList.splice(index, 1)
        }
        this.wordList.unshift({'word':newVal,'signal':'n'})

        this.select = newVal
      }
      this.$refs[this.newWord].playAudio()
    },

  },
  methods: {
    async showHr(id) {
      const res = await this.$http.get('/Reader/hr', {
        params: {
          _id: id,
          choice: 'show_all',
          userId: localStorage.getItem('userId'),
        },
        headers: {
          'Content-Type': 'text/plain;charset=UTF-8',
        },
      })
      this.wordList = res.data.data

    },
    changeNext(){
      this.$refs[this.newWord].changeNext()
    },
    changeDesView(){
      this.$refs[this.newWord].changeDesView();
    },
  }

}
</script>
<!--*0.115vw-->
<style scoped lang="less">
item-body {
  padding: 5vh 0;
  background-color: #E0E0E0;
  transition-duration: .3s;
}

#hr_box {
  display: flex;
  flex-direction: column;
  width: 100%;
  margin-right: 0;
  height: 100%;

}
</style>
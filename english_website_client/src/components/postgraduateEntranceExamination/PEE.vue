<template>
  <div id="box">
    <item-body v-for="item in nowList" :id="item.word" :filename="page" :wordSignal="item.signal"
               :stateItem='select==item?"unfold":"fold"'></item-body>
    <div class="addMore" @click="addWord()">加载更多</div>
  </div>
</template>

<script>
import ItemBody from "../item/item_body/itemBody.vue";

export default {
  name: "PEE",
  data() {
    return {
      select: 'wrap',
      wordList: [],
      nowList: [],
    }
  },
  props: ['page'],
  components: {ItemBody},
  created() {///Reader/getArticle
    this.getPee(this.page)
  },
  methods: {
    async getPee(id) {

      const res = await this.$http.get('/Reader/getArticle', {
        params: {
          _id: id,
          choice: 'pee',
          userId: localStorage.getItem('userId')
        },
        headers: {
          'Content-Type': 'text/plain;charset=UTF-8',
        },
      })

      this.wordList = res.data.pee
      this.addWord();
    },
    addWord() {
      let len_w = this.wordList.length
      let len_n = this.nowList.length
      if (len_w > len_n) {


        if (len_n + 20 < len_w) {
          this.nowList = this.nowList.concat(this.wordList.slice(len_n, len_n + 20));
        } else {
          this.nowList = this.nowList.concat(this.wordList.slice(len_n, -1))
        }
      }


    }
  },
  watch: {
    async page(newVal, oldVal) {

      const res = await this.$http.get('/Reader/getArticle', {
        params: {
          _id: newVal,
          choice: 'pee',
          userId: localStorage.getItem('userId')
        },
        headers: {
          'Content-Type': 'text/plain;charset=UTF-8',
        },
      })
      this.wordList = res.data.pee
      this.nowList = []
      this.addWord();
    }
  }

}
</script>
<!--*0.115vw-->
<style scoped lang="less">
item-body {
  padding: 5vh 0;
  background-color: #E0E0E0;

}

#box {
  display: flex;
  flex-direction: column;
  width: 100%;
  margin-right: 0;
  height: 100%;

}
.addMore{
  width: 8vw;
  background-color: #efeeee;
  height: 5vh;
  box-shadow: 1px 1px 5vh #f1f2fa;
  cursor: pointer;
  text-align: center;
  line-height: 5vh;
  margin-left: 10vw;
  margin-bottom: 1vh;
}
.addMore:hover{
  box-shadow: 1px 1px 5vh #d2d6f5;
  background-color: #2c6afc;
  color: #ffffff;
  border-radius: 1vh;
  transition-duration: .4s;
}
</style>
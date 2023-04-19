<template>
  <div id="box">
  <item-body v-for="(item,index) in wordList" :id="item.word" :filename="page" :wordSignal="'y'"
             :stateItem='select===item.word?"unfold":"fold"'></item-body>
  </div>
</template>

<script>
import ItemBody from "../item/item_body/itemBody.vue";
export default {
  name: "BM",
  components: {ItemBody},
  data() {
    return {
      select: 'wrap',
      wordList: []
    }
  },
  props: ['page'],
  created() {///Reader/getArticle
    this.getCollect(this.page)
  },
  watch:{
    async page(newVal ,oldVal){
      await this.getCollect(newVal);
    }
  },
  methods: {
    async getCollect(id) {

      const res = await this.$http.get('/Reader/getArticle', {
        params: {
          _id: id,
          choice: 'collect',
          userId: localStorage.getItem('userId')
        },
        headers: {
          'Content-Type': 'text/plain;charset=UTF-8',
        },
      })
      this.wordList = res.data.collect



    },

  }
}
</script>

<style scoped>
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
</style>
<template>
  <div>
<!--      <button :class="testType=='1'?'':''" @click="changeType('1')">英语一</button>-->
<!--      <button :class="testType=='1'?'':''" @click="changeType('2')">英语二</button>-->
      <el-tabs class="etab" v-model="activeName"  type="border-card">
        <el-tab-pane class="testListBox" label="英语一" name="y1">
          <el-card class="box-card testBox" v-for="(item ,index) in page_list_1" @click="openTestPage(item.year,1,item.beDone,item.score)">
            <template #header>
              <div class="card-header">
                <span> {{ item.year }} 年考研英语一真题</span>
                <el-button class="button" type="text">{{ item.beDone == 'true' ? '查看试卷' : '去做题' }}</el-button>
              </div>
            </template>
            {{ item.beDone == 'true' ? item.score : '未做' }}
          </el-card>
        </el-tab-pane>
        <el-tab-pane class="testListBox" label="英语二" name="y2">
          <el-card class="box-card testBox" v-for="(item ,index) in page_list_2" @click="openTestPage(item.year,2,item.beDone,item.score)">
            <template #header>
              <div class="card-header">
                <span> {{ item.year }} 年考研英语二真题</span>
                <el-button class="button" type="text">Operation button</el-button>
              </div>
              {{ item.beDone == 'true' ? item.score : '未做' }}
            </template>
          </el-card>
        </el-tab-pane>
      </el-tabs>


  </div>
</template>

<script>
export default {
  name: "TestList",

  data() {
    return {
      testType: '1',
      page_list_1: [],
      page_list_2: [],
      activeName:'y1'

    }
  },
  props: ['testPageSelected'],
  emits: ['update:testPageSelected'],
  created() {
    this.getList();
  },
  methods: {

    changeType(num) {
      this.testType = num;
    },
    async getList() {
      const res = await this.$http.get('/Test/testPage', {
        params: {
          _id: 'myId',
          username: localStorage.getItem('username'),
          userId: localStorage.getItem('userId'),
          choice: 'testList',

        },
        headers: {
          'Content-Type': 'text/plain;charset=UTF-8',
        },
      })
      console.log(res)
      this.page_list_1 = res.data.e1;
      this.page_list_2 = res.data.e2;
    },
    openTestPage(year, testType,beDone,score) {
      let picked;
      picked = [year, testType,beDone,score];


      this.$emit('update:testPageSelected', picked);
    }
  }
}
</script>

<style scoped>
.etab{
  margin-top: 8vh;
  margin-left: 7vw;
  height: 88vh;
}
.testBox {
  width: 16vw;
  height: 18vh;
  border: 1px ;
  text-align: center;
  margin-right: 4vw;
}

.testListBox {
  width: 80vw;
  height: 80vh;
  display: flex;
  overflow: scroll;
  flex-direction: row;
  margin-left: 2vw;
  margin-top: 5vh;
  /*padding-left: 4vw;*/
  flex-wrap: wrap;
}

</style>
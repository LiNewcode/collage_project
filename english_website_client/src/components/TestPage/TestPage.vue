<template>
  <div id="question">
    <div id="controlBox">
      <div id="eph">
        <el-page-header :icon="ArrowLeft" class="eph" @back="backToList()"/>
      </div>
      <!--v-show="beDone=='true'"-->
      <div id="itemChoice">
        <!--        <div v-if="beDone!=='true'" :class="item==''?'didnt':'did'" v-for="(item,index) in list_1_a_0"></div>-->
        <!--        <div v-if="beDone!=='true'" :class="item==''?'didnt':'did'" v-for="(item,index) in list_2_a_1"></div>-->
        <!--        <div v-if="beDone!=='true'" :class="item==''?'didnt':'did'" v-for="(item,index) in list_2_a_2"></div>-->
        <!--        <div v-if="beDone!=='true'" :class="item==''?'didnt':'did'" v-for="(item,index) in list_2_a_3"></div>-->
        <!--        <div v-if="beDone!=='true'" :class="item==''?'didnt':'did'" v-for="(item,index) in list_2_a_4"></div>-->
        <!--        <div v-if="beDone!=='true'" :class="item==''?'didnt':'did'" v-for="(item,index) in list_2_b_5"></div>-->
        <!--        <div v-if="beDone!=='true'" :class="item==''?'didnt':'did'" v-for="(item,index) in list_2_b_6"></div>-->
        <!--        <el-row :gutter="12" v-if="beDone=='true'">-->
        <!--          <el-col :span="8" v-for="(item,index) in user_res">-->
        <!--            <el-card shadow="hover" ><p>{{title_list[index]}}</p><span v-show="" >{{item}}</span></el-card>-->
        <!--          </el-col>-->
        <!--        </el-row>-->

        <div id="myHeader">

          <el-button v-if="beDone=='true'" type="primary" style="margin-left: 2vw;margin-top: -0.2vh"
                     @click="drawer = true">总览
          </el-button>
          <d-j-h style="margin-left: 20vw" v-if="beDone!=='true'"></d-j-h>
          <div v-if="beDone=='true'" style="margin-left: 60vw" id="score">成绩：{{ score }} 分</div>
          <el-button class="submit" type="success" style="margin-top: -0.3vh;margin-left: 32vw;" @click="handUp"
                     v-show="beDone!=='true'">交 卷
          </el-button>
        </div>

        <el-drawer class="drawerBox" v-if="beDone=='true'" v-model="drawer" title="I am the title" :with-header="false">
          <span>完型填空</span>
          <div class="drawerItem">
            <div :class="item=='n'?'error':'correct'" v-for="(item,index) in user_res[0]" @click="jump_test(index)">
              {{ index+1 }}
            </div>
          </div>
          <el-divider></el-divider>
          <span>阅读理解-1</span>
          <div class="drawerItem">

            <div :class="item=='n'?'error':'correct'" v-for="(item,index) in user_res[1]" @click="jump_test(20+index)">
              {{ 21 + index }}
            </div>
          </div>
          <el-divider></el-divider>
          <span>阅读理解-2</span>
          <div class="drawerItem">

            <div :class="item=='n'?'error':'correct'" v-for="(item,index) in user_res[2]" @click="jump_test(25+index)">
              {{ 26 + index }}
            </div>
          </div>
          <el-divider></el-divider>
          <span>阅读理解-3</span>
          <div class="drawerItem">
            <div :class="item=='n'?'error':'correct'" v-for="(item,index) in user_res[3]" @click="jump_test(30+index)">
              {{ 31 + index }}
            </div>
          </div>
          <el-divider></el-divider>
          <span>阅读理解-4</span>
          <div class="drawerItem">
            <div :class="item=='n'?'error':'correct'" v-for="(item,index) in user_res[4]" @click="jump_test(35+index)">
              {{ 36 + index }}
            </div>
          </div>
          <el-divider></el-divider>
          <span>创新阅读</span>
          <div class="drawerItem">

            <div :class="item=='n'?'error':'correct'" v-for="(item,index) in user_res[5]" @click="jump_test(40+index)">
              {{ 41 + index }}
            </div>
          </div>
          <el-divider></el-divider>
          <span>翻译</span>
          <div class="drawerItem">
            <div :class="item=='n'?'error':'correct'" v-for="(item,index) in user_res[5]" @click="jump_test(45+index)">
              {{ 46 + index }}
            </div>
          </div>


        </el-drawer>


      </div>

    </div>
    <div id="questionBox" v-if="MyLife">

      <div id="questionContent">

        <el-tabs v-model="pageNum" class="demo-tabs" @click="handleClick">
          <el-tab-pane id="wxtk" class="etp" label="完型填空" name='1'>

            <question-content v-show="pageNum=='1'" v-for="(item ,index) in wanXing.Content"
                              v-bind:testContent="item"></question-content>

          </el-tab-pane>
          <el-tab-pane id="yd1" class="etp" label="阅读理解-Text 1" name='2'>
            <question-content v-show="pageNum=='2'" v-for="(item ,index) in yueDu1.Content"
                              :testContent="item"></question-content>

          </el-tab-pane>
          <el-tab-pane id="yd2" class="etp" label="阅读理解-Text 2" name='3'>
            <question-content v-show="pageNum=='3'" v-for="(item ,index) in yueDu2.Content"
                              :testContent="item"></question-content>
          </el-tab-pane>
          <el-tab-pane id="yd3" class="etp" label="阅读理解-Text 3" name='4'>
            <question-content v-show="pageNum=='4'" v-for="(item ,index) in yueDu3.Content"
                              :testContent="item"></question-content>
          </el-tab-pane>
          <el-tab-pane id="yd4" class="etp" label="阅读理解-Text 4" name='5'>
            <question-content v-show="pageNum=='5'" v-for="(item ,index) in yueDu4.Content"
                              :testContent="item"></question-content>
          </el-tab-pane>
          <el-tab-pane id="cxyd" class="etp" label="创新阅读" name='6'>
            <question-content v-show="pageNum=='6'" v-for="(item ,index) in yueDu5.Content"
                              :testContent="item"></question-content>
          </el-tab-pane>
          <el-tab-pane id="fy" class="etp" label="翻译" name='7'>
            <question-content v-show="pageNum=='7'" v-for="(item ,index) in fanYi.Content"
                              :test-content="item"></question-content>
          </el-tab-pane>
          <el-tab-pane class="etp" label="小作文" name="8">
            <question-content v-show="pageNum=='8'" v-for="(item ,index) in xiaoZuoWen.Content"
                              :testContent="item"></question-content>
          </el-tab-pane>
          <el-tab-pane class="etp" label="大作文" name="9">
            <question-content v-show="pageNum=='9'" v-for="(item ,index) in daZuoWen.Content"
                              :test-content="item"></question-content>
          </el-tab-pane>
        </el-tabs>


      </div>
      <div id="questionReply" v-show="beDone!=='true'">
        <question v-show="pageNum==1" v-for="(item,index) in wanXing.QuestionList" :mySignal="wx" :qst="item.Question"
                  v-bind:choice="item.Choice" v-model:indexSelected="list_1_a_0[index]"></question>
        <question v-show="pageNum==2" v-for="(item,index) in yueDu1.QuestionList" :mySignal="yd" :qst="item.Question"
                  v-bind:choice="item.Choice" v-model:indexSelected="list_2_a_1[index]"></question>
        <question v-show="pageNum==3" v-for="(item,index) in yueDu2.QuestionList" :mySignal="yd" :qst="item.Question"
                  v-bind:choice="item.Choice" v-model:indexSelected="list_2_a_2[index]"></question>
        <question v-show="pageNum==4" v-for="(item,index) in yueDu3.QuestionList" :mySignal="yd" :qst="item.Question"
                  v-bind:choice="item.Choice" v-model:indexSelected="list_2_a_3[index]"></question>
        <question v-show="pageNum==5" v-for="(item,index) in yueDu4.QuestionList" :mySignal="yd" :qst="item.Question"
                  v-bind:choice="item.Choice" v-model:indexSelected="list_2_a_4[index]"></question>
        <question2 v-show="pageNum==6" v-for="(item,index) in yueDu5.QuestionList" :mySignal="yd" :qst="item.Question"
                   v-bind:choice="item.Choice" v-model:indexSelected="list_2_b_5[index]"></question2>
        <div v-show="pageNum==7">
          翻译答题区
          <div v-for="(item,index) in list_2_b_6" style="margin-top: 1.5vh;margin-bottom: 5vh;">
            <center>
              <div
                  style="border-radius: 50%;background-color: #5a8ee7;width: 1.2vw;height: 1.2vw;text-align: center;line-height: 1.2vw;color: white">
                {{ index + 46 }}
              </div>
            </center>
            <el-input
                v-model="list_2_b_6[index]"
                :autosize="{ minRows: 8, maxRows: 18 }"
                type="textarea"
                placeholder="Please input"

            >
            </el-input>
          </div>

        </div>
        <div v-show="pageNum==8">
          小作文答题区
          <el-input
              v-model="textarea2"
              :autosize="{ minRows: 15, maxRows: 30 }"
              type="textarea"
              placeholder="Please input"
              style="margin-top: 3vh;width: 96%"
          >
          </el-input>
        </div>
        <div v-show="pageNum==9">
          大作文答题区
          <el-input
              v-model="textarea2"
              :autosize="{ minRows: 15, maxRows: 30 }"
              type="textarea"
              placeholder="Please input"
              style="margin-top: 3vh;width: 96%"
          >
          </el-input>
        </div>
      </div>
      <div id="questionAns" v-show="beDone=='true'">
        <div>
          <el-tabs v-model="ansModelName" type="border-card">
            <el-tab-pane label="答题卡" name="1">
              <el-card class="box-card" v-for="(item,index) in dtkList">
                <div @click="jump_test(item.TiHao-1)">
                  <p>{{ item.Question }}</p>
                  <p v-for="i in item.Choice">{{ i.Text }}</p>
                  <p>我的答案：{{}}&nbsp;&nbsp;&nbsp;&nbsp; 正确答案:{{}}</p>
                </div>
              </el-card>
            </el-tab-pane>
            <el-tab-pane label="小题解析" name="2">
              <el-card class="box-card" v-if="qads!=null">
                <p>正确答案:&nbsp;{{ qads.ans }}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;正确率:&nbsp;{{ qads.rightRate }}%</p>
                <div>考点：
                  <el-tag class="ml-2" type="success">{{ qads.point }}</el-tag>
                </div>
                <p style="letter-spacing: 0.08vh;line-height: 3.1vh">解析:{{ qads.analysis }}</p>
              </el-card>
            </el-tab-pane>
            <el-tab-pane label="文章概述" name="3">文章概述
              <p v-for="item in ftr" style="letter-spacing: 0.1vh;">{{ item }}</p>
            </el-tab-pane>
            <el-tab-pane label="全文翻译" name="4">全文翻译
              <p v-for="item in sms" style="letter-spacing: 0.1vh;line-height: 3vh">{{ item }}</p>
            </el-tab-pane>
          </el-tabs>
        </div>
      </div>
      <div>

      </div>
    </div>
  </div>
</template>

<script>
import Question from "../Question/Question.vue";
import QuestionContent from "../questionContent/questionContent.vue";
import Question2 from "../Question2/Question2.vue";
import qs from 'qs'
import DJH from "../DaoJiShi/DJH.vue";


export default {
  name: "TestPage",
  components: {DJH, Question2, QuestionContent, Question},
  data() {
    return {
      list_1_a_0: ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
      list_2_a_1: ['', '', '', '', ''],
      list_2_a_2: ['', '', '', '', ''],
      list_2_a_3: ['', '', '', '', ''],
      list_2_a_4: ['', '', '', '', ''],
      list_2_b_5: ['', '', '', '', ''],
      list_2_b_6: ['', '', '', '', ''],
      list_3_a_7: ['', ''],
      title_list: ['完形填空', '阅读理解-1', '阅读理解-2', '阅读理解-3', '阅读理解-4', '创新阅读', '翻译', '小作文', '大作文'],
      list_ans: null,
      wanXing: null,
      yueDu1: null,
      yueDu2: null,
      yueDu3: null,
      yueDu4: null,
      yueDu5: null,
      fanYi: null,
      radio: '2',
      xiaoZuoWen: null,
      daZuoWen: null,
      MyLife: false,
      Choice: null,
      pageNum: '1',
      activeName: '',
      beDone: '',
      score: '',
      user_res: [],
      ansNav: '1',
      nowMyAns: '',
      qads: null,
      ansModelName: '1',
      bigDetail: null,
      ftr: null,
      sms: null,
      drawer: false,
      dtkList: null,
      wx: 'wx',
      yd: 'yd'
    }
  },
  props: ['testPageSelected'],
  emits: ['update:testPageSelected'],
  created() {
    this.getTestPage(this.testPageSelected[0], this.testPageSelected[1])
    this.getContent()
    this.beDone = this.testPageSelected[2]
    this.score = this.testPageSelected[3]
    if (this.beDone == 'true') {
      this.getAns(this.testPageSelected[0], this.testPageSelected[1]);

    }
  },
  watch: {
    async pageNum(newVal, oleVal) {
      let num = parseInt(newVal)
      num -= 1

      this.sms = this.bigDetail[num].sms
      this.ftr = this.bigDetail[num].ftr


      if (this.beDone == 'true') {
        switch (num) {
          case 0:
            this.dtkList = this.wanXing.QuestionList;
            break;
          case 1:
            this.dtkList = this.yueDu1.QuestionList;
            break;
          case 2:
            this.dtkList = this.yueDu2.QuestionList;
            break;
          case 3:
            this.dtkList = this.yueDu3.QuestionList;
            break;
          case 4:
            this.dtkList = this.yueDu4.QuestionList;
            break;
          case 5:
            this.dtkList = this.yueDu5.QuestionList;
            break;
          case 6:
            break;
          default:
            break;
        }

        this.qads = null;
      }

    }
  },
  methods: {
    async getTestPage(year, testType) {
      const res = await this.$http.get('/Test/testPage', {
        params: {
          _id: 'myId',
          choice: 'content',
          year: year,
          testType: testType,
          userId: localStorage.getItem('userId'),
        },
        headers: {
          'Content-Type': 'text/plain;charset=UTF-8',
        },
      })


      let data = res.data.testPage;
      this.wanXing = data[0];

      this.yueDu1 = data[1];
      this.yueDu2 = data[2];
      this.yueDu3 = data[3];
      this.yueDu4 = data[4];
      this.yueDu5 = data[5];
      this.fanYi = data[6];
      this.xiaoZuoWen = data[7];
      this.daZuoWen = data[8];
      this.MyLife = true;
      this.dtkList = data[0].QuestionList;



    },
    backToList() {
      this.$emit('update:testPageSelected', -1)
    },
    jump_test(index) {
      this.ansModelName = '2'
      switch (true) {
        case index < 20:
          this.pageNum = '1'
          break;
        case index >= 20 && index < 25:
          this.pageNum = '2'
          break;
        case index >= 25 && index < 30:
          this.pageNum = '3'
          break;
        case index >= 30 && index < 35:
          this.pageNum = '4'
          break;
        case index >= 35 && index < 40:
          this.pageNum = '5'
          break;
        case index >= 40 && index < 45:
          this.pageNum = '6'
          break;
        default:
          break;
      }
      this.getAnsDetail(index + 1)
    },
    async getAnsDetail(index) {
      let year = this.testPageSelected[0]
      let testType = this.testPageSelected[1]
      let _id = testType + '-' + year + '-' + index
      const res = await this.$http.get('/Test/testPage', {
        params: {
          _id: _id,
          choice: 'ansDetail'
        },
        headers: {
          'Content-Type': 'text/plain;charset=UTF-8',
        },
      })
      this.qads = res.data

    },
    getContent() {

    },
    async getAns(page, testType) {
      let res = await this.$http.get('/Test/testPage', {
        params: {
          _id: 'myId',
          choice: 'ans',
          year: page,
          testType: testType,
          userId: localStorage.getItem('userId'),
        },
        headers: {
          'Content-Type': 'text/plain;charset=UTF-8',
        },
      })
      this.user_res = res.data.res
      this.bigDetail = res.data.detail
      this.ftr = this.bigDetail[0].ftr
      this.sms = this.bigDetail[0].sms
    },
    async handUp() {
      let ans = [];
      ans = ans.concat(this.list_1_a_0);
      ans = ans.concat(this.list_2_a_1);
      ans = ans.concat(this.list_2_a_2);
      ans = ans.concat(this.list_2_a_3);
      ans = ans.concat(this.list_2_a_4);
      ans = ans.concat(this.list_2_b_5);
      ans = ans.concat(this.list_2_b_6);
      // ans.push(this.list_3_a_7);

      let empty = [];

      for (let index = 0; index < ans.length; index++) {
        if (ans[index] == '') {
          empty.push(index + 1);

        }
      }
      if (empty == [] || empty.length < 1) {
        alert(ans);
      } else {

        alert('您的 ' + empty.join(',') + '题还没做完！');
        return 0;
      }

      const res = await this.$http.get('/Test/headUp', {
        params: {
          ans: {'ans': ans},
          userId: localStorage.getItem('userId'),
          testType: this.testPageSelected[1],
          year: this.testPageSelected[0]
        },
        headers: {
          'Content-Type': 'text/plain;charset=UTF-8',
        },
      })

      this.beDone = 'true'
      if (this.beDone == 'true') {
        this.getAns(this.testPageSelected[0], this.testPageSelected[1]);

      }
    },
    handleClick() {
      // alert(this.activeName)
    }


  }
}
</script>

<style scoped lang="less">
#myHeader {
  //padding-top: 10vh;
  display: flex;

  flex-direction: row;
}

#question {
  display: flex;
  flex-direction: column;;
  overflow: hidden;
}

.etp {
  overflow: scroll !important;
  width: 62vw;
  height: 80vh;
  color: #5a8ee7;
  position: relative;
}

#eph {

}

.drawerBox {
  color: #7bd91d;

  span {
    height: 1vw;
    font-size: 1vw;
    line-height: 1vw;
    padding: 0;
    margin: 0;
    font-weight: bolder;
  }
}

.drawerItem {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;

}

#itemChoice {
  width: 96vw;
  height: 6vh;
  display: flex;
  flex-direction: row;
}

#score {
  width: 20vw;
  height: 2.2vw;
  background-color: #e2f5e2;
  color: #4fb429;
  font-size: 1.4vw;
  font-family: 'FangSong_GB2312';
  border-radius: 1.2vh;
  text-align: center;
  line-height: 2vw;
  margin-left: 2vw;
  text-align: center;
}

.didnt {
  width: 1.4vw;
  height: 1.4vw;
  margin-top: 2.2vh;
  border-radius: 50%;
  margin-left: 1vh;
  background-color: #959595;
  border-color: #bab9b9;
  text-align: center;
}

.did {
  width: 1.4vw;
  height: 1.4vw;
  margin-top: 2.2vh;
  border-radius: 50%;
  margin-left: 1vh;
  background-color: #f3f1f1;
  border-color: #ffffff;
  text-align: center;
}

.correct {
  width: 1.6vw;
  height: 1.6vw;
  line-height: 1.6vw;
  margin-top: 2vh;
  border-radius: 20%;
  margin-left: 1vh;
  background-color: #41e741;
  border-color: #ffffff;
  color: white;
  text-align: center;

}

.error {
  width: 1.6vw;
  height: 1.6vw;
  line-height: 1.6vw;
  margin-top: 2vh;
  border-radius: 20%;
  margin-left: 1vh;
  background-color: #ee2828;
  border-color: #ffffff;
  color: white;
  text-align: center;
}

#nav {
  float: left;
  list-style-type: none;
  margin: 0;
  padding: 0;

  li {
    float: left;
    margin-left: 3.2vw;

    .choose_nav {
      padding-bottom: 1vh;
      font-weight: normal;
      color: #2050ff;
      border-bottom: #2050ff solid 1px;
    }

    .nav {
      padding-bottom: 1vh;

    }
  }
}

#questionContent {
  color: #5a8ee7;
  display: flex;
  flex-direction: column;
  width: 64vw;
  overflow: hidden;
  border: #c4c3c3 .5px solid;
}

.demo-tabs > .el-tabs__content {
  padding: 32px;
  background-color: #f4f5f7;
  color: #6b778c;
  font-size: 32px;
  font-weight: 600;
}

#questionReply {
  display: flex;
  width: 35vw;
  flex-direction: column;
  overflow: scroll;
  height: 87.7vh;
  border: #c7c7c7 1px solid;
  padding-top: 1vh;
  //border-left: none!important;
  //border-bottom: none;
  padding-left: 1vw;
  margin-left: 2vw;
  margin-top: 0vh;
  //border: 1px solid;
}

#questionAns {
  display: flex;
  width: 35vw;
  flex-direction: column;
  overflow: scroll;
  height: 87.7vh;
  padding-top: 2vh;
  //border-left: none!important;
  //border-bottom: none;
  padding-left: 1vw;
  margin-top: 0vh;
  //border: 1px solid;
}

.btn {
  width: 18vw;
  height: 6vh;
}

.eph {
  color: #686a66;

  :hover {
    color: #5a8ee7;
  }
}

.submit {
  margin-top: 1vh;
  border-radius: 2vh;
  background-color: #5a8ee7;
  border-color: #5a8ee7;
  margin-left: 40vw;
}

#controlBox {
  margin-top: 8vh;

  display: flex;
  flex-direction: row;
}

#questionBox {
  width: 96vw;
  height: 86vh;
  display: flex;
  margin-top: -2vh;
  flex-direction: row;
  overflow: hidden;
}

</style>
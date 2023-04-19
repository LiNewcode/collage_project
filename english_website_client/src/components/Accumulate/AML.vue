<template>
  <div class="menuBox">
    <el-radio-group class="e_radio" v-model="isCollapse">
      <el-radio-button :label="false">expand</el-radio-button>
      <el-radio-button :label="true">collapse</el-radio-button>
    </el-radio-group>
    <el-menu
        default-active="1-1"
        class="el-menu-vertical-demo menu"
        :collapse="isCollapse"
        @open="handleOpen"
        @close="handleClose"
        @select="selectIndex"
    >
      <el-sub-menu index="1">
        <template #title>
          <!--          <el-icon><location /></el-icon>-->
          <img src="/cihui.png"/>
          <span>词汇积累</span>
        </template>

        <el-menu-item-group>
          <template #title><span>词汇分阶</span></template>
          <el-menu-item index="1-1">基础3500词</el-menu-item>
          <el-menu-item index="1-2">考研5500词</el-menu-item>
          <el-menu-item index="1-3">六级5500词</el-menu-item>
          <el-sub-menu index="1-4">
            <template #title><span>听写簿</span></template>
            <el-menu-item-group>
              <el-menu-item index="1-4-1" style="text-align: center" disabled>&nbsp;听音写英</el-menu-item>
              <el-menu-item index="1-4-2" style="text-align: center" disabled>&nbsp;听音写汉</el-menu-item>
              <el-menu-item index="1-4-3" style="text-align: center">&nbsp;看英写汉</el-menu-item>
            </el-menu-item-group>
          </el-sub-menu>
          <el-sub-menu index="1-5">
            <template #title><span>朝花夕拾</span></template>
            <el-menu-item-group>
              <el-menu-item index="1-5-1" style="text-align: center">&nbsp;朝花</el-menu-item>
              <el-menu-item index="1-5-2" style="text-align: center">&nbsp;夕拾</el-menu-item>
              <!--            <el-menu-item index="1-4-3" style="text-align: center" >&nbsp;看英写汉 </el-menu-item>-->
            </el-menu-item-group>
          </el-sub-menu>
        </el-menu-item-group>
      </el-sub-menu>
      <el-menu-item index="2">
        <!--      <el-icon><icon-menu /></el-icon>-->
        <img src="/zhenti.png"/>
        <template #title>真题匹配</template>
      </el-menu-item>
      <el-menu-item index="3" disabled>
        <img src="/cuoti.png"/>
        <template #title>错题积累</template>
      </el-menu-item>
      <el-menu-item index="4" disabled>
        <img src="/zuowen.png"/>
        <template #title>作文积累</template>
      </el-menu-item>
    </el-menu>
  </div>
  <div id="aml">
    <div id="aml-similarity" v-show="showItem=='similarity'">
      <el-table
          :data="similarity_list"
          :default-sort="{ prop: 'similarity', order: 'descending' }"
          style="width: 58vw;height: 80vh;overflow: scroll;margin-left: 6.2vw"
      >
        <el-table-column prop="similarity" label="匹配度" sortable width="190"/>
        <el-table-column prop="type" label="类型" :formatter="formatter"/>
        <el-table-column prop="year" label="年份" width="190"/>
        <el-table-column prop="index" label="题目" width="190"/>
      </el-table>
    </div>

    <div id="txb" v-show="showItem=='kyxh'">
      <div class="txb-title">
        <span class="txb-kyxh-choice" :class="txb_kyxh.tx_choice=='1'?'txb-kyxh-selected':'txb-kyxh-non-selected'"
              @click="txb_kyxh.tx_choice='1'">单词篮子</span>
        <el-divider direction="vertical"></el-divider>
        <span class="txb-kyxh-choice" :class="txb_kyxh.tx_choice=='2'?'txb-kyxh-selected':'txb-kyxh-non-selected'"
              @click="txb_kyxh.tx_choice='2'">随机抽取</span>
      </div>
      <el-divider/>
      <div class="txb-body"></div>
    </div>


    <div v-for="tab in et">
      <el-tabs type="border-card" class="demo-tabs" v-if="showItem==tab.showSignal"
               style="margin-left: -9vw;width: 80vw;background-color: #ffffff;">
        <el-tab-pane :label="tab.label" style="background-color: #ffffff">
          <center>
            <div v-if="(showItem!=='zh')&&(showItem!=='xs')">
              <el-check-tag :checked="checked=='my'" @change="" @click="onChange('my')">已积累</el-check-tag>
              <span style="width: 2vw;">&nbsp;&nbsp;</span>
              <el-check-tag :checked="checked=='no'" @change="" @click="onChange('no')">未积累</el-check-tag>
            </div>
          </center>
          <div v-if="detailSignal">
            <w-d @fatherMethod="deleteWord" @fatherMethod2="deleteWord2" :selectedMenu="showItem"
                 :word="now_selected"></w-d>
          </div>
          <div style="display: flex;flex-direction: row;flex-wrap: wrap">
            <w-c :word="item" v-for="(item,index) in now_word" @click="showDetail(item,index)"></w-c>
          </div>
          <center>
            <el-pagination v-model:currentPage="page" background page-size="10" layout="prev, pager, next"
                           :total="total">
              <audio autoplay/>
            </el-pagination>
          </center>

        </el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>

<script>
import WC from "../WordCard/WC.vue";
import WD from "../WordCard/WD.vue";

export default {
  name: "AML",
  components: {WD, WC},
  data() {
    return {
      similarity_list: [],
      isCollapse: false,
      showItem: 'jc',
      detailSignal: false,
      checked: 'my',
      word_my: [],
      word_no: [],
      page: 1,
      total: 10,
      now_word: [],
      now_selected: '',
      now_delete_word: '',
      et: [{
        label: '高中基础词汇',
        showSignal: 'jc',
        detailSignal: 'jc',
      }, {
        label: '考研词汇',
        showSignal: 'ky',
        detailSignal: 'ky',
      },
        {
          label: '六级词汇',
          showSignal: 'lj',
          detailSignal: 'lj',
        },
        {
          label: '朝花',
          showSignal: 'zh',
          detailSignal: 'zh',
        },
        {
          label: '夕拾',
          showSignal: 'xs',
          detailSignal: 'xs',
        },
      ],

      txb_kyxh: {
        tx_choice: '1'
      }


    }
  },
  created() {
    this.getRecommend();
    this.getWordList('jc')
  },
  watch: {
    async page(newVal, oldVal) {
      this.detailSignal = false
      this.change_now_word();
    },

    async checked(newVal, oldVal) {

      this.detailSignal = false
      this.change_now_word();

    }
  },
  methods: {
    selectIndex(index, indexPath) {
      switch (index) {
        case '1-1':
          this.showItem = 'jc';
          this.detailSignal = false;
          this.getWordList('jc');
          break;
        case '1-2':
          this.showItem = 'ky';
          this.detailSignal = false;
          this.getWordList('ky')
          break;
        case '1-3':
          this.showItem = 'lj';
          this.detailSignal = false;
          this.getWordList('lj')
          break;
        case '1-4-3':
          // this.detailSignal=false;
          this.showItem = 'kyxh';
          break;
        case '1-5-1':
          this.showItem = 'zh';
          this.detailSignal = false;
          this.getWordList('zh');
          break;
        case '1-5-2':
          this.showItem = 'xs';
          this.detailSignal = false;
          this.getWordList('xs');
          break;
        case '2':
          this.showItem = 'similarity';
          break;
        case '3':
          this.showItem = 'cuoTi';
          break;
      }
    },
    showDetail(word, index) {
      this.detailSignal = true;
      this.now_selected = word;
      this.selected_index = (this.page - 1) * 10 + index;
      // this.deleteWord(word, index);
    },
    deleteWord() {
      this.word_no.splice(this.selected_index, 1);
      this.word_my.unshift(this.now_selected);
      this.now_selected = '';
      this.selected_index = -1;
      this.detailSignal = false;
      this.change_now_word();
    },
    change_now_word() {
      if (this.checked == 'no') {
        this.total = this.word_no.length
        this.now_word = this.word_no.slice((this.page - 1) * 10, this.page * 10)
      } else {
        this.total = this.word_my.length
        this.now_word = this.word_my.slice((this.page - 1) * 10, this.page * 10)
      }
    },
    async getRecommend() {
      const res = await this.$http.get('/User/Recommend', {
        params: {
          userId: localStorage.getItem('userId'),
        },
        headers: {
          'Content-Type': 'text/plain;charset=UTF-8',
        },
      })
      this.similarity_list = res.data.similarity_list

    },
    async getWordList(choice) {
      const res = await this.$http.get('/User/Accumulate', {
        params: {
          userId: localStorage.getItem('userId'),
          choice: choice
        },
        headers: {
          'Content-Type': 'text/plain;charset=UTF-8',
        },
      })
      this.word_my = res.data.data.my
      this.word_no = res.data.data.no
      if (this.checked == 'no') {
        this.total = this.word_no.length
        this.now_word = this.word_no.slice((this.page - 1) * 10, this.page * 10)
      } else {
        this.now_word = this.word_my.slice((this.page - 1) * 10, this.page * 10)
        this.total = this.word_my.length
      }


    },
    deleteWord2() {
      let signal = ''
      if (this.word_my[this.selected_index] == this.now_selected) {
        this.word_my.splice(this.selected_index, 1);
        if (this.selected_index - 1 < 0) {
          this.selected_index = 0;
        } else if (this.selected_index <= this.word_my.length) {
          this.now_selected = this.word_my[this.selected_index];
        } else {
          this.selected_index = this.selected_index - 1;
          this.now_selected = this.word_my[this.selected_index - 1];
        }

      }
      if (this.word_no[this.selected_index] == this.now_selected) {
        this.word_no.splice(this.selected_index, 1);
        if (this.selected_index - 1 < 0) {
          this.selected_index = 0;
        } else if (this.selected_index <= this.word_no.length) {
          this.now_selected = this.word_no[this.selected_index];
        } else {
          this.selected_index = this.selected_index - 1;
          this.now_selected = this.word_no[this.selected_index - 1];
        }
      }

      // this.word_my.unshift(this.now_selected);

      // this.selected_index ;
      // this.detailSignal = false;
      this.change_now_word();
    },
    onChange(choice) {

      if (this.checked == 'no' && choice == 'my') {
        this.checked = 'my';

        this.total = this.word_my.length
        this.now_word = this.word_no.slice((this.page - 1) * 10, this.page * 10)
      } else if (this.checked == 'my' && choice == 'no') {
        this.checked = 'no';
        this.total = this.word_no.length
        this.now_word = this.word_no.slice((this.page - 1) * 10, this.page * 10)
      }

      // this.page = 1;
    },
  }
}
</script>

<style scoped>
#aml {
  width: 90vw;
  height: 88vh;
  margin-top: 8vh;
  margin-left: 4vw;
}

.menuBox {
  display: flex;
  flex-direction: column;
}

.e_radio {
  margin-top: 8vh;
  display: flex;
  flex-direction: row;
  width: 20vw;
  margin-left: 1vw;
}

.menu {
  margin-top: 2vh;
}

.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}

#aml-similarity {
  width: 70vw;
  padding: 3vh 3vw;
  margin-left: -10vw;
  border: 1px #eceaea solid;
  box-shadow: 1px 1px 10px #f3f1f1;
}

.txb-kyxh-choice {
  font-family: FangSong_GB2312;
  cursor: default;
}

.txb-kyxh-non-selected {
  color: #959595;
}

.txb-kyxh-selected {
  color: #5082f6;
}

img {
  width: 2vh;
  margin-right: 1vh;
}

#txb {
  width: 70vw;
  margin-left: -5vw;
  padding-top: 2vh;
}
</style>
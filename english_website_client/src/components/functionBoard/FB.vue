<template>
  <div id="fb" v-if="true">

    <div id="setting">
      <div class="Rod" style="width: 5.5%;"></div>
      <div class="Rod" style="width: 4.5%;"></div>
      <div class="Rod" style="width: 3%;"></div>
    </div>

    <div id="slider" style="">
      <h-r id="hr" ref="hr" :newWord="newWord" :page="page" v-show='view==="hr"' :class='view==="hr"?"vy":"vn"' style=""></h-r>
      <b-m id="bm" v-if='view==="bm"' :page="page" :class='view==="bm"?"vy":"vn"' style=""></b-m>
      <p-e-e id="pee" :page="page" v-if="showPee" v-show='view==="pee"' :class='view==="pee"?"vy":"vn"' style=""></p-e-e>
      <el-backtop target="#slider" :visibility-height="10" :right="50" :bottom="140"></el-backtop>
    </div>

    <div id="bar">
      <span class="icon" :class='view==="bm"?"icon-selected":"icon-selected-non"' @click='view="bm"'><img
          :src='view==="bm"?"/bm-select.png":"/bm.png"'></span>
      <span class="icon" :class='view==="hr"?"icon-selected":"icon-selected-non"' @click='view="hr"'><img
          :src='view==="hr"?"/hr-select.png":"/hr.png"'></span>
      <span class="icon" :class='view==="pee"?"icon-selected":"icon-selected-non"' @click='view="pee";showPee=true'><img
          :src='view==="pee"?"/pee-select.png":"/pee.png"'></span>
    </div>

  </div>
</template>

<script>
import HR from "../historicalRecords/HR.vue";
import BM from "../bookMark/BM.vue";
import PEE from "../postgraduateEntranceExamination/PEE.vue";

export default {
  name: "FB",
  data() {
    return {
      view: '',
      hrWordDetail:'',
      hrReview:true,
      showPee:false
    }
  },
  components: {PEE, BM, HR},
  props: ['page', 'newWord','hr_word'],
  watch:{
    async page(newVal ,oldVal){

        this.view='';
        this.view='hr';
        this.showPee=true;
    },
    async newWord(newVal ,oldVal){

      const res = await this.$http.get('/Reader/hr', {
        params: {
          _id:this.page,
          word:newVal,
          choice:'query',
          userId: localStorage.getItem('userId'),
        },
        headers: {
          'Content-Type': 'text/plain;charset=UTF-8',
        },
      })
      this.hrWordDetail = res.data

    }
  },
  created(){
    this.view='hr';
    // this.xiuTan(this.page);
  },
  methods:{
    changeNext(){

      this.$refs.hr.changeNext();

    },
    changeDesView(){
      this.$refs.hr.changeDesView();
    },
    // async xiuTan(id){
    //     const res = await this.$http.get('/Reader/hr', {
    //       params: {
    //         _id: id,
    //         choice: 'show_all',
    //         userId: localStorage.getItem('userId'),
    //       },
    //       headers: {
    //         'Content-Type': 'text/plain;charset=UTF-8',
    //       },
    //     })
    //     if (res.data.data)
    //
    // }
  }
}
</script>

<style scoped lang="less">
#fb {
  display: flex;
  flex-direction: column;
  width: 30%;
  height: 94%;
  margin-left: 1vw;
  margin-top: 2vh;
  padding: 0;
  border-radius: 0.115*8vw;
  box-shadow: 0px 0vw 0.115*12vw #E0E0E0;
}


.Rod {
  border-radius: 6vh; /*6px*/
  height: 25%;
  background-color: #E0E0E0;
  margin-top: .5%;
}

#setting {
  width: 96.5%;
  margin-left: 3.5%;
  height: 2%;
  margin-top: 2%;
}

#slider {
  height: 83%;
  margin-top: 3%;
  padding-top: 1%;
  width: 96%;
  margin-left: 2%;
  border-radius: 0.115*8vw;
  box-shadow: 0px 0vw 0.115*12vw #F4F4F4;
  overflow: scroll;

}

.vn {
  display: none;
}

.vy {

}

::-webkit-scrollbar {
  width: 0vw;
}

#hr {
  width: 100%;
  margin-right: 0;
}

#pee {
  width: 100%;
  margin-right: 0;
}

#bar {
  margin-top: 3%;
  padding: 0%;
  display: flex;
  flex-direction: row;
  bottom: 0;
  width: 100%;
  height: 10%;
  border-radius: 0px 0px 0.115*8vw 0.115*8vw;
  box-shadow: 0px 0px 0.115*12vw #E0E0E0, inset 0px 0px 0.115*12vw #FDFDFD;
  overflow: hidden;

  .icon {
    width: 33.3%;
    height: 100%;

    img {
      position: relative;
      width: 2vw;
      max-width: 3vw;
      left: 50%;
      top: 50%;
      margin-left: -1vw;
      margin-top: -1vw;
    }
  }

  .icon:hover {
    cursor: pointer;
    background-color: #e0e0e0;
  }
}

.icon-selected {
  background-color: #2c3e50;
}

.icon-selected-non {

}
</style>
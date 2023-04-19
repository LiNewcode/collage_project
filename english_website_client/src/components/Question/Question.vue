<template>
  <div id="v-model-radiobutton">
    <center v-if="mySignal==='wx'">
      <div
          style="border-radius: 50%;background-color: #5a8ee7;width: 1.2vw;height: 1.2vw;text-align: center;line-height: 1.2vw;color: white">
        {{ qst }}
      </div>
    </center>
    <p v-if="mySignal=='yd'">{{ qst }}</p>
    <el-radio class="radio" v-model="picked" label="A" size="large" border="false">{{ choice[0].Text }}</el-radio>
    <el-radio class="radio" v-model="picked" label="B" size="large" border="false">{{ choice[1].Text }}</el-radio>
    <el-radio class="radio" v-model="picked" label="C" size="large" border>{{ choice[2].Text }}</el-radio>
    <el-radio class="radio" v-model="picked" label="D" size="large" border>{{ choice[3].Text }}</el-radio>
    <!--      <input type="radio" id="A" value="A"  v-model="picked" />-->
    <!--      <label for="A"></label>-->

    <!--      <input type="radio" id="B" value="B" v-model="picked" />-->
    <!--      <label for="B">{{choice[1].Text}}</label>-->

    <!--      <input type="radio" id="C" value="C" v-model="picked" />-->
    <!--      <label for="C">{{choice[2].Text}}</label>-->

    <!--      <input type="radio" id="D" value="D" v-model="picked" />-->
    <!--      <label for="D">{{choice[3].Text}}</label>-->
    <!--      <span>{{indexSelected}}</span>-->
    <br/>

    <br/>
  </div>
</template>

<script>
export default {
  name: "Question",
  props: {
    indexSelected: String,
    qst: String,
    mySignal: String,
    choice: {
      type: Array,
      default: [{}, {}, {}, {}]
    },

  },
  emits: ['update:indexSelected'],
  data() {
    return {
      picked: '',
    };
  },
  created() {

  },
  methods: {
    getAns() {
      this.$emit('update:indexSelected', this.picked)
    }
  },
  watch: {
    async picked(newVal, oldVal) {
      this.getAns();
      // alert(this.picked)
    }
  },
}
</script>

<style scoped>
#v-model-radiobutton {
  margin-bottom: 1vh;
  display: flex;
  flex-direction: column;
  padding-left: 1vh;
}

.radio {
  margin-left: 1.5vw;
  margin-top: 0.5vh;
}
</style>
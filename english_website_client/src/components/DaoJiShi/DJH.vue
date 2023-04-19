<template>
<!--  <div>-->
<!--    <input type="datetime-local" :min="currentTime" placeholder="请输入秒杀开始时间" v-model="startTime">-->
<!--    <button @click="submit">开始计时</button>-->
<!--  </div>-->
  <div>
    <span class="djs">{{ countDownTime }}</span>
  </div>
</template>

<script>
let timer = null;
let tipTextPrefix = '离考试结束还有： ';
import moment from "moment";
export default {
  name: "DJH",
  data() { return {
    currentTime: moment().format('YYYY-MM-DDTHH:mm'), // 请使用步骤1-3计算出来的服务器时间
    startTime: moment().format('YYYY-MM-DDTHH:mm'),
    countDownTime: tipTextPrefix + '0天 0小时 0分钟 0秒',
    seconds:3600*3
  }},
  created(){
    this.submit();
  },
  methods: {
    submit: function() {
      const _this = this;
      clearInterval(timer);
      timer = setInterval(() => {
        _this.countDownTime = _this.countDown();
      }, 1000);
    },
    countDown: function() {

      const seconds = this.seconds;
      this.seconds--;

      if (seconds <= 0) {
        clearInterval(timer);
        return '秒杀已开始';
      }
      const second = seconds%60;
      const minutes = (seconds-second) / 60;
      const minute = minutes%60;
      const hours = (minutes-minute) / 60;
      const hour = hours%24;
      const day = (hours-hour) / 24;
      const res = tipTextPrefix + hour + '小时 '+ minute + '分钟 '+ second + '秒 ';
      return res;
    }
  },
}
</script>

<style>
.djs{
  padding: 1vh 1vw;
  margin-left: 12vw;
  font-size: 2vh;
  /*background-color: #8ad564;*/
  color: #5a8ee7;
}
</style>


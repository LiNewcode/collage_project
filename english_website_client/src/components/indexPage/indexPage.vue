<template>
  <div id="indexPage" v-show="indexShow==''">

    <div id="read" v-model:indexShow="indexShow" class="miniBox" v-show="indexShow==''" @click="showRead">
      <img src="/pablita-remote-education.png">
      <p>Read</p>
    </div>
    <div id="test" v-model:indexShow="indexShow" class="miniBox" v-show="indexShow==''" @click="showTest">
      <img src="/pablita-page-is-under-construction.png">
      <p>Test</p></div>
  </div>
</template>

<script>
export default {
  name: "indexPage",
  data() {
    return {
      activeIndex:'1'
    }
  },

  props: ['indexShow','userId'],
  emits: ['update:indexShow'],
  methods: {
    showRead() {
      alert('不让你点')
      // this.$emit('update:indexShow', 'read')
    },
    showTest() {
      alert('不让你点')
      // this.$emit('update:indexShow', 'test')
    }
  }
}
</script>

<style scoped lang="less">
#indexPage {
  display: flex;
  flex-direction: row;
  position: relative;
  width: 80%;
  height: 80%;
  left: 50%;
  margin-left: -40%;
  //background-color: #2c3e50;
}

#read {
  img {
    max-width: 80%;
    margin-left: 12%;
  }
}

#test {
  img {
    max-width: 95%;
    height: 77%;
    margin-left: 2.5%;
    margin-top: 8%;
  }
}

.miniBox {
  position: relative;
  left: 8vw;
  display: block;
  width: 25vw;
  height: 40vh;
  margin-left: 10vh;
  margin-top: 20vh;
  background-color: rgba(248, 246, 248, 0.8);
  transition-duration: 0.2s;


  p {
    position: absolute;
    bottom: -15vh;
    font-size: 2.5vw;
    color: #52249a;
    width: 100%;
    line-height: 4vw;
    border:  rgba(240, 238, 240, 0.8) 1px solid;
    background-color: rgba(252, 253, 253, 0.6);
    text-align: center;
    transition-duration: 0.2s;
  }

  p:hover {
    background-color: rgba(255, 253, 253, 0.6);
    box-shadow: 0 0 1vw rgba(235, 220, 235, 0.8);
    cursor: pointer;
  }
}

.miniBox:hover {
  background-color: rgba(252, 252, 252, 0.8);
  box-shadow: 0 0 1vw rgba(230, 220, 240, 0.8);
  cursor: pointer;
}
</style>
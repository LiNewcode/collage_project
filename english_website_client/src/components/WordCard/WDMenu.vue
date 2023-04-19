<template>
  <div id="wd-menu">
    <span :class="selected_menu=='js'?'select':''" @click="change_menu('js')">解释</span>
    <div class="wd-line"></div>
    <span :class="selected_menu=='cz'?'select':''" @click="change_menu('cz')">词组</span>
    <div class="wd-line"></div>
    <span :class="selected_menu=='lj'?'select':''" @click="change_menu('lj')">例句</span>
    <!--  <div class="wd-line"></div>-->
  </div>
</template>

<script>
export default {
  name: "WDmenu",
  data() {
    return {}
  },
  props: {
    selected_menu: String
  },
  emits: ['update:selected_menu'],
  methods: {
    change_menu(item) {
      if (item == this.selected_menu) {
        this.$emit('update:selected_menu', '')
      } else {
        this.$emit('update:selected_menu', item)
      }

    }
  }
}
</script>

<style scoped lang="less">
#wd-menu {
  display: flex;
  flex-direction: column;
  width: 8vw;
  height: 19vh;
  font-family: "Bodoni MT Black";

  span {
    width: 7.8vw;
    height: 6vh;
    text-align: center;
    line-height: 6vh;
  }

  span:hover {
    cursor: pointer;
    background-color: #e5effd;
  }
}

.wd-line {
  width: 5vw;
  height: 0.1vh;
  margin-left: 1.5vw;
  border-top: 1px solid #e7e6e6;
}

.select {
  background-color: #e5effd;
  color: #5a8ee7;
  font-weight: bold;

}
</style>
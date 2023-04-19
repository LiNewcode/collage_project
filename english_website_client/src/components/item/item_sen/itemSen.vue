<template>
  <div >
    <div v-for="item in sentence.example" style="display: flex;flex-direction: column;margin-left: 20px;padding-top: 3vh">
      <span class="en">{{ item.en }}</span>
        <span class="ch">{{ item.ch }}</span>
    </div>

  </div>
</template>

<script>
export default {
  name: "itemSen",
  data(){
    return{

    }
  },
  props:['sentence']
}
</script>

<style scoped lang="less">
.en{
  padding-bottom: 1vh;
}
.ch{
  padding-bottom: 2vh;
}
</style>
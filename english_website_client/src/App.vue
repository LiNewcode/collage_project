<template>
  <el-menu
      :default-active="activeIndex"
      class="el-menu-demo menu"
      mode="horizontal"
      @select="handleSelect"
      ref="menu"
  >
    <el-menu-item index="1">首页</el-menu-item>
    <el-menu-item index="2">阅读</el-menu-item>
    <el-menu-item index="3">测试</el-menu-item>
    <el-menu-item index="4">积累库</el-menu-item>
    <el-menu-item index="5">反馈</el-menu-item>
    <el-sub-menu index="6">
      <template #title>个人</template>
      <el-menu-item index="6-1">登陆</el-menu-item>
      <el-menu-item index="6-2">注册</el-menu-item>
      <el-menu-item index="6-3">个人信息</el-menu-item>
    </el-sub-menu>
  </el-menu>
  <login v-model:indexShow="indexShow" v-model:userId="userId" v-if="indexShow=='login'"></login>
  <register v-model:indexShow="indexShow" v-model:userId="userId" v-if="indexShow=='register'"></register>
<reader v-model:indexShow="indexShow" :userId="userId" v-show="readerShow" v-if="indexShow=='read'"></reader>
  <test v-model:indexShow="indexShow" :userId="userId" v-show="!readerShow" v-if="indexShow=='test'"></test>
  <a-m-l v-model:indexShow="indexShow" :userId="userId" v-show="!readerShow" v-if="indexShow=='accumulate'"></a-m-l>
  <f-d-b v-model:indexShow="indexShow" :userId="userId" v-show="!readerShow" v-if="indexShow=='feedback'"></f-d-b>
  <info v-model:indexShow="indexShow" :userId="userId" v-show="!readerShow" v-if="indexShow=='info'"></info>
<index-page  v-model:indexShow="indexShow" :userId="userId" ></index-page>
</template>

<script>
import Reader from "./components/reader/reader.vue";
import IndexPage from "./components/indexPage/indexPage.vue";
import Test from "./components/Test/Test.vue";
import Login from "./components/Login/Login.vue";
import Register from "./components/Register/Register.vue";
import AML from "./components/Accumulate/AML.vue";
import FDB from "./components/FeedBack/FDB.vue";
import Info from "./components/Info/Info.vue";
export default {
  name: 'App',
  components: {Info, FDB, AML, Register, Login, Test, IndexPage, Reader},
  data(){
    return{
    readerShow:false,
      readerIf:false,
      indexShow:'',
      userId:'',
      loginState:'',
      activeIndex:'1'
    }
  },
  // watch:{
  //   async indexShow(newV,oldV){
  //     switch (newV){
  //       case 'read':
  //         this.
  //     }
  //   }
  // },
  created() {
    this.isLogin();
  },
  methods: {
    handleSelect(key, keyPath){

      switch (key){
        case "1":
          this.indexShow=''
          break;
        case "2":
          this.indexShow='read'
          break;
        case "3":
          this.indexShow='test'
          break;
        case "4":
          this.indexShow='accumulate'
          break;
        case "5":
          this.indexShow='feedback';
          break;
        case "6-1":
          this.indexShow='login'
          break;
        case "6-2":
          this.indexShow='register';
          break;
        case "6-3":
          this.indexShow='info';
          break;
      }
    },
    async isLogin(){
      let un = localStorage.getItem('username')
      let pwd = localStorage.getItem('password')

      let id = localStorage.getItem('id')
      const res = await this.$http.get('/User/login', {
        params: {
          username: un,
          password: pwd
        },
        headers: {
          'Content-Type': 'text/plain;charset=UTF-8',
        },
        cookies:{
          withCredentials: true
        }
      })
      // this.$emit('update:indexShow', '')
      let data = res.data
      if(data.state=='true'){
        this.$message.success(
            {
              message:'尊敬的 '+ un+' ,欢迎回来！'
            }
        )
        this.indexShow=''
      }else {
        this.$message.error(
            {
              message: '请登录！'
            }
        )
        this.indexShow='login'
      }

    }
  }
}
</script>
<style scoped>
.menu{
  position: absolute;
  width: 100%;
  height: 7vh;
  z-index: 10;
}
</style>

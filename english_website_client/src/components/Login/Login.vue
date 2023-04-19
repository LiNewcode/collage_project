<template>
  <div class="login-des">
    <div >
      <p  class="login-des-en">In the south, after a rainy night in February</p>
      <p class="login-des-ch">南方二月雨夜</p>
      <p  class="login-des-en">spring will come on the next day</p>
      <p class="login-des-ch">天亮了会是春天</p>
      <p  class="login-des-en">I am young</p>
      <p class="login-des-ch">我很年轻</p>
      <p  class="login-des-en">so I won’t wear too many</p>
      <p class="login-des-ch">所以穿薄薄的衣服</p>
      <p  class="login-des-en">I will get up early</p>
      <p class="login-des-ch">我要早起</p>
      <p  class="login-des-en">I will be bouncy and full of energy to live</p>
      <p class="login-des-ch">我要充满活力地去呼吸</p>
    </div>

  </div>
  <div class="login-line"></div>
  <div class="ef-box">
    <div class="ef-title">Login<el-divider direction="vertical" ></el-divider><p>登&nbsp;&nbsp;陆</p></div>
  <el-form
      size="large"
      :model="form"
      status-icon
      :rules="rules"
      label-width="9vw"
      class="demo-ruleForm ef"
  >
    <video autoplay loop style="width:36vw;
    margin-left: -2vw;
  height:36vh;margin-top:-7vh;z-index:-1;position: absolute" ><source src="/Walking in the rain.mp4" type="video/mp4"></video>
    <el-form-item label="Confirm" prop="username">
      <el-input
          v-model="form.username"
          type="text"
          autocomplete="off"
      ></el-input>
    </el-form-item>
    <el-form-item label="Password" prop="pass">
      <el-input
          v-model="form.pass"
          type="password"
          autocomplete="off"
      ></el-input>
    </el-form-item>

    <el-form-item>
      <el-button type="primary" @click="login()"
      >Login</el-button
      >
        <el-button @click="register()">Turn to Register</el-button>
    </el-form-item>
  </el-form>
  </div>
</template>

<script >

export default {
  name: "Login",
  props: ['indexShow','userId'],
  emits: ['update:indexShow','update:userId'],
  data(){
    return{
      form:{
        username:'',
        pass:'',
      },
      rules:{
        username: [{ required: true, message: '请输入用户名', trigger: 'blur' }],
        pass: [{ required: true, message: '请输入密码', trigger: 'blur' }]

      }
    }
  },
  methods:{
    async login(){

      const res = await this.$http.get('/User/login', {
        params: {
          username: this.form.username,
          password: this.form.pass
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
              message: '登陆成功！'
            }
        )
        await this.set_cookie(data.id);
        this.$emit('update:userId', data.id)
        this.$emit('update:indexShow', '')
      }else {
        this.$message.error(
            {
              message: '登陆失败！'
            }
        )
      }
      console.log(res.data)
    },
    register(){
      this.$emit('update:indexShow', 'register')
    },
    get_cookie(){

    },
    async set_cookie(id){
      localStorage.setItem('username',this.form.username)
      localStorage.setItem('password',this.form.pass)
      localStorage.setItem('userId',id)
    },

  }
}



</script>

<style scoped lang="less">
.ef-box{
  width: 35vw;
  top:35vh;
  left: 15vw;
  height: 80vh;
  position: relative;
  .ef-title{
    font-size: 5vw;
    position: absolute;
    margin-top: -16vh;
    margin-left: -7vw;
    display: flex;
    flex-direction: row;
  p{
    //width: 2vh;
    //height: 15vh;
    font-size: 0.8vw;
    font-family: "Indie Flower";
    margin-top: -2vh;
    margin-left: 1vh;
    //word-wrap: break-word;/*英文的时候需要加上这句，自动换行*/
    /*自测了这句话没啥用*/
    //writing-mode: vertical-rl;/*从左向右 从右向左是 writing-mode: vertical-rl;*/
    writing-mode: tb-rl;/*IE浏览器的从左向右 从右向左是 writing-mode: tb-rl；*/
    text-align: center;
    padding:0px;
    display:flex;
    font-size: 1.4vw;
    -webkit-display:flex;
    flex-direction:column;
    /* align-content: center; */
    /* vertical-align: middle; */
    justify-content:center;
  }
  }
}
.ef{
  position: relative;
  //top:50vh;
  //left: 25vw;
  height: 28vh;
  padding-top: 7vh;
  padding-right: 5vw;
  width: 25vw;

  //margin-left: -15vw;
  //margin-top: -26vh;
  border-radius: 1vw;
  box-shadow: 0 0 2vw #eae8e8;
  border: 1px seashell solid;
  font-size: 1.5vw;
  overflow: hidden;
  color: white;
}
.login-des{
  margin-left: 10vw;
  margin-top: 15vh;
  display: flex;
  flex-direction: row;

  .login-des-ch{
    color: #c7c5c5;
  }
  .login-des-en{
    margin-top: 3vh;
    font-family: "Indie Flower";
    p{
      margin-top: 1vh;
    }
  }
}
.login-line{
  height: 70vh;
  margin-top: 15vh;
  border-left: 1px solid #d2d0d0;
  margin-left: 2vw;
  margin-right: 2vw;

}
</style>
<template>
  <div class="register-des">
    <div >
      <p  class="register-des-en">In the south, after a rainy night in February</p>
      <p class="register-des-ch">南方二月雨夜</p>
      <p  class="register-des-en">spring will come on the next day</p>
      <p class="register-des-ch">天亮了会是春天</p>
      <p  class="register-des-en">I am young</p>
      <p class="register-des-ch">我很年轻</p>
      <p  class="register-des-en">so I won’t wear too many</p>
      <p class="register-des-ch">所以穿薄薄的衣服</p>
      <p  class="register-des-en">I will get up early</p>
      <p class="register-des-ch">我要早起</p>
      <p  class="register-des-en">I will be bouncy and full of energy to live</p>
      <p class="register-des-ch">我要充满活力地去呼吸</p>
    </div>

  </div>
  <div class="register-line"></div>
  <div class="ef-box">
    <div class="ef-title">register<el-divider direction="vertical" ></el-divider><p>注&nbsp;&nbsp;册</p></div>
  <el-form
      size="large"
      :model="form"
      status-icon
      :rules="rules"
      label-width="9vw"
      class="demo-ruleForm ef"
  >
    <video autoplay loop style="width:38vw;
    margin-left: -2vw;
  height:48vh;margin-top:-11vh;z-index:-1;position: absolute" ><source src="/Walking in the rain.mp4" type="video/mp4"></video>
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
    <el-form-item label="Phone" prop="phone">
      <el-input
          v-model="form.phone"
          type="text"
          autocomplete="off"
      ></el-input>
    </el-form-item>

    <el-form-item>
      <el-button type="primary" @click="register()"
      >Register</el-button
      >
      <el-button @click="login()">Turn to Login</el-button>
    </el-form-item>
  </el-form>
  </div>
  <audio  style="display: none" autoplay><source src="/start.mp3" type="audio/mp3"></audio>
</template>

<script >
export default {
  name: "Register",
  props: ['indexShow','userId'],
  emits: ['update:indexShow','update:userId'],
  data(){
    return{
      form:{
        username:'',
        pass:'',
        phone:''
      },
      rules:{
        username: [{ required: true, message: '请输入用户名', trigger: 'blur' }],
        pass: [{ required: true, message: '请输入密码', trigger: 'blur' }],
        phone:[{ required: true, message: '请输入手机号', trigger: 'blur' }]
      }
    }
  },
  methods:{
    async  register(){
      const res = await this.$http.get('/User/register', {
        params: {
          username: this.form.username,
          password: this.form.pass,
          phone:this.form.phone
        },
        headers: {
          'Content-Type': 'text/plain;charset=UTF-8',
        },
      })
      // this.$emit('update:indexShow', '')

      let data = res.data
      if(data.state=='true'){
        this.$message.success(
            {
              message: '注册成功！跳转至登陆页面！'
            }
        )
        this.$emit('update:userId', data.id)
        this.$emit('update:indexShow', 'login')
      }else {
        this.$message.error(
            {
              message: '注册失败！'
            }
        )
      }
      // this.$emit('update:indexShow', 'login')
    },
    login(){
      this.$emit('update:indexShow', 'login')
    }
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
  //left: 35vw;
  height: 34vh;
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
.register-des{
  margin-left: 10vw;
  margin-top: 15vh;
  display: flex;
  flex-direction: row;

  .register-des-ch{
    color: #c7c5c5;
  }
  .register-des-en{
    margin-top: 3vh;
    font-family: "Indie Flower";
    p{
      margin-top: 1vh;
    }
  }
}
.register-line{
  height: 70vh;
  margin-top: 15vh;
  border-left: 1px solid #d2d0d0;
  margin-left: 2vw;
  margin-right: 2vw;

}
</style>
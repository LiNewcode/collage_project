import { createApp } from 'vue'
import axios from "axios";
import App from './App.vue'
import './index.css'
import Reader from "./components/reader/reader.vue";
import IndexPage from "./components/indexPage/indexPage.vue";
import Test from "./components/Test/Test.vue";
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
axios.defaults.baseURL = "http://127.0.0.1:5000/"
const app= createApp(App)
app.component('index-page',IndexPage)
app.component('reader',Reader)
app.component('test',Test)
app.use(ElementPlus)
app.config.globalProperties.$http = axios
app.mount('#app')


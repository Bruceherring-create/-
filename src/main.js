import { createApp } from 'vue'//这个就是vue3的版本
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'//引入app
import router from './router'
//引入echarts

import * as echarts from 'echarts'


const app=createApp(App).use(router).mount('#app')
app.use(ElementPlus)
app.echarts=echarts

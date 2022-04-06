// 创建一个Vue 应用
const app = Vue.createApp({})

// 定义一个名为 button-counter 的新全局组件
app.component('button-counter', {
data() {
return {
count: 0
}
},
template: `
<button @click="count++">
You clicked me {{ count }} times.
</button>`
})
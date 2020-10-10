import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import About from './views/About.vue'
import Fortune from './views/Fortune.vue'
import Char from './views/Char.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',
      component: About
    },
    {
        path: '/fortune',
        name: 'fortune',
        component: Fortune
      },
      {
        path: '/char',
        name: 'char',
        component: Char
      }
  ]
})
import { createRouter, createWebHistory } from 'vue-router'
// import HomeViewApp from '../views/HomeViewApp.vue'

const Home =() => import('../views/HomeViewApp.vue');
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path:'/',component: Home, name:'home' }
  ]
})

export default router

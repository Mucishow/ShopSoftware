import { createRouter, createWebHistory } from 'vue-router'
import ToValidate from '../views/ToValidate.vue'
import Validated  from '../views/Validated.vue'
import Crawler from '../views/Crawler.vue'

const routes = [
  {
    path: '/',
    name: 'ToValidate',
    component: ToValidate
  },
  {
    path: '/shop',
    name: 'Validated',
    component: Validated
  },
  {
    path: '/products/crawler',
    name: 'Crawler',
    component: Crawler
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

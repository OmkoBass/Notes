import { createRouter, createWebHashHistory } from 'vue-router'

import Home from '../views/Home.vue';
import Login from '../views/Login';
import Signup from '../views/Signup';
import About from '../views/About';
import CreateNote from "@/components/CreateNote";
import AllNotes from "@/components/AllNotes";

const routes = [
  {
    path: '',
    name: 'Home',
    component: Home,
    children: [
      {
        path: '',
        name: 'CreateNote',
        component: CreateNote,
      },
      {
        path: 'all',
        name: 'AllNotes',
        component: AllNotes,
      }
    ]
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/about',
    name: 'About',
    component: About
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router

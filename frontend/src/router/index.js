import Vue from 'vue';
import Router from 'vue-router';
import Login from "../pages/Login";
import NotFound from "../pages/404"

Vue.use(Router);

export default new Router({
  linkActiveClass: 'active',
  mode: 'history',
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '*',
      name: '404',
      component: NotFound
    }
  ]
});

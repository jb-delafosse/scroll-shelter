import Vue from 'vue'
import vuetify from './plugins/vuetify'
import App from "./App";
import router from './router';
import store from './store';


import GAuth from 'vue-google-oauth2'

const gauthOption = {
  clientId: '87641415248-t47sil8hkbrrfp514n6oh9avbvg3jrqv.apps.googleusercontent.com',
  scope: 'profile email',
  prompt: 'select_account'
}

Vue.use(GAuth, gauthOption)
Vue.config.productionTip = false

new Vue({
  vuetify,
  router,
  store: store,
  render: h => h(App)
}).$mount('#app')

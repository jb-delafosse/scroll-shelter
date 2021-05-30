import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import GAuth from 'vue-google-oauth2';


const gAuthOption = {
  clientId: '87641415248-t47sil8hkbrrfp514n6oh9avbvg3jrqv.apps.googleusercontent.com',
  scope: 'email',
  prompt: 'consent',
  fetch_basic_profile: true,
};

Vue.config.productionTip = false

Vue.use(GAuth, gAuthOption);

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')

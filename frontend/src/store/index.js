import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)


export const LOGIN_SUCCESS = "LOGIN_SUCCESS";
export const LOGIN_FAILED = "LOGIN_FAILED";

export default new Vuex.Store({
  state: {
    token: localStorage.getItem('user-token') || '',
    isLogged: localStorage.getItem('user-token') !== null,
    status: '',
    user: undefined,
  },
  mutations: {
    [LOGIN_SUCCESS]: (st, {token, user}) => {
    st.status = 'success';
    st.token = token;
    st.hasLoadedOnce = true;
    st.isLogged = true;
    st.user = user;
    },
    [LOGIN_FAILED]: (st) => {
    st.status = '';
    st.token = '';
    st.hasLoadedOnce = false;
    st.isLogged = false;
    st.user = undefined
    },
  },
  actions: {
    [LOGIN_SUCCESS]: ({ commit }, {token, user}) => new Promise(() => {
      commit(LOGIN_SUCCESS, {token, user});
    }),
    [LOGIN_FAILED]: ({ commit }) => new Promise(() => {
      commit(LOGIN_FAILED);
    }),
  },
  getters:{
    isAuthenticated: (st) => st.token
  },
  modules: {
  }
})

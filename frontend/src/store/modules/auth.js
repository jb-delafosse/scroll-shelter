import AuthService from '../../api/scroll-shelter/auth';

import {
  AUTH_REQUEST, AUTH_ERROR, AUTH_SUCCESS, AUTH_LOGOUT, SIGNUP_REQUEST, CONFIRM_INVITATION_REQUEST,
} from '../actions/auth';

const router = require('@/router');

const state = {
  token: localStorage.getItem('user-token') || '',
  role: localStorage.getItem('user-role') || '',
  isLogged: localStorage.getItem('user-token') !== null,
  status: '',
  hasLoadedOnce: false,
};

const getters = {
  isAuthenticated: () => state.token,
  isAdminOrOwner: () => state.role === 'admin' || state.role === 'owner',
  authStatus: () => state.status,
};

function jwtDecode(tokenString) {
  const token = { raw: tokenString, payload: {} };
  try {
    token.raw = tokenString;
    token.header = JSON.parse(window.atob(tokenString.split('.')[0]));
    token.payload = JSON.parse(window.atob(tokenString.split('.')[1]));
  } catch {
    console.log(`unable to decode '${tokenString}'`);
  }
  return (token);
}

function successResponse(commit, resolve, resp) {
  localStorage.setItem('user-token', resp.token);
  const token = jwtDecode(resp.token.substring(5));
  localStorage.setItem('user-role', token.payload.role);
  commit(AUTH_SUCCESS, token);
  resolve(resp);
}

function errorResponse(commit, reject, err) {
  commit(AUTH_ERROR, err);
  localStorage.removeItem('user-token');
  localStorage.removeItem('user-role');
  reject(err);
}

const actions = {
  [AUTH_REQUEST]: ({ commit }, user) => new Promise((resolve, reject) => {
    commit(AUTH_REQUEST);
    AuthService.auth(user)
      .then((resp) => successResponse(commit, resolve, resp))
      .catch((err) => errorResponse(commit, reject, err));
  }),
  [AUTH_LOGOUT]: ({ commit }) => new Promise((resolve) => {
    commit(AUTH_LOGOUT);
    localStorage.removeItem('user-token');
    localStorage.removeItem('user-role');
    const path = '/login';
    if (router.$route !== undefined && router.$route.path !== path) {
      router.push(path).catch(() => {});
    }
    resolve();
  }),
  [SIGNUP_REQUEST]: ({ commit }, user) => new Promise((resolve, reject) => {
    commit(SIGNUP_REQUEST);
    AuthService.signup(user)
      .then((resp) => successResponse(commit, resolve, resp))
      .catch((err) => errorResponse(commit, reject, err));
  }),
  [CONFIRM_INVITATION_REQUEST]: ({ commit }, user) => new Promise((resolve, reject) => {
    commit(CONFIRM_INVITATION_REQUEST);
    AuthService.confirm(user)
      .then((resp) => successResponse(commit, resolve, resp))
      .catch((err) => errorResponse(commit, reject, err));
  }),
};

const mutations = {
  [AUTH_REQUEST]: () => {
    state.status = 'loading';
  },
  [SIGNUP_REQUEST]: () => {
    state.status = 'loading';
  },
  [CONFIRM_INVITATION_REQUEST]: () => {
    state.status = 'loading';
  },
  [AUTH_SUCCESS]: (st, token) => {
    state.status = 'success';
    console.log(token.payload);
    console.log(token.payload.role);
    state.token = token.raw;
    state.role = token.payload.role;
    state.hasLoadedOnce = true;
    state.isLogged = true;
  },
  [AUTH_ERROR]: () => {
    state.status = 'error';
    state.hasLoadedOnce = true;
  },
  [AUTH_LOGOUT]: () => {
    state.token = '';
    state.isLogged = false;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};

/*
import axios from "axios";

export default{
  register_user(params){
    return axios.post( '/auth/register', params).then((response) => {console.log(response)
}, (error) => {
  console.log(error);
});
  },
  google_auth(){
    const params = {
      params: {
        authentication_backend: 'jwt',
        scopes: [
          'https://www.googleapis.com/auth/userinfo.profile',
          'https://www.googleapis.com/auth/userinfo.email',
          'https://www.googleapis.com/auth/drive.file'
        ]
      }
    };
    return axios.get('auth/google/authorize', params)
      .then((response) => {
        this.$router.replace(response.data.authorization_url)
      }, (error) => {console.log(error);});
  }

}
*/

const axios = require('axios');

export default class AuthService {
  static auth(token) {
    return axios
      .post('http://localhost:5000/api/v1/auth/signin', token)
      .then((res) => res.data)
      .catch((err) => Promise.reject(err.response));
  }

  static signup(token) {
    const params = {
      params: {
        authentication_backend: 'jwt',
        scopes: [
          'https://www.googleapis.com/auth/userinfo.profile',
          'https://www.googleapis.com/auth/userinfo.email',
          'https://www.googleapis.com/auth/drive.file'
        ]
      }
    };
    return axios
      .post('http://localhost:5000/api/v1/auth/signup', token)
      .then((res) => res.data)
      .catch((err) => Promise.reject(err.response));
  }

  static confirm(token) {
    return axios
      .post('http://localhost:5000/api/v1/auth/signup?confirm=true', token)
      .then((res) => res.data)
      .catch((err) => Promise.reject(err.response));
  }
}

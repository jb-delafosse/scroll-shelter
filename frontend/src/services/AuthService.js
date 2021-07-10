import qs from "qs";

const axios = require('axios');

export default class AuthService {
  authorization_url;
  static auth() {
    return axios
      .get('/auth/google/authorize',
        {
          params:{authentication_backend: "jwt", scopes: ["email","profile", "https://www.googleapis.com/auth/drive.file"]},
          paramsSerializer: params => { return qs.stringify(params, { arrayFormat: "repeat" }) }

        })
      .then(response => {
        window.location = response.data.authorization_url;
      })
      .catch((err) => Promise.reject(err.response));
  }
}

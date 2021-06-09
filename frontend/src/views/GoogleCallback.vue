<template>
  <v-main>
    <div v-if="!user">Authorizing ...</div>
    <div v-else>
      {{ user }}
    </div>
  </v-main>
</template>

<script>

import {LOGIN_FAILED, LOGIN_SUCCESS} from "../store";

export default {
  name: "GoogleCallback",
  data() {
    return {
      token: undefined,
      user: undefined
    };
  },
  created() {
    this.authorize();
  },
  methods: {
    getUser() {
      const headers = { Authorization: `Bearer ${this.token}` };
      this.$http
        .get("/users/me", { headers: headers })
        .then(response => {
          this.user = response.data;
          this.$store.dispatch(LOGIN_SUCCESS, {token: this.token, user: this.user})
          this.$router.replace("/")
        });
    },
    authorize() {
      const data = {
        state: this.$route.query.state,
        code: this.$route.query.code
      };
      this.$http
        .get("/auth/google/callback", {params:data})
        .then(async response => {
          this.token = response.data.access_token;
          console.log(this.token)
          this.getUser();
        })
        .catch(() => {
          this.$store.dispatch(LOGIN_FAILED)
          this.$router.replace("/login");
        });
    },
  }
};
</script>

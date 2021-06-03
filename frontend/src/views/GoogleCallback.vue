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
    authorize() {
      const data = {
        state: this.$route.query.state,
        code: this.$route.query.code
      };
      this.$http
        .get("/auth/google/callback", {params:data})
        .then(response => {
          this.token = response.data.access_token;
          this.getUser();
          this.$store.dispatch(LOGIN_SUCCESS, response.data.access_token)
          this.$router.replace("/")
        })
        .catch(() => {
          this.$store.dispatch(LOGIN_FAILED)
          this.$router.replace("/login");
        });
    },
    getUser() {
      const headers = { Authorization: `Bearer ${this.token}` };
      this.$http
        .get("/users/me", { headers: headers })
        .then(response => {
          this.user = response.data;
        });
    }
  }
};
</script>

<template>
  <v-main>
    <v-btn class="ma-2" color="primary" dark @click="loginWithGoogle">
      Login with google
      <v-icon dark right>
        mdi-account
      </v-icon>
    </v-btn>
  </v-main>
</template>

<script>

import AuthService from "../services/AuthService";

export default {
  name: "Login.vue",
  methods: {
     async loginWithGoogle() {
       await AuthService.auth()
    },
  }
}
</script>

<style scoped>

</style>

<template>
  <v-dialog v-model="dialog" persistent max-width="600px" min-width="360px">
      <div>
          <v-tabs v-model="tab" show-arrows background-color="primary" icons-and-text dark grow>
              <v-tabs-slider color="primary"></v-tabs-slider>
              <v-tab v-for="i in tabs" :key="i.name">
                  <v-icon large>{{ i.icon }}</v-icon>
                  <div class="caption py-1">{{ i.name }}</div>
              </v-tab>
              <v-tab-item>
                  <v-card class="px-4">
                      <v-card-text>
                          <v-form ref="loginForm" v-model="valid" lazy-validation>
                              <v-row>
                                  <v-col cols="12">
                                      <v-text-field v-model="loginEmail" :rules="loginEmailRules" label="E-mail" required></v-text-field>
                                  </v-col>
                                  <v-col cols="12">
                                      <v-text-field v-model="loginPassword" :append-icon="show1?'eye':'eye-off'" :rules="[rules.required, rules.min]" :type="show1 ? 'text' : 'password'" name="input-10-1" label="Password" hint="At least 8 characters" counter @click:append="show1 = !show1"></v-text-field>
                                  </v-col>
                                  <v-col class="d-flex" cols="12" sm="6" xsm="12">
                                  </v-col>
                                  <v-spacer></v-spacer>
                                  <v-col class="d-flex" cols="12" sm="3" xsm="12" align-end>
                                      <v-btn x-large block :disabled="!valid" color="success" @click="validate"> Login </v-btn>
                                  </v-col>
                              </v-row>
                          </v-form>
                      </v-card-text>
                  </v-card>
              </v-tab-item>
              <v-tab-item>
                  <v-card class="px-4">
                      <v-card-text>
                          <v-form ref="registerForm" v-model="valid" lazy-validation>
                              <v-row>
                                  <v-col cols="12">
                                      <v-text-field v-model="email" :rules="emailRules" label="E-mail" required></v-text-field>
                                  </v-col>
                                  <v-col cols="12">
                                      <v-text-field v-model="password" :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'" :rules="[rules.required, rules.min]" :type="show1 ? 'text' : 'password'" name="input-10-1" label="Password" hint="At least 8 characters" counter @click:append="show1 = !show1"></v-text-field>
                                  </v-col>
                                  <v-col cols="12">
                                      <v-text-field block v-model="verify" :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'" :rules="[rules.required, passwordMatch]" :type="show1 ? 'text' : 'password'" name="input-10-1" label="Confirm Password" counter @click:append="show1 = !show1"></v-text-field>
                                  </v-col>
                                  <v-col cols="12">
                                    <v-btn class="ma-2" @click.prevent="handleClickGetAuth">
                                      <svg xmlns="http://www.w3.org/2000/svg" width="30" height="18" viewBox="0 0 18 18" aria-hidden="true">
                                        <path fill="#4285F4" d="M17.64 9.2045c0-.6381-.0573-1.2518-.1636-1.8409H9v3.4814h4.8436c-.2086 1.125-.8427 2.0782-1.7959 2.7164v2.2581h2.9087c1.7018-1.5668 2.6836-3.874 2.6836-6.615z"></path><path fill="#34A853" d="M9 18c2.43 0 4.4673-.806 5.9564-2.1805l-2.9087-2.2581c-.8059.54-1.8368.859-3.0477.859-2.344 0-4.3282-1.5831-5.036-3.7104H.9574v2.3318C2.4382 15.9832 5.4818 18 9 18z"></path><path fill="#FBBC05" d="M3.964 10.71c-.18-.54-.2822-1.1168-.2822-1.71s.1023-1.17.2823-1.71V4.9582H.9573A8.9965 8.9965 0 0 0 0 9c0 1.4523.3477 2.8268.9573 4.0418L3.964 10.71z"></path><path fill="#EA4335" d="M9 3.5795c1.3214 0 2.5077.4541 3.4405 1.346l2.5813-2.5814C13.4632.8918 11.426 0 9 0 5.4818 0 2.4382 2.0168.9573 4.9582L3.964 7.29C4.6718 5.1627 6.6559 3.5795 9 3.5795z">
                                        </path>
                                      </svg>
                                      Login with Google
                                    </v-btn>
                                  </v-col>
                                  <v-spacer></v-spacer>
                                  <v-col class="d-flex ml-auto" cols="12" sm="3" xsm="12">
                                      <v-btn x-large block :disabled="!valid" color="success" @click="validate">Register</v-btn>
                                  </v-col>
                              </v-row>
                          </v-form>
                      </v-card-text>
                  </v-card>
              </v-tab-item>
          </v-tabs>
      </div>
  </v-dialog>
</template>


<script>
import ScrollShelterAuth from '../../api/scroll-shelter/auth'

export default {
    name: 'LoginModal',
  computed: {
    passwordMatch() {
      return () => this.password === this.verify || "Password must match";
    }
  },
  methods: {
    validate() {
      console.log("Salut")
      if (this.$refs.registerForm.validate()) {
        ScrollShelterAuth.register_user({
          email: this.email,
          password: this.password,
          is_active: true,
          is_superuser: false,
          is_verified: false
        })
      }
    },
    reset() {
      this.$refs.form.reset();
    },
    resetValidation() {
      this.$refs.form.resetValidation();
    },
    async handleClickGetAuth() {
      try {
        const authCode = await this.$gAuth.getAuthCode()
        const response = await this.$http.post('/auth/google/authorize', {code: authCode, redirect_uri: 'postmessage'})
        console.log(authCode)
        console.log(response)
      } catch (error) {
        // On fail do something
      }
    }
  },
  data: () => ({
    dialog: true,
    tab: 0,
    tabs: [
        {name:"Login", icon:"mdi-account"},
        {name:"Register", icon:"mdi-account-outline"}
    ],
    valid: true,
    email: "",
    password: "",
    verify: "",
    loginPassword: "",
    loginEmail: "",
    loginEmailRules: [
      v => !!v || "Required",
      v => /.+@.+\..+/.test(v) || "E-mail must be valid"
    ],
    emailRules: [
      v => !!v || "Required",
      v => /.+@.+\..+/.test(v) || "E-mail must be valid"
    ],
    show1: false,
    rules: {
      required: value => !!value || "Required.",
      min: v => (v && v.length >= 8) || "Min 8 characters"
    },
  })
};
</script>

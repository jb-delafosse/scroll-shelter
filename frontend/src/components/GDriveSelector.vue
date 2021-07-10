<template>
  <v-btn class="ma-2" color="primary" dark @click="driveIconClicked">
    Pick a file
    <v-icon dark right>
      mdi-account
    </v-icon>
  </v-btn>
</template>

<script>

export default {
  name: "GDriveSelector",
  methods: {
    async driveIconClicked() {
      console.log("Clicked");
      let gapi = window.gapi
      gapi.load("picker", () => {
        console.log("Picker Loaded");
        this.pickerApiLoaded = true;
        this.createPicker();
      });
    },
    createPicker() {
      let google = window.google
      console.log("Create Picker", google.picker);
      if (this.pickerApiLoaded  && this.$store.state.user.oauth_accounts[0].access_token) {
        var folderView = new google.picker.DocsView(google.picker.ViewId.FOLDERS)
          .setIncludeFolders(true)
          .setMimeTypes('application/vnd.google-apps.folder')
          .setSelectFolderEnabled(true);
        var picker = new google.picker.PickerBuilder()
          .enableFeature(google.picker.Feature.MULTISELECT_ENABLED)
          .addView(folderView)
          .setOAuthToken(this.$store.state.user.oauth_accounts[0].access_token)
          .setDeveloperKey("AIzaSyBaQZlYTmndQYCcdlkHoVtBzpZYandwaaA")
          .setCallback(this.pickerCallback)
          .build();
        picker.setVisible(true);
      }
    },
    async pickerCallback(data) {
      let google = window.google
      console.log("PickerCallback", data);
      if (data[google.picker.Response.ACTION] === google.picker.Action.PICKED) {
        // Array of Picked Files
        console.log("pouet");
      }
    }
  },
  mounted() {
    // eslint-disable-next-line no-unused-vars
    let script = document.createElement("script");
    script.setAttribute("type", "text/javascript");
    script.setAttribute("src", "https://apis.google.com/js/api.js");
    //script.onload = this.onloadCallback
    document.head.appendChild(script);
  },
  data() {
    return {
      pickerApiLoaded: false,
      developerKey: "AIzaSyBqLh86CdzjIscu0SOMogzR-TB011El1JM",
      clientId: "87641415248-t47sil8hkbrrfp514n6oh9avbvg3jrqv.apps.googleusercontent.com",
      scope: "https://www.googleapis.com/auth/drive.file",
    }
  },

}
</script>

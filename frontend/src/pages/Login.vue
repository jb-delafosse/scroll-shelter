<template>
  <main-layout>
    <LoginDialog/>
  </main-layout>
</template>


<script>
  import MainLayout from '../layouts/Main.vue'
  import LoginDialog from "../components/auth/LoginDialog";


  export default {
    components: {
      MainLayout,
      LoginDialog

    },
    data: () => ({
    //
  }),
  }
</script>

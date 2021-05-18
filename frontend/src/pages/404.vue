<template>
  <main-layout>
    <div class="v-responsive__content">
      <div class="d-flex align-center">
        <div class="row align-center">
          <div class="col">
            <span>
              <h1 class="text-h2 primary--text">Whoops, 404</h1>
              <p>Page not found</p>
            </span>
          </div>
        </div>
      </div>
    </div>
  </main-layout>
</template>

<script>
  import MainLayout from '../layouts/Main.vue'
  export default {
    components: {
      MainLayout
    }
  }
</script>

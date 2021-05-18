<template>
    <div class="main-container">
        <form>
            <div class="box-container">
                <SocialSignUp />
            </div>
        </form>
        <div class="footer">
            <p>Already have an account? <a href="/login"> Sign In</a></p>
        </div>
    </div>
</template>

<script>
import SocialSignUp from '@/components/SocialLogin'
export default {
  name: 'signup',
  components: {
    SocialSignUp
  }
}
</script>

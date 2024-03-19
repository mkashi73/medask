<template>
  <div class="h-100">
    <TopBar />
    <Navbar />
    <router-view></router-view>
    <Footer />
  </div>
</template>

<script>
import TopBar from "@/components/main/TopBar.vue";
import Navbar from "@/components/main/Navbar.vue";
import Footer from "@/components/main/Footer.vue";

export default {
  components: {
    TopBar,
    Navbar,
    Footer,
  },
};
</script>

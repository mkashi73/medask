<template>
  <div id="dashboardView" style="height: 100vh">
    <!-- <Topbar /> -->
    <Navbar />
    <Main />
    <Footer />
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
// import Topbar from "@/components/dashboard/Topbar.vue";
import Navbar from "@/components/dashboard/Navbar.vue";
import Main from "@/components/dashboard/Main.vue";
import Footer from "@/components/dashboard/Footer.vue";
import util from "@/util.js";

export default {
  components: {
    // Topbar,
    Navbar,
    Main,
    Footer,
  },
  mixins: [util],
  async mounted() {},
  computed: {
    ...mapGetters({
      hasPermission: "appData/hasPermission",
      getLoggedInUser: "appData/getLoggedInUser",
    }),
  },
};
</script>

<style lang="scss">
@import "@core/scss/vue/libs/vue-flatpicker.scss";
body::-webkit-scrollbar{
    display: none;
  }
</style>

<template>
  <div style="height: 7%">
    <div
      class="d-flex justify-content-center align-items-center h-100 bg-primary"
    >
      <b-link
        class="text-white my-nav-item my-nav-link d-flex align-items-center"
        :to="{ name: 'Home' }"
      >
        <b-img
          ref="logo"
          :src="require('@/assets/images/logo/logo.png')"
          width="30"
          height="30"
        ></b-img>
        <span style="font-size: large">HOME</span>
      </b-link>
      <b-link
        class="text-white my-nav-item my-nav-link d-flex align-items-center ml-3"
        :to="{ name: 'PMS' }"
      >
        <b-img
          ref="logo"
          :src="require('@/assets/images/logo/logo.png')"
          width="30"
          height="30"
        ></b-img>
        <span style="font-size: large">PMS</span>
      </b-link>
      <b-link
        class="text-white my-nav-item my-nav-link d-flex align-items-center ml-3"
        :to="{ name: 'HelpCen' }"
      >
        <b-img
          ref="logo"
          :src="require('@/assets/images/logo/logo.png')"
          width="30"
          height="30"
        ></b-img>
        <span style="font-size: large">Help Cen</span>
      </b-link>
      <b-link
        class="text-white my-nav-item my-nav-link d-flex align-items-center ml-3"
        :to="{ name: 'CI' }"
      >
        <b-img
          ref="logo"
          :src="require('@/assets/images/logo/logo.png')"
          width="30"
          height="30"
        ></b-img>
        <span style="font-size: large">C of I</span>
      </b-link>
      <b-link
        class="text-white my-nav-item my-nav-link d-flex align-items-center ml-3"
        :to="{ name: 'SIMS' }"
      >
        <b-img
          ref="logo"
          :src="require('@/assets/images/logo/logo.png')"
          width="30"
          height="30"
        ></b-img>
        <span style="font-size: large">Sims</span>
      </b-link>
      <b-link
        class="text-white my-nav-item my-nav-link d-flex align-items-center ml-3"
        :to="{ name: 'NOC' }"
      >
        <b-img
          ref="logo"
          :src="require('@/assets/images/logo/logo.png')"
          width="30"
          height="30"
        ></b-img>
        <span style="font-size: large">NOC</span>
      </b-link>
      <b-link
        class="text-white my-nav-item my-nav-link d-flex align-items-center ml-3"
        :to="{ name: 'eARMS' }"
      >
        <b-img
          ref="logo"
          :src="require('@/assets/images/logo/logo.png')"
          width="30"
          height="30"
        ></b-img>
        <span style="font-size: large">eARMS</span>
      </b-link>
      <b-link
        class="text-white my-nav-item my-nav-link d-flex align-items-center ml-3"
        :to="{ name: 'HMS' }"
      >
        <b-img
          ref="logo"
          :src="require('@/assets/images/logo/logo.png')"
          width="30"
          height="30"
        ></b-img>
        <span style="font-size: large">HMS</span>
      </b-link>
      <b-link
        class="text-white my-nav-item my-nav-link d-flex align-items-center ml-3"
        :to="{ name: 'CNE' }"
      >
        <b-img
          ref="logo"
          :src="require('@/assets/images/logo/logo.png')"
          width="30"
          height="30"
        ></b-img>
        <span style="font-size: large">CNE</span>
      </b-link>
      <b-link
        class="text-white my-nav-item my-nav-link d-flex align-items-center ml-3"
        :to="{ name: 'Misc' }"
      >
        <b-img
          ref="logo"
          :src="require('@/assets/images/logo/logo.png')"
          width="30"
          height="30"
        ></b-img>
        <span style="font-size: large">Misc</span>
      </b-link>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  components: {},
};
</script>

<style scoped>
.my-text {
  font-size: 24px !important;
}
</style>

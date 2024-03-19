<template>
  <b-container fluid style="background-color: #9cb3a5; height: 11%">
    <b-row
      class="mt-0 text-center p-50 my-border h-100"
      no-gutters
      align-v="center"
    >
      <b-col md="9" class="text-left d-flex align-items-center">
        <!-- <b-img
          ref="logo"
          :src="require('@/assets/images/logo/logo.png')"
          width="65"
          height="65"
        ></b-img>
        <div>
          <h1
            class="mb-0 ml-3 font-weight-bolder text-primary"
            style="color: white; font-size: 3rem"
          >
            Medical Tourism
          </h1>
        </div> -->
      </b-col>

      <b-col md="3" class="d-flex justify-content-end align-items-center">
        <div class="text-left"></div>
      </b-col>
    </b-row>
    <b-row>
      <div class="v-100"></div>
    </b-row>
  </b-container>
</template>
<script>
import moment from "moment";
export default {
  components: {
    moment,
  },
  mounted() {
    this.$refs.logo.classList.add("logo-animate");
  },
  beforeDestroy() {
    this.$refs.logo.classList.remove("logo-animate");
  },
  data() {
    return {
      currDate: null,
    };
  },
};
</script>

<style scoped>
.logo-animate {
  animation-name: logo-animation;
  animation-duration: 2s;
  animation-iteration-count: infinite;
  animation-direction: alternate;
}

@keyframes logo-animation {
  0% {
    transform: scale(1);
  }

  50% {
    transform: scale(1.1);
  }

  100% {
    transform: scale(1);
  }
}

@keyframes slideUp {
  from {
    transform: translateX(100%);
  }

  to {
    transform: translateX(-100%);
  }
}

.animation-container {
  overflow: hidden;
}

.survey-wrapper {
  animation: slideUp 20s linear infinite;
}
</style>

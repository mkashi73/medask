<template>
  <div style="height: 4%">
    <b-row
      class="h-100 bg-primary d-flex align-items-center justify-content-center"
    >
      <b-col class="md-4"> </b-col>
      <b-col class="md-4">
        <h6
          class="mb-0 text-center font-weight-bolder bg-primary text-white my-footer"
        >
          <span>Developed and Maintained by AG's Branch</span>
        </h6>
      </b-col>
      <b-col class="md-4"> </b-col>
    </b-row>
  </div>
</template>

<script>
import { mapActions } from "vuex";
import util from "@/util.js";
export default {
  data() {
    return {
      counter: "",
    };
  },
  mixins: [util],
  async mounted() {},
  methods: {
    ...mapActions({}),
  },
};
</script>

<style scoped>
.my-text {
  font-size: small !important;
}
.my-footer {
  font-size: medium;
}
</style>

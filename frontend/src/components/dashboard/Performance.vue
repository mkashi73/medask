<template>
  <b-card no-body class="h-100 m-0">
    <p class="font-weight-bolder m-0 text-center w-100 mt-50">Performance</p>
    <b-card-body class="h-100 p-50">
      <div class="border-primary h-100 overflow-auto">
        <b-list-group-item
          v-for="(item, index) in scores"
          :key="index"
          tag="li"
          class="p-50"
        >
          <div class="d-flex">
            <div class="ml-25 w-100">
              <b-card-text class="mb-0">
                <span class="font-weight-bold">Name:</span>
                {{ item.user_data.name }}
              </b-card-text>
              <small class="mb-0 d-block">
                <span class="font-weight-bold">Organization:</span>
                {{ item.user_data.organization }}
              </small>
              <small class="mb-0 d-block">
                <span class="font-weight-bold">Appointment:</span>
                {{ item.user_data.appointment }}
              </small>
              <small class="mb-0 d-block">
                <span class="font-weight-bold">Points:</span>
                {{ item.points }}
              </small>
            </div>
          </div>
        </b-list-group-item>
      </div>
    </b-card-body>
  </b-card>
</template>

<script>
import { mapActions } from "vuex";
import util from "@/util.js";

export default {
  mixins: [util],
  data() {
    return {
      scores: [],
    };
  },
  async mounted() {
    try {
      const res = await this.getPerformanceData();
      this.scores = res.data;
    } catch (error) {
      this.displayError(error);
    }
  },
  methods: {
    ...mapActions({
      getPerformanceData: "appData/getPerformanceData",
    }),
  },
};
</script>

<style></style>

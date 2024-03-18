<template>
  <b-row class="h-100" no-gutters>
    <b-col cols="12" class="h-100">
      <div class="h-50 d-flex">
        <b-card
          no-body
          class="h-100 m-0 font-weight-bolder text-center cursor-pointer w-50"
          @click="
            showComplaint({
              exceed_by_10_days: true,
            })
          "
        >
          <p class="font-weight-bolder m-0 text-center w-100 mt-50">
            Exceeded By 10 Days
          </p>
          <b-card-body
            class="py-50 d-flex align-items-center justify-content-center"
          >
            <span
              class="m-0 text-danger text-center font-weight-bolder my-font-size-lg"
            >
              {{ data.exceeds_10_days }}
            </span>
          </b-card-body>
        </b-card>
        <b-card
          no-body
          class="h-100 m-0 font-weight-bolder text-center cursor-pointer w-50 ml-50"
          @click="
            showComplaint({
              last_30_days: true,
            })
          "
        >
          <p class="font-weight-bolder m-0 text-center w-100 mt-50">
            Last 30 Days
          </p>
          <b-card-body
            class="py-50 d-flex align-items-center justify-content-center"
          >
            <span
              class="m-0 text-danger text-center font-weight-bolder my-font-size-lg"
            >
              {{ data.last_30_days }}
            </span>
          </b-card-body>
        </b-card>
      </div>
      <div class="h-50 pt-50 d-flex">
        <b-card
          no-body
          class="h-100 m-0 font-weight-bolder text-center cursor-pointer w-100 mr-50"
          @click="
            showComplaint({
              exceed_by_48_hrs: true,
            })
          "
        >
          <p class="font-weight-bolder m-0 text-center w-100 mt-50">
            Exceeded 48 Hrs Call
          </p>
          <b-card-body
            class="py-50 d-flex align-items-center justify-content-center"
          >
            <span
              class="m-0 text-danger text-center font-weight-bolder cursor-pointer my-font-size-lg"
            >
              {{ data.exceeds_48_hrs }}
            </span>
          </b-card-body>
        </b-card>
        <b-card
          no-body
          class="h-100 m-0 font-weight-bolder text-center cursor-pointer w-100"
          @click="
            showComplaint({
              delayed_by_48_hrs: true,
            })
          "
        >
          <p class="font-weight-bolder m-0 text-center w-100 mt-50">
            Delayed 48 Hrs Call
          </p>
          <b-card-body
            class="py-50 d-flex align-items-center justify-content-center"
          >
            <span
              class="m-0 text-danger text-center font-weight-bolder cursor-pointer my-font-size-lg"
            >
              {{ data.delayed_48_hrs }}
            </span>
          </b-card-body>
        </b-card>
      </div>
    </b-col>
  </b-row>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import moment from "moment";
import util from "@/util.js";

export default {
  mixins: [util],
  data() {
    return {
      data: {},
      filter: {},
    };
  },
  async mounted() {
    try {
      const res = await this.getStatisticsData();
      this.data = res.data;
    } catch (error) {
      this.displayError(error);
    }
  },
  methods: {
    ...mapActions({
      getStatisticsData: "appData/getStatisticsData",
    }),
    showComplaint({
      exceed_by_10_days,
      exceed_by_48_hrs,
      delayed_by_48_hrs,
      last_30_days,
    }) {
      this.filter = {};
      if (exceed_by_10_days) {
        this.filter.exceed_by_10_days = moment(new Date()).format("YYYY-MM-DD");
        this.filter.status = this.complaintStatus.PROCESSING;
      }
      if (exceed_by_48_hrs) {
        this.filter.exceed_by_48_hrs = moment(new Date()).format("YYYY-MM-DD");
        this.filter.status = this.complaintStatus.PROCESSING;
      }
      if (delayed_by_48_hrs) {
        this.filter.delayed_by_48_hrs = moment(new Date()).format("YYYY-MM-DD");
        this.filter.status = this.complaintStatus.PROCESSING;
      }
      if (last_30_days) {
        this.filter.last_30_days = moment(new Date()).format("YYYY-MM-DD");
      }
      this.filter.draft = false;
      this.$emit(
        "complaintShowModal",
        this.filter,
        this.showModalPlace.EXCEEDED
      );
    },
  },
  computed: {
    ...mapGetters({
      hasPermission: "appData/hasPermission",
      getLoggedInUser: "appData/getLoggedInUser",
    }),
  },
};
</script>

<style></style>

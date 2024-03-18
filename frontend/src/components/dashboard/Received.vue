<template>
  <b-row class="h-100" no-gutters>
    <b-col cols="6" class="h-100">
      <b-card
        no-body
        class="h-100 m-0 font-weight-bolder text-center mr-50 p-25"
      >
        <p class="font-weight-bolder m-0 text-center w-100">Received Today</p>
        <b-card-body class="h-100 p-0 pb-50">
          <div
            class="bg-warning text-white rounded h-50 d-flex align-items-center justify-content-center cursor-pointer my-font-size-lg"
            @click="
              showComplaint({
                today_process_complaint: true,
              })
            "
          >
            Processed:
            {{ data.today_process_complaint }}
          </div>
          <div
            class="bg-success text-white rounded h-50 d-flex align-items-center justify-content-center mt-50 cursor-pointer my-font-size-lg"
            @click="
              showComplaint({
                today_closed_complaint: true,
              })
            "
          >
            Closed:
            {{ data.today_closed_complaint }}
          </div>
        </b-card-body>
      </b-card>
    </b-col>
    <b-col cols="6" class="h-100">
      <b-card no-body class="h-100 m-0 font-weight-bolder text-center p-25">
        <p class="font-weight-bolder m-0 text-center w-100">Received Total</p>
        <b-card-body class="h-100 p-0 pb-50">
          <div
            class="bg-warning text-white rounded h-50 d-flex align-items-center justify-content-center cursor-pointer my-font-size-lg"
            @click="
              showComplaint({
                overall_process_complaint: true,
              })
            "
          >
            Processed:
            {{ data.overall_process_complaint }}
          </div>
          <div
            class="bg-success text-white rounded h-50 d-flex align-items-center justify-content-center mt-50 cursor-pointer my-font-size-lg"
            @click="
              showComplaint({
                overall_closed_complaint: true,
              })
            "
          >
            Closed:
            {{ data.overall_closed_complaint }}
          </div>
        </b-card-body>
      </b-card>
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
      today_closed_complaint,
      today_process_complaint,
      overall_closed_complaint,
      overall_process_complaint,
    }) {
      this.filter = {};
      if (today_closed_complaint) {
        this.filter.status = this.complaintStatus.CLOSED;
        this.filter.created_at = moment(new Date()).format("YYYY-MM-DD");
      }
      if (today_process_complaint) {
        this.filter.status = this.complaintStatus.PROCESSING;
        this.filter.created_at = moment(new Date()).format("YYYY-MM-DD");
      }
      if (overall_closed_complaint) {
        this.filter.status = this.complaintStatus.CLOSED;
      }
      if (overall_process_complaint) {
        this.filter.status = this.complaintStatus.PROCESSING;
      }
      this.filter.draft = false;
      this.$emit(
        "complaintShowModal",
        this.filter,
        this.showModalPlace.RECEIVED
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

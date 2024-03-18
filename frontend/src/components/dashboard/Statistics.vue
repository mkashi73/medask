<template>
  <b-row class="h-100" no-gutters>
    <b-col cols="4" class="h-100">
      <b-card no-body class="h-100 m-0 font-weight-bolder text-center">
        <p class="font-weight-bolder m-0 text-center w-100 mt-50">
          Today's Received
        </p>
        <b-card-body class="h-100 p-0 pb-50">
          <div
            class="bg-warning text-white rounded h-50 d-flex align-items-center justify-content-center cursor-pointer"
            @click="
              showComplaint({
                today_process_complaint: true,
              })
            "
          >
            Process:
            {{ data.today_process_complaint }}
          </div>
          <div
            class="bg-success text-white rounded h-50 d-flex align-items-center justify-content-center mt-50 cursor-pointer"
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
    <b-col cols="4" class="h-100 px-50">
      <div class="h-50">
        <b-card
          no-body
          class="h-100 m-0 font-weight-bolder text-center cursor-pointer"
          @click="
            showComplaint({
              exceed_by_10_days: true,
            })
          "
        >
          <p class="font-weight-bolder m-0 text-center w-100 mt-50">
            Exceed By 10 Days
          </p>
          <b-card-body
            class="py-50 d-flex align-items-center justify-content-center"
          >
            <p class="m-0 text-danger text-center font-weight-bolder">
              {{ data.exceeds_10_days }}
            </p>
          </b-card-body>
        </b-card>
      </div>
      <div class="h-50 pt-50 d-flex">
        <b-card
          no-body
          class="h-100 m-0 font-weight-bolder text-center cursor-pointer w-100 mr-50"
          @click="
            showComplaint({
              exceed_by_24_hrs: true,
            })
          "
        >
          <p class="font-weight-bolder m-0 text-center w-100 mt-50">
            Exceed 24 Hrs Call
          </p>
          <b-card-body
            class="py-50 d-flex align-items-center justify-content-center"
          >
            <p
              class="m-0 text-danger text-center font-weight-bolder cursor-pointer"
            >
              {{ data.exceeds_24_hrs }}
            </p>
          </b-card-body>
        </b-card>
        <b-card
          no-body
          class="h-100 m-0 font-weight-bolder text-center cursor-pointer w-100"
          @click="
            showComplaint({
              delayed_by_24_hrs: true,
            })
          "
        >
          <p class="font-weight-bolder m-0 text-center w-100 mt-50">
            Delayed 24 Hrs Call
          </p>
          <b-card-body
            class="py-50 d-flex align-items-center justify-content-center"
          >
            <p
              class="m-0 text-danger text-center font-weight-bolder cursor-pointer"
            >
              {{ data.delayed_24_hrs }}
            </p>
          </b-card-body>
        </b-card>
      </div>
    </b-col>
    <b-col cols="4" class="h-100">
      <b-card no-body class="h-100 m-0 font-weight-bolder text-center">
        <p class="font-weight-bolder m-0 text-center w-100">Total Received</p>
        <b-card-body class="h-100 p-0 pb-50">
          <div
            class="bg-warning text-white rounded h-50 d-flex align-items-center justify-content-center cursor-pointer"
            @click="
              showComplaint({
                overall_process_complaint: true,
              })
            "
          >
            Process:
            {{ data.overall_process_complaint }}
          </div>
          <div
            class="bg-success text-white rounded h-50 d-flex align-items-center justify-content-center mt-50 cursor-pointer"
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
      exceed_by_10_days,
      overall_closed_complaint,
      overall_process_complaint,
      exceed_by_24_hrs,
      delayed_by_24_hrs,
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
      if (exceed_by_10_days) {
        this.filter.exceed_by_10_days = moment(new Date()).format("YYYY-MM-DD");
        this.filter.status = this.complaintStatus.PROCESSING;
      }
      if (exceed_by_24_hrs) {
        this.filter.exceed_by_24_hrs = moment(new Date()).format("YYYY-MM-DD");
        this.filter.status = this.complaintStatus.PROCESSING;
      }
      if (delayed_by_24_hrs) {
        this.filter.delayed_by_24_hrs = moment(new Date()).format("YYYY-MM-DD");
        this.filter.status = this.complaintStatus.PROCESSING;
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
        this.showModalPlace.STATISTICS
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

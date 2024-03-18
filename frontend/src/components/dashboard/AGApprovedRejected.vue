<template>
  <b-row class="h-100" no-gutters>
    <b-col cols="6" class="h-100">
      <b-card no-body class="h-100 m-0 font-weight-bolder text-center p-25">
        <p class="font-weight-bolder m-0 text-center w-100">Finalized</p>
        <b-card-body class="h-100 p-0">
          <div
            class="
              bg-success
              text-white
              rounded
              h-100
              d-flex
              align-items-center
              justify-content-center
              cursor-pointer
              my-font-size-lg
            "
            @click="
              showComplaint({
                approved_complaint: true,
              })
            "
          >
            {{ data.finalized_complaint }}
          </div>
          <!-- <div
            class="bg-danger text-white rounded h-50 d-flex align-items-center justify-content-center mt-50 cursor-pointer my-font-size-lg"
            @click="
              showComplaint({
                rejected_complaint: true,
              })
            "
          >
            Rejected:
            {{ data.rejected_complaint }} 
          </div>-->
        </b-card-body>
      </b-card>
    </b-col>
    <b-col cols="6" class="h-100">
      <b-card no-body class="h-100 m-0 font-weight-bolder text-center p-25">
        <p class="font-weight-bolder m-0 text-center w-100">Disposed Call</p>
        <b-card-body class="h-100 p-0">
          <div
            class="
              bg-warning
              text-white
              rounded
              h-100
              d-flex
              align-items-center
              justify-content-center
              cursor-pointer
              my-font-size-lg
            "
            @click="
              showComplaint({
                after_approval_24_hrs: true,
              })
            "
          >
            {{ data.after_approval_24_hrs }}
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
    showComplaint({ approved_complaint, after_approval_24_hrs }) {
      this.filter = {};
      if (approved_complaint) {
        this.filter.status = this.complaintStatus.FINALIZED;
      }
      // if (rejected_complaint) {
      //   this.filter.final_approval = this.finalApproval.REJECTED;
      // }
      if (after_approval_24_hrs) {
        this.filter.after_approval_24_hrs = moment(new Date()).format(
          "YYYY-MM-DD"
        );
        this.filter.not_final_approval = this.finalApproval.DEFAULT;
      }
      this.filter.draft = false;
      this.$emit(
        "complaintShowModal",
        this.filter,
        this.showModalPlace.AG_APPROVED_REJECTED
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

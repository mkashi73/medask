<template>
  <b-card no-body class="h-100 m-0">
    <p class="font-weight-bolder m-0 text-center w-100 mt-50">
      Overall Complaint By Cat
    </p>
    <b-card-body class="h-100 p-50 overflow-auto">
      <b-table-simple hover bordered small caption-top>
        <b-thead>
          <b-tr>
            <b-th class="text-center my-font-size">Cat</b-th>
            <b-th class="text-center my-font-size">In Process</b-th>
            <b-th class="text-center my-font-size">Closed</b-th>
            <b-th class="text-center my-font-size">Total</b-th>
          </b-tr>
        </b-thead>
        <b-tbody>
          <b-tr v-for="(value, name, index) in data" :key="index" :style="{
            backgroundColor: rowClassCategoryHex(parseInt(name)),
          }">
            <b-th class="text-center my-font-size-lg text-white font-weight-bolder">{{ value.name }}
            </b-th>
            <b-td class="text-center my-font-size-lg text-white font-weight-bolder" @click="
              showComplaint({
                overall_process_complaint: true,
                category: parseInt(name),
              })
            ">{{ value.processing }}</b-td>
            <b-td class="text-center my-font-size-lg text-white font-weight-bolder" @click="
              showComplaint({
                overall_closed_complaint: true,
                category: parseInt(name),
              })
            ">{{ value.closed }}</b-td>
            <b-td class="text-center my-font-size-lg text-white font-weight-bolder" @click="
              showComplaint({
                category: parseInt(name),
              })
            ">{{ value.closed + value.processing }}</b-td>
          </b-tr>
        </b-tbody>
      </b-table-simple>
    </b-card-body>
  </b-card>
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
      overallIsServing: true,
    };
  },
  async mounted() {
    try {
      const res = await this.getOverallComplaintCatStatusPlot();
      this.data = res.data;
    } catch (error) {
      this.displayError(error);
    }
  },
  methods: {
    ...mapActions({
      getOverallComplaintCatStatusPlot: "appData/getOverallComplaintCatStatusPlot",
    }),
    showComplaint({
      overall_closed_complaint,
      overall_process_complaint,
      category,
    }) {
      this.filter = {};

      if (overall_closed_complaint) {
        this.filter.status = this.complaintStatus.CLOSED;
      }
      if (overall_process_complaint) {
        this.filter.status = this.complaintStatus.PROCESSING;
      }
      if (category) {
        this.filter.category = category;
      }
      this.filter.draft = false;
      this.$emit(
        "complaintShowModal",
        this.filter,
        this.showModalPlace.CAT_TABLE
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

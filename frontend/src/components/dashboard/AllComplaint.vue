<template>
  <b-card no-body class="h-100 m-0">
    <p class="font-weight-bolder m-0 text-center w-100 mt-50">All Complaints</p>
    <b-card-body class="h-100 p-50 overflow-auto d-flex align-items-center justify-content-center">
      <vue-apex-charts type="pie" :options="options" :series="series" width="100%" height="100%" />
    </b-card-body>
  </b-card>
</template>

<script>
import { mapActions } from "vuex";
import VueApexCharts from "vue-apexcharts";
import util from "@/util.js";

export default {
  components: {
    VueApexCharts,
  },
  mixins: [util],
  data() {
    return {
      series: [],
      options: {
        chart: {
          type: "pie",
        },
        legend: {
          show: true,
          position: "bottom",
        },
        responsive: [
          {
            options: {
              chart: {},
              legend: {
                show: false,
              },
            },
          },
        ],
      },
    };
  },
  async mounted() {
    try {
      const res = await this.getOverallComplaintCatPlot({
        isToday: false,
      });

      this.series = res.data.complaints;

      this.options = {
        ...this.options,
        labels: res.data.category_types,
        colors: this.categoryColorsHex,
      };
    } catch (error) {
      this.displayError(error);
    }
  },
  methods: {
    ...mapActions({
      getOverallComplaintCatPlot: "appData/getOverallComplaintCatPlot",
    }),
  },
};
</script>

<style></style>

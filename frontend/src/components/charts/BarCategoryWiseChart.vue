<template>
  <b-card no-body>
    <b-card-title class="mb-3 text-center"> Courses Statistics </b-card-title>
    <!-- <b-row class="mb-1" align-v="center">
      <b-input-group
        class="d-flex align-items-center"
      >
        <template #prepend>
          <feather-icon icon="CalendarIcon" size="16" />
        </template>
        <flat-pickr
          v-model="rangeDateStatus"
          :config="{ mode: 'range' }"
          @on-change="onStatusDateChange"
          class="
            form-control
            flat-picker
            bg-transparent
            border-0
            shadow-none
            my-font-size
            pr-0
            py-0
          "
          style="position: relative"
          placeholder="YYYY-MM-DD"
        />
      </b-input-group>
    </b-row> -->
    <b-card-body class="h-100 w-100">
      <vue-apex-charts
        v-if="render"
        type="bar"
        height="100%"
        :options="donutChart.chartOptions"
        :series="donutChart.chartOptions.series"
      />
    </b-card-body>
  </b-card>
</template>

<script>
import { BCard, BCardTitle, BCardSubTitle } from "bootstrap-vue";
// import flatPickr from "vue-flatpickr-component";

import VueApexCharts from "vue-apexcharts";
import { mapActions } from "vuex";
import moment from "moment";

export default {
  components: {
    VueApexCharts,
    BCard,
    BCardTitle,
    BCardSubTitle,
    // flatPickr,
  },
  data() {
    return {
      render: false,
      // startDate: moment(new Date()).subtract(1, "d").format("YYYY-MM-DD"),
      // endDate: moment(new Date()).add(1, "d").format("YYYY-MM-DD"),
      // rangeDateStatus: `${moment(new Date())
      //   .subtract(5, "d")
      //   .format("YYYY-MM-DD")} to ${moment(new Date())
      //   .add(5, "d")
      //   .format("YYYY-MM-DD")}`,
      // startDateStatus: moment(new Date()).subtract(2, "d").format("YYYY-MM-DD"),
      // endDateStatus: moment(new Date()).add(1, "d").format("YYYY-MM-DD"),
      donutChart: {
        series: [],
        chartOptions: {
          series: [],
          chart: {
            type: "bar",
            height: 350,
            stacked: true,
            stackType: "100%",
          },
          responsive: [
            {
              breakpoint: 480,
              options: {
                legend: {
                  position: "bottom",
                  offsetX: -10,
                  offsetY: 0,
                },
              },
            },
          ],
          xaxis: {
            categories: [],
          },
          dataLabels: {
            enabled: true,
            
          },
          fill: {
            opacity: 1,
          },
          legend: {
            position: "right",
            offsetX: 0,
            offsetY: 50,
          },
        },
      },
    };
  },
  async mounted() {
    await this.apiCall();
  },
  methods: {
    ...mapActions({
      getCourseWiseState: "appData/getCourseWiseState",
    }),
    async apiCall(e) {
      try {
        const res = await this.getCourseWiseState();
        console.log("RESSS: ", res.data);
        // this.donutChart.chartOptions.labels = res.data.status_types;

        // this.donutChart.series.name = res.data.status_types;
        // this.donutChart.series[0].data = res.data.count;
        this.donutChart.chartOptions.series = res.data.data;
        console.log(
          "donutChart.chartOptions.series - ",
          this.donutChart.chartOptions.series
        );
        this.donutChart.chartOptions.xaxis.categories = res.data.courses;
        console.log(
          "donutChart.chartOptions.xaxis.categories - ",
          this.donutChart.chartOptions.xaxis.categories
        );
        this.render = true;
      } catch (error) {
        console.log("Society Plot Error:", error);
      }
    },

    // async onStatusDateChange(range) {
    //   // this.render = false;
    //   if (range.length > 1) {
    //     this.startDateStatus = moment(range[0]).format("YYYY-MM-DD");
    //     this.endDateStatus = moment(range[1]).format("YYYY-MM-DD");

    //     await this.nocBySocietyPlot()

    //   }
    // },
  },
};
</script>

<template>
  <b-card no-body>
    <b-card-title class="mb-3 text-center"> Category Wise </b-card-title>

    <b-card-body class="h-100 w-100">
      <vue-apex-charts
        v-if="render"
        type="donut"
        height="100%"
        :options="donutChart.chartOptions"
        :series="donutChart.series"
      />
    </b-card-body>
  </b-card>
</template>


<script>
import { BCard, BCardTitle, BCardSubTitle } from "bootstrap-vue";

import VueApexCharts from "vue-apexcharts";
import { mapActions } from "vuex";
import moment from "moment";

export default {
  components: {
    VueApexCharts,
    BCard,
    BCardTitle,
    BCardSubTitle,
  },
  data() {
    return {
      render: false,
      startDate: moment(new Date()).subtract(1, "d").format("YYYY-MM-DD"),
      endDate: moment(new Date()).add(1, "d").format("YYYY-MM-DD"),
      donutChart: {
        series: [85, 16, 50, 50],
        chartOptions: {
          legend: {
            show: true,
            position: "bottom",
            fontSize: "14px",
            fontFamily: "Montserrat",
          },

          dataLabels: {
            enabled: true,
            formatter(val) {
              // eslint-disable-next-line radix
              return `${parseInt(val)}%`;
            },
          },
          plotOptions: {
            pie: {
              donut: {
                labels: {
                  show: true,
                  name: {
                    fontSize: "1rem",
                    fontFamily: "Montserrat",
                  },
                  value: {
                    fontSize: "1rem",
                    fontFamily: "Montserrat",
                    formatter(val) {
                      // eslint-disable-next-line radix
                      return `${parseInt(val)} NOCs`;
                    },
                  },
                },
              },
            },
          },
          labels: ["Operational", "Networking", "Hiring", "R&D"],
          responsive: [
            {
              breakpoint: 992,
              options: {
                chart: {
                  height: 380,
                },
                legend: {
                  position: "bottom",
                },
              },
            },
            {
              breakpoint: 576,
              options: {
                chart: {
                  height: 320,
                },
                plotOptions: {
                  pie: {
                    donut: {
                      labels: {
                        show: true,
                        name: {
                          fontSize: "1.5rem",
                        },
                        value: {
                          fontSize: "1rem",
                        },
                        total: {
                          fontSize: "1.5rem",
                        },
                      },
                    },
                  },
                },
                legend: {
                  show: true,
                },
              },
            },
          ],
        },
      },
    };
  },
  async mounted() {
    await this.nocBySocietyPlot();
  },
  methods: {
    ...mapActions({
      getRFACatPlot: "appData/getRFACatPlot",
    }),
    async nocBySocietyPlot(e) {
      // console.log("start: ", this.startDate, ' - ', "end: ", this.endDate)
      try {
        const res = await this.getRFACatPlot({
          start_date: this.startDate,
          end_date: this.endDate,
        });
        // console.log ("RES ", res.data.count);
        this.donutChart.chartOptions.labels = res.data.status_types;

        this.donutChart.series = res.data.count;
        // this.donutChart.series = [12,1,4,5,7,8];

        this.render = true;
      } catch (error) {
        console.log("Society Plot Error:", error);
      }
    },
  },
};
</script>
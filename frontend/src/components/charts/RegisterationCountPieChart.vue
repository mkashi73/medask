<template>
  <b-card no-body class="mb-0">
    <!-- <b-card-title class="mb-3 text-center">
      No. of Registerations
    </b-card-title> -->
    <b-card-body class="h-100 w-100">
      <vue-apex-charts
        v-if="render"
        type="pie"
        :options="donutChart.chartOptions"
        :series="donutChart.series"
      />
    </b-card-body>
  </b-card>
</template>

<script>
import { BCard, BCardTitle, BCardSubTitle } from "bootstrap-vue";

import { $themeColors } from "@themeConfig";
import VueApexCharts from "vue-apexcharts";
import { mapActions } from "vuex";
export default {
  components: {
    VueApexCharts,
    BCard,
    BCardTitle,
    BCardSubTitle,
  },
  data() {
    return {
      render: true,
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
            // pie: {
            //   donut: {
            //     labels: {
            //       show: true,
            //       name: {
            //         fontSize: "1rem",
            //         fontFamily: "Montserrat",
            //       },
            //       value: {
            //         fontSize: "1rem",
            //         fontFamily: "Montserrat",
            //         formatter(val) {
            //           // eslint-disable-next-line radix
            //           return `${parseInt(val)} Candidates`;
            //         },
            //       },
            //     },
            //   },
            // },
          },
          labels: ["ASRC Rwp", "ASRC Fsd", "ASRC Lhr", "ASRC Lhr"],
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
  async mounted() {},
  methods: {
    ...mapActions({}),
  },
};
</script>

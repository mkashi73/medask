<template>
  <b-card no-body>
    <b-card-title class="mb-3 text-center">
      ASRC Wise
    </b-card-title>
    
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
import {
  BCard, BCardTitle, BCardSubTitle,
} from 'bootstrap-vue'

import { $themeColors } from "@themeConfig";
import VueApexCharts from 'vue-apexcharts'
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
      center_counts: null,
      center_names: null,
      render: false,
      donutChart: {
        // series: [85, 16, 50, 50],
        series: [],
        chartOptions: {
          colors: [
            '#836AF9', // primaryColorShade
            '#28dac6', // successColorShade
            // '#ffe802', // warningColorShade
            '#ffe800', // yellowColor
            '#2c9aff', // blueColor
            '#FF8C00', // Dark Orange
            '#ff4961', // lineChartDangercolors
            '#FF4500', // Orange Red
            '#32CD32', // Lime Green
            '#4169E1', // Royal Blue
            '#8A2BE2', // Blue Violet
          ],
          legend: {
            show: true,
            position: 'bottom',
            fontSize: '14px',
            fontFamily: 'Montserrat',
          },
          
          dataLabels: {
            enabled: true,
            formatter(val) {
              // eslint-disable-next-line radix
              return `${parseInt(val)}%`
            },
          },
          plotOptions: {
            pie: {
              donut: {
                labels: {
                  show: true,
                  name: {
                    fontSize: '1rem',
                    fontFamily: 'Montserrat',
                  },
                  value: {
                    fontSize: '1rem',
                    fontFamily: 'Montserrat',
                    formatter(val) {
                      // eslint-disable-next-line radix
                      return `${parseInt(val)} Candidates`
                    },
                  },
                  
                },
              },
            },
          },
          // labels: [],
          labels: ["ASRC RWP", "ASRC MZD", "ASRC LHR", "ASRC FSD", "ASRC PSC", "ASRC QTA", "ASRC KCI", "ASRC MTN", "ASRC HYD", "ASRC GLT", "ASRC DIK", "ASRC PQL", "ASRC KZD"],
          responsive: [
            {
              breakpoint: 992,
              options: {
                chart: {
                  height: 380,
                },
                legend: {
                  position: 'bottom',
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
                          fontSize: '1.5rem',
                        },
                        value: {
                          fontSize: '1rem',
                        },
                        total: {
                          fontSize: '1.5rem',
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
    }
  },
   async mounted() {
    await this.regCountCenterWise();
  },
  methods: {
    ...mapActions({
      getCenterWiseRegCounts: "appData/getCenterWiseRegCounts",
    }),
    async regCountCenterWise(e) {
      try {
        const res = await this.getCenterWiseRegCounts();
        this.center_names = res.data.center_names;
        this.center_counts = res.data.center_counts;
        this.donutChart.chartOptions.labels = res.data.center_names;

        this.donutChart.series = res.data.center_counts;

        console.log('center_names :', res.data.center_names)
        console.log('center_counts :', res.data.center_counts)

        this.render = true;
      
      } catch (error) {
        console.log("Society Plot Error:", error);
      }
    },
  }
}
</script>
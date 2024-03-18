<template>
  <div style="height: 88%" class="bg-primary py-50 px-50">
    <b-row class="h-100" no-gutters>
      <b-col cols="3" class="h-100 bg-white rounded border border-light">
        <p class="font-weight-bolder m-0 text-center w-100 mt-1">
          Course-wise Registration
        </p>
        <vue-apex-charts
          v-if="render_one"
          type="bar"
          width="95%"
          height="95%"
          :key="courseCenterCountKey"
          :options="courseCenterCountOptions"
          :series="courseCenterCountSeries"
        />
      </b-col>
      <b-col cols="6" class="h-100 pl-50 pr-50">
        <b-row style="height: 35%" no-gutters>
          <b-col cols="4" class="h-100">
            <b-card no-body class="h-100 m-0 border border-light">
              <p
                class="font-weight-bolder m-0 text-center w-100 mt-1"
                style="font-size: 17px"
              >
                Registrations Today -
                <strong v-if="overallCounts!=null" style="color: red">{{overallCounts.today_reg}}</strong>
              </p>
              <b-card-body>
                <b-row class="mb-2">
                  <b-col md="6" class="text-center h-100 ">
                    <b-avatar size="60" variant="primary" class="mb-0">
                      <feather-icon
                        size="30"
                        icon="CheckCircleIcon"
                        class="cursor-pointer"
                      />
                    </b-avatar>
                    <p
                      class="font-weight-bolder mb-0 text-primary"
                      style="font-size: 12px"
                    >
                      Approved
                    </p>
                    <p
                      class="mb-0 font-weight-bolder text-primary"
                      style="font-size: 12px"
                      v-if="overallCounts!=null"
                    >
                      {{ overallCounts.today_appr }}
                    </p>
                  </b-col>
                  <b-col md="6" class="text-center h-100">
                    <b-avatar size="60" variant="info" class="mb-0">
                      <feather-icon
                        size="30"
                        icon="XCircleIcon"
                        class="cursor-pointer"
                      />
                    </b-avatar>
                    <p
                      class="font-weight-bolder mb-0 text-info"
                      style="font-size: 12px"
                    >
                      Rejected
                    </p>
                    <p
                      class="mb-0 font-weight-bolder text-info"
                      style="font-size: 12px"
                      v-if="overallCounts!=null"
                    >
                      {{ overallCounts.today_rej }}
                    </p>
                  </b-col>
                </b-row>
                <b-row class="h-0">
                  <b-col md="12" class="text-center h-100">
                    <b-avatar size="60" variant="warning" class="mb-50">
                      <feather-icon
                        size="30"
                        icon="LoaderIcon"
                        class="cursor-pointer"
                      />
                    </b-avatar>
                    <p class="font-weight-bolder m-0 text-warning"  style="font-size: 12px">
                      Pending
                    </p>
                    <p
                      class="mb-0 font-weight-bolder text-warning"
                      style="font-size: 12px"
                      v-if="overallCounts!=null"
                    >
                      {{ overallCounts.today_pen }}
                    </p>
                  </b-col>
                </b-row>
              </b-card-body>
            </b-card>
          </b-col>
          <b-col
            cols="4"
            class="h-100 text-center"
            style="padding-left: 7px; padding-right: 7px"
          >
            <div
              class="
                border
                h-100
                rounded
                border-light
                d-flex
                justify-content-center
                align-items-center
              "
              style="background-color: #E4E4D0"
            >
              <b-img :src="this.appLogoImage" alt="logo" height="130" />
            </div>
          </b-col>
          <b-col cols="4" class="h-100">
            <b-card no-body class="h-100 m-0">
              <p
                class="font-weight-bolder m-0 text-center w-100 mt-1"
                style="font-size: 17px"
              >
                Registrations Total -
                <strong v-if="overallCounts!=null" style="color: red">{{ overallCounts.total_reg }}</strong>
              </p>
              <b-card-body>
                <b-row>
                  <b-col md="6" class="text-center h-100">
                    <b-avatar size="60" variant="primary" class="mb-0">
                      <feather-icon
                        size="30"
                        icon="CheckCircleIcon"
                        class="cursor-pointer"
                      />
                    </b-avatar>
                    <p
                      class="font-weight-bolder m-0 text-primary"
                      style="font-size: 12px"
                    >
                      Approved
                    </p>
                    <p
                      class="m-0 font-weight-bolder text-primary"
                      style="font-size: 12px"
                      v-if="overallCounts!=null"
                    >
                      {{ overallCounts.total_appr }}
                    </p>
                  </b-col>
                  <b-col md="6" class="text-center h-100">
                    <b-avatar size="60" variant="info" class="mb-0">
                      <feather-icon
                        size="30"
                        icon="XCircleIcon"
                        class="cursor-pointer"
                      />
                    </b-avatar>
                    <p
                      class="font-weight-bolder mb-0 text-info"
                      style="font-size: 12px"
                    >
                      Rejected
                    </p>
                    <p
                      class="mb-0 font-weight-bolder text-info"
                      style="font-size: 12px"
                      v-if="overallCounts!=null"
                    >
                      {{ overallCounts.total_rej }}
                    </p>
                  </b-col>
                </b-row>
                <b-row>
                  <b-col md="12" class="text-center">
                    <b-avatar size="60" variant="warning" class="mb-0">
                      <feather-icon
                        size="30"
                        icon="LoaderIcon"
                        class="cursor-pointer"
                      />
                    </b-avatar>
                    <p
                      class="font-weight-bolder mb-0 text-warning"
                      style="font-size: 12px"
                    >
                      Pending
                    </p>
                    <p
                      class="m-0 font-weight-bolder text-warning"
                      style="font-size: 12px"
                      v-if="overallCounts!=null"
                    >
                      {{ overallCounts.total_pen }}
                    </p>
                  </b-col>
                </b-row>
              </b-card-body>
            </b-card>
          </b-col>
        </b-row>
        <b-row style="padding: 2px; height: 63.5%" no-gutters>
          <b-card no-body class="h-100 w-100 mt-1">
            <bar-category-wise-chart
              class="
                p-1
                h-100
                w-100
                d-flex
                align-items-center
                justify-content-center
              "
            />
            
          </b-card>
        </b-row>
      </b-col>
      <b-col cols="3" class="h-100">
        <b-row class="h-50" style="padding-bottom: 4px" no-gutters>
          <b-col class="h-100">
            <society-wise-chart
              class="
                h-100
                w-100
                d-flex
                align-items-center
                justify-content-center
              "
            />
          </b-col>
        </b-row>
        <b-row class="h-50" style="padding-top: 4px" no-gutters>
          <b-col cols="12" class="h-100">
            <b-card no-body class="h-100 m-0 p-50">
              <b-row no-gutters align-v="center">
                <b-col md="9" class="px-50">
                  <swiper
                    class="swiper-centered-slides-2 mx-3"
                    :options="swiperOptions"
                    :slides-per-view="3"
                  >
                    <h5>No. of Registrations</h5>
                    
                  </swiper>                  
                </b-col>
                <b-col cols="3" class="pl-50">
                  <b-input-group
                    class="d-flex align-items-center"
                    v-if="rfaPlot === 1"
                  >
                    <template #prepend>
                      <feather-icon icon="CalendarIcon" size="16" />
                    </template>
                    <flat-pickr
                      v-model="rangeDate"
                      :config="{ mode: 'range' }"
                      @on-change="onDateChange"
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
                  
                  <b-form-radio-group
                    id="isTodayRFACat"
                    size="sm"
                    v-model="isTodayRFACat"
                    v-if="rfaPlot === 2"
                    @change="rfaCatPlot"
                    name="isTodayRFACat"
                    :key="rfaCatPlotKey"
                  >
                    <b-input-group
                      class="d-flex align-items-center"
                      v-if="rfaPlot === 2"
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
                  </b-form-radio-group>
                  <b-form-radio-group
                    id="isTodayRFAType"
                    size="sm"
                    v-model="isTodayRFAType"
                    v-if="rfaPlot === 6"
                    @change="rfaTypePlot"
                    name="isTodayRFAType"
                    :key="rfaTypePlotKey"
                  >
                    <b-form-radio
                      v-model="isTodayRFAType"
                      :value="true"
                      class="p-0 mr-2"
                    >
                      Today
                    </b-form-radio>
                    <b-form-radio
                      v-model="isTodayRFAType"
                      :value="false"
                      class="p-0"
                    >
                      Overall
                    </b-form-radio>
                  </b-form-radio-group>
                </b-col>
              </b-row>
              <b-row class="h-100" no-gutters>
                <b-col class="h-100">
                  <vue-apex-charts
                    type="area"
                    width="100%"
                    height="100%"
                    :key="noRFAPlotKey"
                    :options="noRFAPlotOptions"
                    :series="noRFAPlotSeries"
                    v-if="rfaPlot === 1"
                  />
                 
                </b-col>
              </b-row>
            </b-card>
          </b-col>
        </b-row>
      </b-col>
    </b-row>
    <!-- <noc-circulation-modal
      :petition="petitions"
      @modalClosed="onModalClosed"
      :key="`edit-${petitionCirculationModalCount}`"
    /> -->
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import VueApexCharts from "vue-apexcharts";
import { $themeColors } from "@themeConfig";
import flatPickr from "vue-flatpickr-component";
import moment from "moment";
import VuePerfectScrollbar from "vue-perfect-scrollbar";
import { Swiper, SwiperSlide } from "vue-awesome-swiper";
import CityWiseChart from "../charts/CityWiseChart.vue";
import SocietyWiseChart from "../charts/SocietyWiseChart.vue";
import CategoryWiseChart from "../charts/CategoryWiseChart.vue";
import BarCategoryWiseChart from "../charts/BarCategoryWiseChart.vue";
import PolarAreaChart from "../charts/PolarAreaChart.vue";
import util from "@/util.js";
import "swiper/css/swiper.css";
import { $themeConfig } from "@themeConfig";

export default {
  components: {
    VueApexCharts,
    VuePerfectScrollbar,
    flatPickr,
    Swiper,
    SwiperSlide,
    CityWiseChart,
    PolarAreaChart,
    SocietyWiseChart,
    CategoryWiseChart,
    BarCategoryWiseChart,
  },
  mixins: [util],
  data() {
    return {
      render_one: false,
      render_two: false,
      render_three: false,
      appLogoImage: "",
      data: {},
      perfectScrollbarSettings: {
        maxScrollbarLength: 150,
        wheelPropagation: false,
        useBothWheelAxes: false,
        suppressScrollX: true,
      },
      overallCounts: null,
      swiperOptions: {
        slidesPerView: "auto",
        centeredSlides: true,
        spaceBetween: 30,
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
        },
      },
      rangeDateStatus: `${moment(new Date())
        .subtract(5, "d")
        .format("YYYY-MM-DD")} to ${moment(new Date())
        .add(5, "d")
        .format("YYYY-MM-DD")}`,
      startDateStatus: moment(new Date()).subtract(2, "d").format("YYYY-MM-DD"),
      endDateStatus: moment(new Date()).add(1, "d").format("YYYY-MM-DD"),

      rangeDate: `${moment(new Date())
        .subtract(5, "d")
        .format("YYYY-MM-DD")} to ${moment(new Date())
        .add(5, "d")
        .format("YYYY-MM-DD")}`,
      startDate: moment(new Date()).subtract(5, "d").format("YYYY-MM-DD"),
      endDate: moment(new Date()).add(5, "d").format("YYYY-MM-DD"),

      noRFAPlotSeries: [
        {
          data: [20, 25, 30, 35, 40, 50, 60],
        },
      ],
      noRFAPlotOptions: {
        chart: {
          toolbar: {
            show: false,
          },
        },
        markers: {
          strokeWidth: 4,
          strokeOpacity: 0.7,
          strokeColors: [$themeColors.light],
          colors: [$themeColors.primary],
        },
        colors: [$themeColors.primary],
        dataLabels: {
          enabled: false,
        },
        stroke: {
          show: true,
          colors: [$themeColors.primary],
        },
        grid: {
          xaxis: {
            lines: {
              show: true,
            },
          },
        },
        tooltip: {
          custom(data) {
            return `${'<div class="px-1 py-50"><span>'}${
              data.series[data.seriesIndex][data.dataPointIndex]
            }</span></div>`;
          },
        },
        xaxis: {
          categories: [],
        },
      },
      courseCenterCountSeries:[],
      courseCenterCountOptions: {
        chart: {
          stacked: true,
          toolbar: {
            show: true,
          },
        },
        plotOptions: {
          bar: {
            horizontal: true,
            barHeight: "70%",
            // endingShape: "null",
          },

          colors: $themeColors.primary,
        },
        dataLabels: {
          enabled: true,
          position: "center",
          total: {
            enabled: true,
            offsetX: 0,
            style: {
              colors:["#00000"],
              fontSize: '13px',
              fontWeight: "bold"
            },
          },
          style:{
            color:"#000000",
            fontSize: "12px", 
            fontWeight: "bolder",
          }
        },
        legend: {
          show: true,
          position: 'top'
        },
        stroke: {
          show: true,
          width: 1,
          colors: ["transparent"],
        },
        grid: {
          xaxis: {
            lines: {
              show: false,
            },
          },
        },
        xaxis: {
          categories: [],
        },
        fill: {
          opacity: 1,
        },
      },
      rfaCatPlotSeries: [
        {
          data: [85, 100, 30, 40, 95, 90, 30, 110, 62, 20],
        },
      ],
      rfaCatPlotOptions: {
        chart: {
          stacked: true,
          toolbar: {
            show: false,
          },
        },
        plotOptions: {
          bar: {
            columnWidth: "15%",
          },
        },
        dataLabels: {
          enabled: false,
        },
        legend: {
          show: true,
        },
        stroke: {
          show: true,
          colors: [$themeColors.light],
        },
        grid: {
          xaxis: {
            lines: {
              show: true,
            },
          },
        },
        xaxis: {
          categories: [],
        },
        fill: {
          opacity: 1,
        },
      },
      rfaTypePlotSeries: [
        {
          data: [99, 99, 99, 99, 99, 99, 99, 99, 99, 99],
        },
      ],
      rfaTypePlotOptions: {
        chart: {
          stacked: true,
          toolbar: {
            show: false,
          },
        },
        plotOptions: {
          bar: {
            columnWidth: "15%",
          },
        },
        dataLabels: {
          enabled: false,
        },
        legend: {
          show: true,
        },
        stroke: {
          show: true,
          colors: ["transparent"],
        },
        grid: {
          xaxis: {
            lines: {
              show: true,
            },
          },
        },
        xaxis: {
          categories: [],
        },
        fill: {
          opacity: 1,
        },
      },
      filter: {},
      petitionShowModalCount: 0,
      todayIsServing: true,
      overallIsServing: true,
      isTodayRFACat: true,
      isTodayRFAType: true,
      rfaPlot: 1,
      noRFAPlotKey: 1,
      dirRFADtePlotKey: 1,
      todayRFARankPlotKey: 1,
      courseCenterCountKey: 1,
      rfaCatPlotKey: 1,
      rfaTypePlotKey: 1,
      date: moment(new Date()).format("YYYY-MM-DD"),
      petitions: [],
      petition: null,
      petitionCirculationModalCount: 0,
      genOffrs: false,
    };
  },
  created() {
    this.appLogoImage = $themeConfig.app.appLogoImage;
  },
  async mounted() {
    // await this.dashboardData();
    // await this.noOfRFAPlot();
    await this.courseCenterCount();
    await this.overallCountData();
    // await this.rfaCatPlot();
    // await this.rfaTypePlot();
    // await this.fetchPaginatedData();
  },
  methods: {
    ...mapActions({
      // getDashboardData: "appData/getDashboardData",
      // getNoOfRFAPlot: "appData/getNoOfRFAPlot",
      // getDirRFAByDtePlot: "appData/getDirRFAByDtePlot",
      // getTodayRFARankPlot: "appData/getTodayRFARankPlot",
      getCourseCenterCount: "appData/getCourseCenterCount",
      getOverallCounts: "appData/getOverallCounts",
      // getRFACatPlot: "appData/getRFACatPlot",
      // getRFATypePlot: "appData/getRFATypePlot",
      // getPetitions: "appData/getPetitions",
    }),
    async fetchPaginatedData() {
      // if (this.getLoggedInUser.appointment_name == "AG") {
      //   this.genOffrs = true;
      // }
      // let marked_to_Dir = false;
      // let marked_to_DG = false;
      // let marked_to_AG = false;
      // let approved_by_Dir = false;
      // let approved_by_DG = false;
      // let approved_by_AG = false;
      // console.log("ROLE: ", this.getLoggedInUser.role_data.code_name);
      // if (this.getLoggedInUser.role_data.code_name === "dir_wr") {F
      //   marked_to_Dir = true;
      // } else if (this.getLoggedInUser.role_data.code_name === "dg_wr") {
      //   marked_to_DG = true;
      //   approved_by_Dir = true;
      // } else if (this.getLoggedInUser.role_data.code_name === "ag") {
      //   marked_to_AG = true;
      //   approved_by_DG = true;
      //   approved_by_Dir = true;
      // }
      // try {
      //   const res = await this.getPetitions({
      //     pageNumber: 1,
      //     genOffrs: this.genOffrs,
      //     status: this.petitionStatus.NOC_PROCESSED_FOR_APPROVAL,
      //     marked_to_Dir: marked_to_Dir,
      //     marked_to_DG: marked_to_DG,
      //     marked_to_AG: marked_to_AG,
      //     approved_by_Dir: approved_by_Dir,
      //     approved_by_DG: approved_by_DG,
      //     approved_by_AG: approved_by_AG,
      //   });
      //   this.petitions = res.data.results;
      // } catch (error) {
      //   this.displayError(error);
      // }
    },
    showCirculation() {
      console.log("----------", this.petitions[0]);
      this.petitionCirculationModalCount += 1;
      this.$nextTick(() => {
        this.$bvModal.show("noc-circulation-modal");
      });
    },
    showPetition({
      today_closed_petition,
      today_process_petition,
      exceed_by_7_days,
      overall_closed_petition,
      overall_process_petition,
      type,
      isServing,
      category,
      exceed_by_24_hrs,
    }) {
      this.filter = {};
      if (today_closed_petition) {
        this.filter.status = this.petitionStatus.CLOSED;
        this.filter.created_at = moment(new Date()).format("YYYY-MM-DD");
      }
      if (today_process_petition) {
        this.filter.status = this.petitionStatus.PROCESSING;
        this.filter.created_at = moment(new Date()).format("YYYY-MM-DD");
      }
      if (exceed_by_7_days) {
        this.filter.exceed_by_7_days = moment(new Date()).format("YYYY-MM-DD");
      }
      if (exceed_by_24_hrs) {
        this.filter.exceed_by_24_hrs = moment(new Date()).format("YYYY-MM-DD");
      }
      if (overall_closed_petition) {
        this.filter.status = this.petitionStatus.CLOSED;
      }
      if (overall_process_petition) {
        this.filter.status = this.petitionStatus.PROCESSING;
      }
      if (type) {
        this.filter.type = type;
      }
      if (isServing !== undefined) {
        this.filter.is_serving = isServing;
      }
      if (category) {
        this.filter.category = category;
      }
      this.petitionShowModalCount += 1;
      this.$nextTick(() => {
        this.$bvModal.show("petition-show-modal");
      });
    },
    async dashboardData() {
      try {
        const res = await this.getDashboardData();
        this.data = res.data;
      } catch (error) {
        this.displayError(error);
      }
    },
    async onDateChange(range) {
      if (range.length > 1) {
        this.startDate = moment(range[0]).format("YYYY-MM-DD");
        this.endDate = moment(range[1]).format("YYYY-MM-DD");

        await this.noOfRFAPlot();
      }
    },
    async onStatusDateChange(range) {
      if (range.length > 1) {
        this.startDateStatus = moment(range[0]).format("YYYY-MM-DD");
        this.endDateStatus = moment(range[1]).format("YYYY-MM-DD");

        await this.rfaCatPlot();
      }
    },
    async noOfRFAPlot() {
      try {
        const res = await this.getNoOfRFAPlot({
          start_date: this.startDate,
          end_date: this.endDate,
        });

        const cat = [];

        let stDate = this.startDate;
        while (moment(stDate).format("YYYY-MM-DD") <= this.endDate) {
          cat.push(`${moment(stDate).date()} ${moment(stDate).format("MMMM")}`);
          stDate = moment(stDate).add(1, "d").format("YYYY-MM-DD");
        }

        this.noRFAPlotOptions = {
          ...this.noRFAPlotOptions,
          xaxis: {
            categories: cat,
          },
        };
        this.noRFAPlotSeries = [
          {
            data: res.data.petitions,
          },
        ];
      } catch (error) {
        this.displayError(error);
      }
    },
    // async overallCoursesData(){
    //   try{
    //     const res = await this.getOverallCounts();
    //     this.overallCounts = res.data
    //     console.log('Overall count Data: ' + res.data.total_appr);
    //   } catch (error) {
    //     this.displayError(error);
    //   }
    // },
    async overallCountData(){
      try{
        const res = await this.getOverallCounts();
        this.overallCounts = res.data
        console.log('Overall count Data: ' + res.data.total_appr);
      } catch (error) {
        this.displayError(error);
      }
    },
    async courseCenterCount(e) {
      try {
        const res = await this.getCourseCenterCount();
        console.log("getCourseCenterCount RES: ", res.data);

        this.courseCenterCountOptions = {
          ...this.courseCenterCountOptions,
          xaxis: {
            categories: res.data[0].centers_names,
          },
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
          ]
        };
        let res_data = res.data
        for (let i = 0; i < res.data.length; i++) {
            this.courseCenterCountSeries.push({
                'name': res.data[i].course_name,
                'data': res.data[i].centers_counts
            });
        }
        console.log('courseCenterCountSeries');
        console.log(this.courseCenterCountSeries);
        this.render_one=true;
        
      } catch (error) {
        this.displayError(error);
      }
    },
    async rfaCatPlot(e) {
      try {
        const res = await this.getRFACatPlot({
          start_date: this.startDateStatus,
          end_date: this.endDateStatus,
        });

        this.rfaCatPlotOptions = {
          ...this.rfaCatPlotOptions,
          xaxis: {
            categories: res.data.category_types,
          },
          colors: ["#5cb85c", "#f0ad4e"],
        };
        this.rfaCatPlotSeries = [
          {
            name: "In Process",
            data: res.data.process_petition,
          },
          {
            name: "Closed",
            data: res.data.closed_petition,
          },
        ];
      } catch (error) {
        this.displayError(error);
      }
    },
    async rfaTypePlot(e) {
      try {
        const res = await this.getRFATypePlot({
          isToday: this.isTodayRFAType,
        });

        this.rfaTypePlotOptions = {
          ...this.rfaTypePlotOptions,
          xaxis: {
            categories: res.data.petition_types,
          },
          colors: ["#5cb85c", "#f0ad4e"],
        };
        this.rfaTypePlotSeries = [
          {
            name: "In Process",
            data: res.data.process_petition,
          },
          {
            name: "Closed",
            data: res.data.closed_petition,
          },
        ];
      } catch (error) {
        this.displayError(error);
      }
    },
    async onModalClosed() {
      console.log("MODAL CLOSED");
      await this.fetchPaginatedData();
      await this.dashboardData();
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

<style lang="scss">
@import "@core/scss/vue/libs/vue-flatpicker.scss";
@import "@core/scss/vue/libs/swiper.scss";
</style>

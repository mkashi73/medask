<template>
  <b-card no-body class="h-100 m-0">
    <b-card-body class="p-50">
      <b-row no-gutters align-v="center" style="height: 10%">
        <b-col md="9" class="px-50">
          <swiper
            class="swiper-centered-slides-2 mx-3"
            :options="swiperOptions"
            :slides-per-view="3"
          >
            <swiper-slide class="rounded swiper-shadow">
              <b-button
                variant="primary"
                pill
                size="sm"
                @click="
                  () => {
                    complaintPlot = 1;
                    noComplaintPlotKey += 1;
                  }
                "
                >No. of Complaint's by Dte</b-button
              >
            </swiper-slide>
            <swiper-slide class="rounded swiper-shadow">
              <b-button
                variant="primary"
                pill
                size="sm"
                class="ml-50"
                @click="
                  () => {
                    complaintPlot = 2;
                    dirComplaintDtePlotKey += 1;
                  }
                "
                >Dir Complaint's by Dte</b-button
              >
            </swiper-slide>
            <swiper-slide class="rounded swiper-shadow">
              <b-button
                variant="primary"
                pill
                size="sm"
                class="ml-50"
                @click="
                  () => {
                    complaintPlot = 3;
                    complaintCatPlotKey += 1;
                  }
                "
                >Complaint By Cat</b-button
              >
            </swiper-slide>
            <swiper-slide class="rounded swiper-shadow">
              <b-button
                variant="primary"
                pill
                size="sm"
                class="ml-50"
                @click="
                  () => {
                    complaintPlot = 4;
                    complaintTypePlotKey += 1;
                  }
                "
                >Complaint By Type</b-button
              >
            </swiper-slide>
          </swiper>
          <div slot="button-next" class="swiper-button-next" />
          <div slot="button-prev" class="swiper-button-prev" />
        </b-col>
        <b-col cols="3" class="pl-50">
          <b-input-group class="d-flex align-items-center" v-if="complaintPlot === 1">
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
          <!-- <date-picker
            id="date"
            v-model="date"
            placeholder="Date of Commission"
            valueType="format"
            @input="dirComplaintByDtePlot()"
            :max="new Date()"
            class="form-control flat-picker bg-transparent border-0 shadow-none my-font-size pr-0 py-0"
            v-if="complaintPlot === 2"
          /> -->
          <flat-pickr
            v-model="dateRange"
            :config="{ mode: 'range' }"
            @on-change="onchangeDate"
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
            v-if="complaintPlot === 2"
          />
          <b-form-radio-group
            id="isTodayComplaintCat"
            size="sm"
            v-model="isTodayComplaintCat"
            v-if="complaintPlot === 3"
            @change="complaintCatPlot"
            name="isTodayComplaintCat"
            :key="complaintCatPlotKey"
          >
            <b-form-radio
              v-model="isTodayComplaintCat"
              :value="true"
              class="p-0 mr-2"
            >
              Today
            </b-form-radio>
            <b-form-radio v-model="isTodayComplaintCat" :value="false" class="p-0">
              Overall
            </b-form-radio>
          </b-form-radio-group>
          <b-form-radio-group
            id="isTodayComplaintType"
            size="sm"
            v-model="isTodayComplaintType"
            v-if="complaintPlot === 4"
            @change="complaintTypePlot"
            name="isTodayComplaintType"
            :key="complaintTypePlotKey"
          >
            <b-form-radio
              v-model="isTodayComplaintType"
              :value="true"
              class="p-0 mr-2"
            >
              Today
            </b-form-radio>
            <b-form-radio v-model="isTodayComplaintType" :value="false" class="p-0">
              Overall
            </b-form-radio>
          </b-form-radio-group>
        </b-col>
      </b-row>
      <b-row no-gutters c style="height: 90%">
        <b-col class="h-100" cols="12">
          <!-- <vue-apex-charts
            type="area"
            width="100%"
            height="100%"
            :key="noComplaintPlotKey"
            :options="noComplaintPlotOptions"
            :series="noComplaintPlotSeries"
            v-if="complaintPlot === 1"
          /> -->
          <vue-apex-charts
            type="bar"
            width="100%"
            height="100%"
            :key="dirComplaintDtePlotKey"
            :options="dirComplaintDtePlotOptions"
            :series="dirComplaintDtePlotSeries"
            v-if="complaintPlot === 2"
          />
          <vue-apex-charts
            type="bar"
            width="100%"
            height="100%"
            :key="complaintCatPlotKey"
            :options="complaintCatPlotOptions"
            :series="complaintCatPlotSeries"
            v-if="complaintPlot === 3"
          />
          <vue-apex-charts
            type="bar"
            width="100%"
            height="100%"
            :key="complaintTypePlotKey"
            :options="complaintTypePlotOptions"
            :series="complaintTypePlotSeries"
            v-if="complaintPlot === 4"
          />
          <b-table
            v-if="complaintPlot === 1"
            sticky-header
            class="h-100"
            :items="complaintTable"
          >
          </b-table>
        </b-col>
      </b-row>
    </b-card-body>
  </b-card>
</template>

<script>
import { mapActions } from "vuex";
import { Swiper, SwiperSlide } from "vue-awesome-swiper";
import flatPickr from "vue-flatpickr-component";
import { $themeColors } from "@themeConfig";
import VueApexCharts from "vue-apexcharts";
import moment from "moment";
import util from "@/util.js";
import "swiper/css/swiper.css";

export default {
  components: {
    flatPickr,
    Swiper,
    SwiperSlide,
    VueApexCharts,
  },
  mixins: [util],
  data() {
    return {
      filter: {},
      status: "",
      organization_id: "",
      organizationsPlot: [],
      swiperOptions: {
        slidesPerView: "auto",
        centeredSlides: true,
        spaceBetween: 30,
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
        },
      },
      complaintTable: [],
      complaintPlot: 1,
      noComplaintPlotKey: 1,
      dirComplaintDtePlotKey: 1,
      complaintCatPlotKey: 1,
      complaintTypePlotKey: 1,
      swiperSlides: [],
      todayIsServing: true,
      overallIsServing: true,
      isTodayComplaintCat: true,
      isTodayComplaintType: true,
      noComplaintPlotSeries: [
        {
          data: [],
        },
      ],
      noComplaintPlotOptions: {
        chart: {
          zoom: {
            enabled: false,
          },
          toolbar: {
            show: false,
          },
        },
        markers: {
          strokeWidth: 7,
          strokeOpacity: 1,
          strokeColors: [$themeColors.light],
          colors: [$themeColors.warning],
        },
        colors: [$themeColors.warning],
        dataLabels: {
          enabled: false,
        },
        stroke: {
          curve: "straight",
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
      dirComplaintDtePlotSeries: [
        {
          data: [],
        },
      ],
      dirComplaintDtePlotOptions: {
        chart: {
          stacked: false,
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
      complaintCatPlotSeries: [
        {
          data: [],
        },
      ],
      complaintCatPlotOptions: {
        chart: {
          stacked: false,
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
      complaintTypePlotSeries: [
        {
          data: [],
        },
      ],
      complaintTypePlotOptions: {
        chart: {
          stacked: false,
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
      date: moment(new Date()).format("YYYY-MM-DD"),
      rangeDate: `${moment(new Date("2022-07-07")).format(
        "YYYY-MM-DD"
      )} to ${moment(new Date()).format("YYYY-MM-DD")}`,
      startDate: moment(new Date("2022-07-07")).format("YYYY-MM-DD"),
      endDate: moment(new Date()).format("YYYY-MM-DD"),

      dateRange: `${moment(new Date("2022-07-07")).format(
        "YYYY-MM-DD"
      )} to ${moment(new Date()).format("YYYY-MM-DD")}`,
      dateStart: moment(new Date("2022-07-07")).format("YYYY-MM-DD"),
      dateEnd: moment(new Date()).format("YYYY-MM-DD"),
    };
  },
  async mounted() {
    await this.noOfComplaintPlot();
    await this.dirComplaintByDtePlot();
    await this.complaintCatPlot();
    await this.complaintTypePlot();
    await this.getTableData();
  },
  methods: {
    ...mapActions({
      getNoOfComplaintPlot: "appData/getNoOfComplaintPlot",
      getDirComplaintByDtePlot: "appData/getDirComplaintByDtePlot",
      getComplaintCatPlot: "appData/getComplaintCatPlot",
      getComplaintTypePlot: "appData/getComplaintTypePlot",
    }),
    async onDateChange(range) {
      if (range.length > 1) {
        this.startDate = moment(range[0]).format("YYYY-MM-DD");
        this.endDate = moment(range[1]).format("YYYY-MM-DD");

        // await this.noOfComplaintPlot();
        await this.getTableData();
      }
    },
    async onchangeDate(range) {
      if (range.length > 1) {
        this.dateStart = moment(range[0]).format("YYYY-MM-DD");
        this.dateEnd = moment(range[1]).format("YYYY-MM-DD");

        await this.dirComplaintByDtePlot();
      }
    },
    async getTableData() {
      try {
        const res = await this.getDirComplaintByDtePlot({
          start_date: this.startDate,
          end_date: this.endDate,
        });
        this.complaintTable = [];
        // this.complaintTable = res.data;
        if (res.data.organizations.length > 0) {
          let len = res.data.organizations.length;
          let org_names = res.data.organizations;
          let finalized = res.data.finalize_count;
          let close = res.data.closed_count;
          let inprocess = res.data.in_process_count;

          for (let index = 0; index < len; index++) {
            let element = {
              Dte: org_names[index],
              finalize: finalized[index],
              close: close[index],
              inprocess: inprocess[index],
            };
            this.complaintTable.push(element);
          }
        }
      } catch (error) {
        this.displayError(error);
      }
    },
    submit() {
      this.filter = {
        status: this.status,
        sponsor_organization: this.organization_id,
        date_range_after: this.dateStart,
        date_range_before: this.dateEnd,
      };
      this.$emit(
        "complaintShowModal",
        this.filter,
        this.showModalPlace.RECEIVED
      );
    },
    async noOfComplaintPlot() {
      try {
        const res = await this.getNoOfComplaintPlot({
          start_date: this.startDate,
          end_date: this.endDate,
        });

        const cat = [];

        let stDate = this.startDate;
        while (moment(stDate).format("YYYY-MM-DD") <= this.endDate) {
          cat.push(`${moment(stDate).date()} ${moment(stDate).format("MMMM")}`);
          stDate = moment(stDate).add(1, "d").format("YYYY-MM-DD");
        }

        this.noComplaintPlotOptions = {
          ...this.noComplaintPlotOptions,
          xaxis: {
            categories: cat,
          },
        };
        this.noComplaintPlotSeries = [
          {
            data: res.data.complaints,
          },
        ];
      } catch (error) {
        this.displayError(error);
      }
    },
    async dirComplaintByDtePlot() {
      try {
        const res = await this.getDirComplaintByDtePlot({
          start_date: this.dateStart,
          end_date: this.dateEnd,
        });

        this.organizationsPlot = res.data.organizations_id;

        this.dirComplaintDtePlotOptions = {
          ...this.dirComplaintDtePlotOptions,
          xaxis: {
            categories: res.data.organizations,
          },
          chart: {
            events: {
              dataPointSelection: this.customDataPointSelection,
            },
          },
        };

        this.dirComplaintDtePlotSeries = [
          {
            name: "In Process",
            data: res.data.in_process_count,
          },
          {
            name: "Closed",
            data: res.data.closed_count,
          },
          {
            name: "Finalized",
            data: res.data.finalize_count,
          },
        ];
      } catch (error) {
        this.displayError(error);
      }
    },
    async complaintCatPlot(e) {
      try {
        const res = await this.getComplaintCatPlot({
          isToday: this.isTodayComplaintCat,
        });

        this.complaintCatPlotOptions = {
          ...this.complaintCatPlotOptions,
          xaxis: {
            categories: res.data.complaint_categories,
          },
          colors: ["#5cb85c", "#f0ad4e"],
        };
        this.complaintCatPlotSeries = [
          {
            name: "In Process",
            data: res.data.process_complaint,
          },
          {
            name: "Closed",
            data: res.data.closed_complaint,
          },
        ];
      } catch (error) {
        this.displayError(error);
      }
    },
    async complaintTypePlot(e) {
      try {
        const res = await this.getComplaintTypePlot({
          isToday: this.isTodayComplaintType,
        });

        this.complaintTypePlotOptions = {
          ...this.complaintTypePlotOptions,
          xaxis: {
            categories: res.data.complaint_types,
          },
          colors: ["#5cb85c", "#f0ad4e"],
        };
        this.complaintTypePlotSeries = [
          {
            name: "In Process",
            data: res.data.process_complaint,
          },
          {
            name: "Closed",
            data: res.data.closed_complaint,
          },
        ];
      } catch (error) {
        this.displayError(error);
      }
    },
    customDataPointSelection(event, chartContext, config) {
      switch (config.seriesIndex) {
        case 0:
          this.status = this.complaintStatus.PROCESSING;
          break;
        case 1:
          this.status = this.complaintStatus.CLOSED;
          break;
        case 2:
          this.status = this.complaintStatus.FINALIZED;
          break;
      }

      this.organization_id = this.organizationsPlot[config.dataPointIndex];

      this.submit();
    },
  },
};
</script>

<style lang="scss">
@import "@core/scss/vue/libs/vue-flatpicker.scss";
@import "@core/scss/vue/libs/swiper.scss";
</style>

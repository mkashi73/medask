<template>
  <div class="h-100">
    <b-row class="h-100" no-gutters>
      <b-col cols="12" class="h-100">
        <b-card no-body class="h-100 m-0 font-weight-bolder text-center p-25">
          <b-card-body class="h-100 p-0">
            <b-row style="height: 15%">
              <b-col class="col-sm col-sm-auto">
                <div class="d-flex justify-content-start">
                  <b-card
                    no-body
                    class="
                      m-0
                      font-weight-bolder
                      text-center
                      mb-50
                      border border-primary
                      rounded
                      d-inline-block
                    "
                  >
                    <b-card-body class="h-100 p-0">
                      <div
                        class="
                          bg-success
                          text-white
                          rounded
                          cursor-pointer
                          my-font-size-lg
                          p-50
                        "
                        @click="
                          showComplaint({
                            currently_marked: getLoggedInUser.id,
                          })
                        "
                      >
                        Balance: {{ total }}
                      </div>
                    </b-card-body>
                  </b-card>
                </div>
              </b-col>
              <b-col>
                <p class="font-weight-bolder m-0 text-center">
                  For Approval / Marked To Me
                </p>
              </b-col>
            </b-row>
            <div style="height: 85%" class="overflow-auto">
              <b-table-simple
                hover
                bordered
                small
                caption-top
                responsive
                class="mb-0"
              >
                <b-thead>
                  <b-tr>
                    <b-th class="text-center my-font-size-lg"
                      >Organization</b-th
                    >
                    <b-th class="text-center my-font-size-lg">Cat 1</b-th>
                    <b-th class="text-center my-font-size-lg">Cat 2</b-th>
                    <b-th class="text-center my-font-size-lg">Cat 3</b-th>
                    <b-th class="text-center my-font-size-lg">Cat 4</b-th>
                    <b-th class="text-center my-font-size-lg">Cat 5</b-th>
                  </b-tr>
                </b-thead>
                <b-tbody>
                  <b-tr
                    v-for="(value, name, index) in data.complaints"
                    :key="index"
                  >
                    <b-td
                      class="
                        text-center
                        my-font-size-lg
                        text-black
                        font-weight-bolder
                      "
                      @click="openFirstLevelDetail(value.id)"
                      >{{ value.name }}</b-td
                    >
                    <b-td
                      class="
                        text-center
                        my-font-size-lg
                        text-black
                        font-weight-bolder
                      "
                      v-for="(value_, name_, index_) in value.categories"
                      :key="index_"
                      @click="
                        showComplaint({
                          currently_marked: getLoggedInUser.id,
                          sponsor_organization: parseInt(name),
                          category: parseInt(name_),
                        })
                      "
                    >
                      {{ value_ === 0 ? "" : value_ }}
                    </b-td>
                  </b-tr>
                </b-tbody>
              </b-table-simple>
            </div>
          </b-card-body>
        </b-card>
      </b-col>
    </b-row>
    <user-first-level-modal
      @showComplaint="showComplaint"
      :organizationId="orginzationId"
      :key="`user-first-level-${userFirstLevelModalCount}`"
    />
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import moment from "moment";
// import ComplaintDetailModal from "@/components/complaint/ComplaintDetailModal.vue";
import UserFirstLevelModal from "@/components/dashboard/UserFirstLevelModal.vue";
import util from "@/util.js";

export default {
  components: {
    // ComplaintDetailModal,
    UserFirstLevelModal,
  },
  mixins: [util],
  data() {
    return {
      data: {},
      filter: {},
      total: 0,
      complaint: null,
      orginzationId: null,
      complaintDetailModalCount: 0,
      userFirstLevelModalCount: 0,
    };
  },
  async mounted() {
    try {
      const res = await this.getUserData({});
      this.data = res.data;
      for (let key in this.data.category_total) {
        const value = this.data.category_total[key];
        this.total += value;
      }
    } catch (error) {
      this.displayError(error);
    }
  },
  methods: {
    ...mapActions({
      getUserData: "appData/getUserData",
    }),
    showComplaint({
      currently_marked,
      sponsor_organization,
      category,
      last_30_days,
    }) {
      this.filter = {};
      if (currently_marked) {
        this.filter.status = this.complaintStatus.PROCESSING;
        this.filter.currently_marked = currently_marked;
      }
      if (sponsor_organization) {
        this.filter.status = this.complaintStatus.PROCESSING;
        this.filter.sponsor_organization = sponsor_organization;
      }
      if (category) {
        this.filter.status = this.complaintStatus.PROCESSING;
        this.filter.category = category;
      }
      if (last_30_days) {
        this.filter.last_30_days = moment(new Date()).format("YYYY-MM-DD");
      }
      this.filter.draft = false;
      this.$emit("complaintShowModal", this.filter, this.showModalPlace.User);
    },
    openFirstLevelDetail(id) {
      this.orginzationId = id;
      this.userFirstLevelModalCount += 1;

      this.$nextTick(() => {
        this.$bvModal.show("user-first-level-modal");
      });
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

<style>
.my-font-size-lg {
  font-size: 1.3rem;
}
</style>

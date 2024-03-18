<template>
  <div>
    <b-modal
      id="user-first-level-modal"
      title="Complaint show Modal"
      centered
      hide-footer
      size="lg"
      :no-close-on-esc="true"
      :no-close-on-backdrop="true"
      dialog-class="my-dialog-class"
    >
      <template #modal-title> <h2 class="m-0">Level Detail</h2> </template>

      <b-card no-body class="h-100 m-0 font-weight-bolder text-center p-25">
        <b-card-body class="h-100 p-0">
          <div style="height: 100%" class="overflow-auto">
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
                  <b-th class="text-center my-font-size-lg">Organization</b-th>
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
                    class="text-center my-font-size-lg text-black font-weight-bolder"
                    >{{ value.name }}</b-td
                  >
                  <b-td
                    class="text-center my-font-size-lg text-black font-weight-bolder"
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
    </b-modal>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import moment from "moment";
import util from "@/util.js";

export default {
  mixins: [util],
  props: {
    organizationId: Number,
  },
  components: {},
  data() {
    return {
      data: {},
      filter: {},
      total: 0,
      complaint: null,
    };
  },
  async mounted() {
    if (this.organizationId) {
      try {
        const res = await this.getUserData({
          organization_id: this.organizationId,
        });
        this.data = res.data;
        for (let key in this.data.category_total) {
          const value = this.data.category_total[key];
          this.total += value;
        }
      } catch (error) {
        this.displayError(error);
      }
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
      this.$emit("showComplaint", this.filter, this.showModalPlace.User);
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

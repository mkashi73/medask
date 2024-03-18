<template>
  <div style="height: 7%;" class="py-0 pt-1 px-0 bg-primary">
    <div
      class="
        d-flex
        justify-content-center
        align-items-center
        h-100
        bg-primary1
        gold-border
        round
      "
    >
      
      <b-link
        class="
          text-light
          my-nav-item my-nav-link
          d-flex
          align-items-center
          ml-2
        "
        :to="{ name: 'User' }"
        v-if="hasPermission('user_show')"
        
      >
        <feather-icon icon="UserIcon" size="16" class="mr-50 gold" />
        <span>USER</span>
      </b-link>
      
      <b-link
        class="
          text-light
          my-nav-item my-nav-link
          d-flex
          align-items-center
          ml-2
        "
        :to="{ name: 'Candidate' }"
        v-if="hasPermission('show_dashboard')"        
      >
        <feather-icon icon="UserIcon" size="20" class="mr-50 gold" />
        <span><b>Candidates</b></span>
      </b-link>

      <b-link
        class="
          text-light
          my-nav-item my-nav-link
          d-flex
          align-items-center
          ml-2
        "
        :to="{ name: 'Course' }"
        v-if="hasPermission('show_dashboard')"        
      >
        <feather-icon icon="BriefcaseIcon" size="20" class="mr-50 gold" />
        <span><b>Courses</b></span>
      </b-link>

      <b-link
        class="
          text-light
          my-nav-item my-nav-link
          d-flex
          align-items-center
          ml-2
        "
        :to="{ name: 'Report' }"
        v-if="hasPermission('show_dashboard')"        
      >
        <feather-icon icon="ClipboardIcon" size="20" class="mr-50 gold" />
        <span><b>Reports</b></span>
      </b-link>

      <b-dropdown
        text="Reports"
        class="m-0 p-0 ml-2"
        variant="primary"
        size="sm"
        v-if="
          hasPermission('daily_report_show') ||
          hasPermission('overall_report_show')
        "
      >
        <template #button-content>
          <feather-icon icon="FileIcon" size="15" class="mr-50 text-light" />
          Reports
        </template>
        <b-dropdown-item
          v-if="hasPermission('daily_report_show')"
          :to="{ name: 'Daily' }"
          >Daily</b-dropdown-item
        >
        <b-dropdown-item
          v-if="hasPermission('overall_report_show')"
          :to="{ name: 'Overall' }"
          >Overall</b-dropdown-item
        >
      </b-dropdown>

      <b-button
        type="submit"
        variant="primary"
        class="btn-login btn-border "
        pill
        @click="logoutButtonClick"
      >
        Logout <feather-icon size="15" icon="LogOutIcon" class="mr-50" />
      </b-button>
    </div>
    <div></div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  computed: {
    ...mapGetters({
      hasPermission: "appData/hasPermission",
      getLoggedInUser: "appData/getLoggedInUser",
    }),
  },
  methods: {
    ...mapActions({ logout: "appData/logout" }),
    async logoutButtonClick() {
      try {
        const res = await this.logout();
        if (res.status === 204) {
          this.$router.push({ name: "Login" });
        }
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>

<style>
.btn-login {
  margin-right: 0px;
  margin-left: 2%;
  float: right;
  padding: 5px 5px;
  border: 2px solid #e1bf93 !important;
}
.gold-border{
  border: 1px solid #e1bf93;
}
.gold{
  color: #e1bf93;
}
</style>

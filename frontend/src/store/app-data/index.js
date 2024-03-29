import axiosIns from "@/libs/axios";

export default {
  namespaced: true,
  state: {
    isLoggedIn: false,
    user: null,
    navMenuItems: [],
  },
  getters: {
    getLoggedInUser: (state) => {
      return state.user;
    },
    hasPermission: (state) => (name) => {
      if (state.user) {
        return state.user.permissions.hasOwnProperty(name);
      }
      return false;
    },
    hasRole: (state) => (name) => {
      if (state.user.role_data.code_name === name) {
        return true;
      }
      return false;
    },
    isLoggedIn: (state) => state.isLoggedIn,
    getNavMenuItems: (state) => state.navMenuItems,
  },
  mutations: {
    login(state, data) {
      state.isLoggedIn = true;
      state.user = data.user;
    },
    logout(state) {
      state.isLoggedIn = false;
      state.user = null;
    },
    setNavMenuItems(state) {
      state.navMenuItems = [];

      if (state.user.permissions.hasOwnProperty("show_dashboard")) {
        state.navMenuItems.push({
          title: "Dashboard",
          route: "Dashboard",
          icon: "BarChart2Icon",
        });
      }

      if (state.user.permissions.hasOwnProperty("show_user")) {
        state.navMenuItems.push({
          title: "User",
          icon: "UserIcon",
          route: "User",
        });
      }

      if (state.user.permissions.hasOwnProperty("show_role")) {
        state.navMenuItems.push({
          title: "Role",
          icon: "AwardIcon",
          route: "Role",
        });
      }
  },
  actions: {
    async login({ commit }, payload) {
      const res = await axiosIns.post("login", payload);
      if (res.status === 200) {
        commit("login", res.data);
        commit("setNavMenuItems");
      }
      return res;
    },

    async logout({ commit }) {
      const res = await axiosIns.post("logout");
      if (res.status === 204) {
        commit("logout");
      }
      return res;
    },
    async getUser({ commit }, { pk }) {
      const res = await axiosIns.get(`users/${pk}/`);
      return res;
    },
    async getUsers({ commit }, { pageNumber, name, username, excludeUser }) {
      let url = `users/?page=${pageNumber}`;
      if (name) {
        url += `&name=${name}`;
      }
      if (username) {
        url += `&username=${username}`;
      }
      if (excludeUser) {
        url += `&exclude_user=${excludeUser}`;
      }
      const res = await axiosIns.get(url);
      return res;
    },
    async getUsersUnPaginated({ commit }, { organization, role }) {
      let url = `users-unpaginated/`;
      if (organization) {
        url += `?organization=${organization}`;
      }
      if (role) {
        url += `?role=${role}`;
      }
      const res = await axiosIns.get(url);
      return res;
    },
    async getCurrentUser({ commit }) {
      const res = await axiosIns.get("current");
      if (res.status === 200) {
        commit("login", res.data);
        commit("setNavMenuItems");
      }
    },
    async getUserData({ commit }, { organization_id }) {
      let p = {};
      if (organization_id) {
        p = {
          ...p,
          organization_id: organization_id,
        };
      }
      const res = await axiosIns.get(`user-data`, {
        params: p,
      });
      return res;
    },
    async createUser({ commit }, { payload }) {
      const res = await axiosIns.post("users-create-update", payload);
      return res;
    },
    async updateUser({ commit }, { payload, pk }) {
      const res = await axiosIns.patch(`users/${pk}/`, payload);
      return res;
    },
    async getPermissions({ commit }) {
      const res = await axiosIns.get("permissions");
      return res;
    },

    async getRoles({ commit }, { pageNumber, name, codeName }) {
      let url = `roles/?page=${pageNumber}`;
      if (name) {
        url += `&name=${name}`;
      }
      if (codeName) {
        url += `&code_name=${codeName}`;
      }
      const res = await axiosIns.get(url);
      return res;
    },
    async getRole({ commit }, { pk }) {
      const res = await axiosIns.get(`roles/${pk}/`);
      return res;
    },
    async createRole({ commit }, payload) {
      const res = await axiosIns.post("roles/", payload);
      return res;
    },
    async updateRole({ commit }, { payload, pk }) {
      const res = await axiosIns.put(`roles/${pk}/`, payload);
      return res;
    },
    async deleteRole({ commit }, { pk }) {
      const res = await axiosIns.delete(`roles/${pk}/`);
      return res;
    },
  },
},
};

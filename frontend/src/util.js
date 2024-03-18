import ToastificationContent from "@core/components/toastification/ToastificationContent.vue";
import moment from "moment";

const util = {
  data() {
    return {
      categoryColors: {
      1: "table-primary",
      2: "table-success",
      3: "table-info",
      4: "table-danger",
      5: "table-warning",
    },
    complaintStatus: {
      PENDING: 1,
      PROCESSING: 2,
      FINALIZED: 3,
      CLOSED: 4,
    },
    categoryColorsHex: [
      "#094120",
      "#28a745",
      "#17a2b8",
      "#dc3545",
      "#ffc107",
      "#094120",
      "#28a745",
      "#17a2b8",
      "#dc3545",
      "#ffc107",
      "#094120",
      "#28a745",
      "#17a2b8",
      "#dc3545",
      "#ffc107",
      "#094120",
      "#28a745",
      "#17a2b8",
      "#dc3545",
      "#ffc107",
      "#094120",
      "#28a745",
      "#17a2b8",
      "#dc3545",
      "#ffc107",
      "#094120",
      "#28a745",
      "#17a2b8",
      "#dc3545",
      "#ffc107",
    ],
    showModalPlace: {
      TYPE_TABLE: 1,
      STATISTICS: 2,
      CAT_TABLE: 3,
      AG_APPROVED_REJECTED: 4,
      EXCEEDED: 5,
      RECEIVED: 6,
      USER: 7,
    },
    finalApproval: {
      DEFAULT: 0,
      APPROVED: 1,
      REJECTED: 2,
    },
    searchTypes: [
      { value: 1, name: "Case No" },
      { value: 2, name: "PA No" },
      { value: 3, name: "CNIC" },
      { value: 4, name: "Title" },
      { value: 5, name: "Status" },
      { value: 6, name: "Mobile Number" },
      { value: 7, name: "Date Range" },
      { value: 8, name: "Sponsor Organization" },
    ],
  };
  },
  methods: {
    getDateString(date) {
      return moment(date).format("Do MMMM YYYY on HH:mm");
    },  
    rowClass(item, type) {
      if (!item || type !== "row") return;
      return this.categoryColors[item.category];
    },
    rowClassCategoryHex(category) {
      return this.categoryColorsHex[category - 1];
    },
    statusNamesColor(status) {
      let name = "";
      switch (status) {
        case 1:
          name = "info";
          break;
        case 2:
          name = "warning";
          break;
        case 3:
          name = "success";
          break;
        case 4:
          name = "primary";
          break;
      }
      return name;
    },
    statusNames(status) {
      let name = "";
      switch (status) {
        case 1:
          name = "Pending";
          break;
        case 2:
          name = "Processing";
          break;
        case 3:
          name = "Finalized";
          break;
        case 4:
          name = "Closed";
          break;
      }
      return name;
    }, 
    typeName(type) {
      let name = "";
      switch (type) {
        case 1:
          name = "Army";
          break;
        case 2:
          name = "Civilian";
          break;
        case 3:
          name = "Anonymous";
          break;
        default:
          break;
      }
      return name;
    },
    openFile(path) {
      window.open(path, "_blank");
    },
    displayError(error) {
      const msgs = [];
      if (
        !error.response ||
        error.response.status === 500 ||
        typeof error.response.data === "string"
      ) {
        msgs.push("Error: Server Error");
      } else {
        const data = error.response.data;
        for (let key in data) {
          const element = data[key];
          if (Array.isArray(element)) {
            if (typeof element[0] === "string") {
              if (key !== "msg") {
                msgs.push(`${key}: ${element[0]}`);
              } else {
                msgs.push(`${element[0]}`);
              }
            } else if (typeof element[0] === "object") {
              for (const key in element[0]) {
                if (key !== "msg") {
                  msgs.push(`${key}: ${element[0][key][0]}`);
                } else {
                  msgs.push(`${element[0][key][0]}`);
                }
              }
            }
          } else if (typeof element === "object") {
            for (const key in element) {
              if (key !== "msg") {
                msgs.push(`${key}: ${element[key][0]}`);
              } else {
                msgs.push(`${element[key][0]}`);
              }
            }
          } else {
            if (element !== "Invalid page.") {
              msgs.push(element);
            }
          }
        }
      }

      for (let i = 0; i < msgs.length; i++) {
        const msg = msgs[i];
        this.$toast(
          {
            component: ToastificationContent,
            props: {
              title: "Error",
              icon: "BellIcon",
              text: msg,
              variant: "danger",
            },
          },
          {
            timeout: 2000,
            position: "top-center",
          }
        );
      }
    },
  },
};

export default util;

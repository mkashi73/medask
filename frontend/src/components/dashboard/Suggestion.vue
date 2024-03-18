<template>
  <b-card no-body class="h-100 m-0">
    <p class="font-weight-bolder m-0 text-center w-100 mt-50">
      AG's Suggestion Box
    </p>
    <b-card-body
      class="h-100 px-50 py-0 overflow-auto d-flex align-items-center justify-content-center"
    >
      <validation-observer ref="suggestionBoxFormValidation" class="w-100">
        <BForm @submit.prevent>
          <b-form-group label-for="suggestion">
            <validation-provider
              #default="{ errors }"
              name="Suggestion"
              :rules="{ regex: /^[A-Z0-9.\s]*$/i }"
            >
              <b-form-textarea
                id="suggestion"
                v-model="text"
                placeholder="Please suggest along with your Rank and Name"
                rows="2"
                class="char-textarea"
                no-resize
                v-on:keyup.enter.prevent="validationSuggestionForm()"
              />
              <small class="text-danger">{{ errors[0] }}</small>
              <small
                class="textarea-counter-value float-right"
                :class="text.length >= maxSuggestionCount ? 'bg-danger' : ''"
              >
                <span class="char-count">{{ text.length }}</span>
                /
                {{ maxSuggestionCount }}
              </small>
            </validation-provider>
          </b-form-group>
        </BForm>
      </validation-observer>
    </b-card-body>
  </b-card>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import { ValidationProvider, ValidationObserver } from "vee-validate";
import { required } from "@validations";
import util from "@/util.js";
import { BForm } from "bootstrap-vue";

export default {
  components: {
    ValidationProvider,
    ValidationObserver,
    BForm,
  },
  mixins: [util],
  data() {
    return {
      required,
      text: "",
      maxSuggestionCount: 300,
    };
  },
  methods: {
    ...mapActions({
      createSuggestion: "appData/createSuggestion",
    }),
    async validationSuggestionForm() {
      const success = await this.$refs.suggestionBoxFormValidation.validate();
      if (success) {
        await this.submitSuggestionForm();
      }
    },
    async submitSuggestionForm() {
      try {
        if (this.text.length > this.maxSuggestionCount) {
          this.displayError(
            `Suggestion Length cannot be greater than ${this.maxSuggestionCount}`
          );
          return;
        }

        const res = await this.createSuggestion({
          text: this.text,
          created_by: this.getLoggedInUser.id,
          updated_by: this.getLoggedInUser.id,
        });
        if (res.status === 201) {
          this.$swal({
            title: "Suggestion created successfully",
            icon: "success",
          });
          this.text = "";
        }
      } catch (error) {
        console.log(error);
        this.displayError(error);
      }
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

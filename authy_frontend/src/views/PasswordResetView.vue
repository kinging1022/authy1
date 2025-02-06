<template>
    <div class="min-h-screen w-full bg-gradient-to-br from-emerald-50 to-white flex items-start sm:items-center justify-center p-4 pt-8 sm:p-4">
      <div class="w-full max-w-md space-y-8 bg-white p-8 rounded-2xl shadow-sm">
        <div class="text-center">
          <h2 class="text-3xl font-semibold text-emerald-950">Reset Password</h2>
          <p class="mt-2 text-sm text-gray-500">Enter your new password below</p>
        </div>
  
        <form v-if="!isLoading && !isSuccess" @submit.prevent="handleSubmit" class="mt-8 space-y-6">
          <div class="space-y-4">
            <!-- New Password Field -->
            <div class="relative">
              <label for="new-password" class="sr-only">New Password</label>
              <Lock class="absolute left-3 top-1/2 -translate-y-1/2 h-5 w-5 text-gray-400" />
              <input
                id="new-password"
                name="new-password"
                type="password"
                v-model="formData.newPassword"
                class="block w-full rounded-lg border border-gray-200 pl-12 p-3 text-sm focus:border-emerald-500 focus:ring-emerald-500"
                placeholder="New Password"
              />
              <p v-if="errors.newPassword" class="text-sm text-red-500">{{ errors.newPassword }}</p>
            </div>
  
            <!-- Confirm Password Field -->
            <div class="relative">
              <label for="confirm-password" class="sr-only">Confirm Password</label>
              <Lock class="absolute left-3 top-1/2 -translate-y-1/2 h-5 w-5 text-gray-400" />
              <input
                id="confirm-password"
                name="confirm-password"
                type="password"
                v-model="formData.confirmPassword"
                class="block w-full rounded-lg border border-gray-200 pl-12 p-3 text-sm focus:border-emerald-500 focus:ring-emerald-500"
                placeholder="Confirm Password"
              />
              <p v-if="errors.confirmPassword" class="text-sm text-red-500">{{ errors.confirmPassword }}</p>
            </div>
          </div>
  
          <!-- General Error Message -->
          <p v-if="errors.general" class="text-sm text-red-500 text-center">{{ errors.general }}</p>
  
          <!-- Submit Button -->
          <button
            type="submit"
            class="group relative w-full flex justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-lg text-white bg-emerald-600 hover:bg-emerald-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-emerald-500"
          >
            Reset Password
            <ArrowRight class="ml-2 h-4 w-4 transition-transform group-hover:translate-x-1" />
          </button>
        </form>
  
        <!-- Loading Animation -->
        <div v-if="isLoading" class="flex flex-col items-center justify-center space-y-4">
          <div class="loader"></div>
          <p class="text-emerald-600 font-medium">Resetting your password...</p>
        </div>
  
        <!-- Success Message -->
        <div v-if="isSuccess" class="text-center space-y-4">
          <CheckCircle class="w-16 h-16 text-emerald-500 mx-auto" />
          <h3 class="text-2xl font-semibold text-emerald-900">Password Reset Successful</h3>
          <p class="text-gray-600">Your password has been successfully reset.</p>
          <button
            @click="goToLogin"
            class="mt-4 w-full flex justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-lg text-white bg-emerald-600 hover:bg-emerald-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-emerald-500"
          >
            Go to Login
            <ArrowRight class="ml-2 h-4 w-4 transition-transform group-hover:translate-x-1" />
          </button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { Lock, ArrowRight, CheckCircle } from 'lucide-vue-next';
  import { useToastStore } from "@/stores/toast";
  import axios from 'axios';
  
  export default {
    name: 'PasswordResetForm',
    components: {
      Lock,
      ArrowRight,
      CheckCircle
    },
    data() {
      return {
        formData: {
          newPassword: "",
          confirmPassword: "",
        },
        errors: {},
        isLoading: false,
        isSuccess: false,
      };
    },
    setup() {
      const toastStore = useToastStore();
  
      return {
        toastStore,
      };
    },
    methods: {
      async handleSubmit() {
        this.errors = {}; // Reset errors before validation
  
        // Validate Inputs
        if (!this.formData.newPassword) this.errors.newPassword = "New password is required";
        if (!this.formData.confirmPassword) this.errors.confirmPassword = "Confirm password is required";
        if (this.formData.newPassword !== this.formData.confirmPassword) {
          this.errors.general = "Passwords do not match";
        }
  
        // Stop if validation errors exist
        if (Object.keys(this.errors).length > 0) return;
  
        this.isLoading = true;
  
        try {
          // Get the token from the URL
          const token = this.$route.params.token;
          
  
          if (!token) {
            this.errors.general = "Invalid or missing reset token";
            this.isLoading = false;
            return;
          }
  
          const response = await axios.post('api/reset-password/', {
            token: token,
            new_password: this.formData.newPassword,
            confirm_password: this.formData.confirmPassword
          });
  
          // Simulate a delay for the loading animation
          setTimeout(() => {
            this.isLoading = false;
            this.isSuccess = true;
          }, 2000);
  
        } catch (err) {
          console.error(err.response?.data);
  
          this.isLoading = false;
  
          if (err.response && err.response.data) {
            this.errors.general = err.response.data.error || 'An error occurred. Please try again.';
          } else {
            this.errors.general = 'An error occurred. Please try again.';
          }
  
          this.toastStore.showToast(5000, this.errors.general, "bg-red-500");
        }
      },
      goToLogin() {
        this.$router.push('/login');
      }
    }
  };
  </script>
  
  <style scoped>
  .loader {
    border: 5px solid #f3f3f3;
    border-top: 5px solid #10b981;
    border-radius: 50%;
    width: 50px;
    height: 50px;
    animation: spin 1s linear infinite;
  }
  
  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }
  
  .fade-enter-active, .fade-leave-active {
    transition: opacity 0.5s;
  }
  .fade-enter, .fade-leave-to {
    opacity: 0;
  }
  </style>
  
  

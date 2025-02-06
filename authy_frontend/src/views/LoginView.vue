<template>
    <div class="min-h-screen w-full bg-gradient-to-br from-emerald-50 to-white flex items-start sm:items-center justify-center p-4 pt-8 sm:p-4">
      <div class="w-full max-w-md space-y-8 bg-white p-8 rounded-2xl shadow-sm">
        <div class="text-center">
          <h2 class="text-3xl font-semibold text-emerald-950">LOGIN</h2>
          <p class="mt-2 text-sm text-gray-500">Welcome</p>
        </div>
  
        <form @submit.prevent="handleSubmit" class="mt-8 space-y-6">
          <div class="space-y-4">
            <!-- Username Field -->
            <div class="relative">
              <label for="username" class="sr-only">Username</label>
              <User class="absolute left-3 top-1/2 -translate-y-1/2 h-5 w-5 text-gray-400" />
              <input
                id="username"
                name="username"
                type="text"
                v-model="formData.username"
                class="block w-full rounded-lg border border-gray-200 pl-12 p-3 text-sm focus:border-emerald-500 focus:ring-emerald-500"
                placeholder="Username"
              />
              <p v-if="errors.username" class="text-sm text-red-500">{{ errors.username }}</p>
            </div>
  
            <!-- Password Field -->
            <div class="relative">
              <label for="password" class="sr-only">Password</label>
              <Lock class="absolute left-3 top-1/2 -translate-y-1/2 h-5 w-5 text-gray-400" />
              <input
                id="password"
                name="password"
                type="password"
                v-model="formData.password"
                class="block w-full rounded-lg border border-gray-200 pl-12 p-3 text-sm focus:border-emerald-500 focus:ring-emerald-500"
                placeholder="Password"
              />
              <p v-if="errors.password" class="text-sm text-red-500">{{ errors.password }}</p>
            </div>
          </div>
  
          <!-- Forgot Password Link -->
          <div class="text-right">
            <a @click.prevent="showForgotPasswordModal" href="#" class="text-sm text-emerald-600 hover:text-emerald-500">
              Forgot your password?
            </a>
          </div>
  
          <!-- General Error Message -->
          <p v-if="errors.general" class="text-sm text-red-500 text-center">{{ errors.general }}</p>
  
          <!-- Submit Button -->
          <button
            type="submit"
            class="group relative w-full flex justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-lg text-white bg-emerald-600 hover:bg-emerald-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-emerald-500"
          >
            Sign in
            <ArrowRight class="ml-2 h-4 w-4 transition-transform group-hover:translate-x-1" />
          </button>
        </form>
      </div>
  
      <!-- Forgot Password Modal -->
      <div v-if="showForgotPassword" class="fixed inset-0 bg-gradient-to-br from-emerald-50 to-white  flex items-center justify-center p-4">
        <div class="bg-white p-6 rounded-lg max-w-md w-full">
          <h3 class="text-lg font-medium text-gray-900 mb-4">Reset Password</h3>
          <form @submit.prevent="handleForgotPassword">
            <div class="mb-4">
              <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
              <input
                type="email"
                id="email"
                v-model="forgotPasswordEmail"
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-emerald-500 focus:ring-emerald-500"
                required
              />
            </div>
            <div class="flex justify-end space-x-3">
              <button
                type="button"
                @click="showForgotPassword = false"
                class="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-100 rounded-md hover:bg-gray-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500"
              >
                Cancel
              </button>
              <button
                type="submit"
                class="px-4 py-2 text-sm font-medium text-white bg-emerald-600 rounded-md hover:bg-emerald-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-emerald-500"
              >
                Reset Password
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { User, Lock, ArrowRight } from 'lucide-vue-next';
  import { useUserStore } from "@/stores/user";
  import { useToastStore } from "@/stores/toast";
  import axios from 'axios';
  
  export default {
    name: 'AdminLoginForm',
    components: {
      User,
      Lock,
      ArrowRight
    },
    data() {
      return {
        formData: {
          username: "",
          password: "",
        },
        errors: {},
        showForgotPassword: false,
        forgotPasswordEmail: "",
      };
    },
    setup() {
      const userStore = useUserStore();
      const toastStore = useToastStore();
  
      return {
        userStore,
        toastStore,
      };
    },
    methods: {
      async handleSubmit() {
        this.errors = {}; // Reset errors before validation
  
        // Validate Inputs
        if (!this.formData.username) this.errors.username = "Username is required";
        if (!this.formData.password) this.errors.password = "Password is required";
  
        // Stop if validation errors exist
        if (Object.keys(this.errors).length > 0) return;
  
        try {
          const response = await axios.post('api/login/', this.formData);
          this.userStore.setToken(response.data);
  
          // Reset form fields
          this.formData.username = "";
          this.formData.password = "";

          // Fetch user details
          await this.fetchUser()

          this.$router.push('/dashboard')

          this.toastStore.showToast(5000, `Welcome ${this.userStore.user.username}`, "bg-emerald-500");


          
  
        } catch (err) {
          console.error(err.response?.data?.detail); // Debugging
  
          if (err.response && err.response.data) {
            if (err.response.data.detail === 'Account is inactive') {
              this.errors.general = 'Your account is inactive. Check your email or contact support.';
              this.toastStore.showToast(5000, this.errors.general, "bg-emerald-500");
  
            } else if (err.response.data.detail === 'No active account found with the given credentials') {
              this.errors.general = 'Invalid username or password.';
              this.toastStore.showToast(5000, this.errors.general, "bg-red-500");
  
            } else {
              this.errors.general = 'An error occurred. Please try again.';
              this.toastStore.showToast(5000, this.errors.general, "bg-red-500");
            }
          } else {
            this.errors.general = 'An error occurred. Please try again.';
          }
        }
      },

      async fetchUser(){
        try{
            const response = await axios.get('api/user/')
            this.userStore.setUserInfo(response.data)

          }catch(error){
            console.error(error)

          }
      },
      showForgotPasswordModal() {
        this.showForgotPassword = true;
     },

    async handleForgotPassword() {
      try {
        await axios.post('api/request-password-reset/', { email: this.forgotPasswordEmail });
        this.toastStore.showToast(5000, "Password reset instructions sent to your email.", "bg-emerald-500");
        this.showForgotPassword = false;
        this.forgotPasswordEmail = "";
      } catch (err) {
        console.error(err);
        this.toastStore.showToast(5000, "An error occurred. Please try again.", "bg-red-500");
      }
    }
    }
  };
  </script>
  

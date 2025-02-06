<template>
    <div class="min-h-screen w-full bg-gradient-to-br from-emerald-50 to-white flex items-start sm:items-center justify-center p-4 pt-8 sm:p-4">
      <div class="w-full max-w-md space-y-8 bg-white p-8 rounded-2xl shadow-sm">
        <div class="text-center">
          <h2 class="text-3xl font-semibold text-emerald-950">SIGN UP</h2>
          <p class="mt-2 text-sm text-gray-500">
            Welcome 
          </p>
        </div>
        <form @submit.prevent="handleSubmit" class="mt-8 space-y-6">
          <div class="space-y-4">
            <div class="relative">
              <label for="email" class="sr-only">
                Email
              </label>
              <User class="absolute left-3 top-1/2 -translate-y-1/2 h-5 w-5 text-gray-400" />
              <input
                id="email"
                name="email"
                type="email"
                required
                v-model="formData.email"
                class="block w-full rounded-lg border border-gray-200 pl-12 p-3 text-sm focus:border-emerald-500 focus:ring-emerald-500"
                placeholder="Email Address"
              />
              <p v-if="errors.email" class="text-sm text-red-500">{{ errors.email }}</p>
            </div>
            <div class="relative">
              <label for="username" class="sr-only">
                Username
              </label>
              <User class="absolute left-3 top-1/2 -translate-y-1/2 h-5 w-5 text-gray-400" />
              <input
                id="username"
                name="username"
                type="text"
                required
                v-model="formData.username"
                class="block w-full rounded-lg border border-gray-200 pl-12 p-3 text-sm focus:border-emerald-500 focus:ring-emerald-500"
                placeholder="Username"
              />
              <p v-if="errors.username" class="text-sm text-red-500">{{ errors.username }}</p>
            </div>
            <div class="relative">
              <label for="password" class="sr-only">
                Password
              </label>
              <Lock class="absolute left-3 top-1/2 -translate-y-1/2 h-5 w-5 text-gray-400" />
              <input
                id="password"
                name="password"
                type="password"
                required
                v-model="formData.password"
                class="block w-full rounded-lg border border-gray-200 pl-12 p-3 text-sm focus:border-emerald-500 focus:ring-emerald-500"
                placeholder="Password"
              />
              <p v-if="errors.password" class="text-sm text-red-500">{{ errors.password }}</p>
            </div>
            <div class="relative">
              <label for="password2" class="sr-only">
                Retype Password
              </label>
              <Lock class="absolute left-3 top-1/2 -translate-y-1/2 h-5 w-5 text-gray-400" />
              <input
                id="password2"
                name="password2"
                type="password2"
                required
                v-model="formData.password2"
                class="block w-full rounded-lg border border-gray-200 pl-12 p-3 text-sm focus:border-emerald-500 focus:ring-emerald-500"
                placeholder="Retype Password"
              />
              <p v-if="errors.password2" class="text-sm text-red-500">{{ errors.password2 }}</p>
            </div>
          </div>
          <button
            type="submit"
            class="group relative w-full flex justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-lg text-white bg-emerald-600 hover:bg-emerald-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-emerald-500"
          >
            Sign in
            <ArrowRight class="ml-2 h-4 w-4 transition-transform group-hover:translate-x-1" />
          </button>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  import { User, Lock, ArrowRight } from 'lucide-vue-next'
  import axios from 'axios';
  import {useToastStore} from "@/stores/toast";

  export default {
    name: 'SignUpForm',
    components: {
      User,
      Lock,
      ArrowRight
    },
    setup() {
        const toastStore = useToastStore()

        return {
            toastStore
        }
    },
    data() {
      return {
        formData: {
          username: "",
          password: "",
          email: "",
          password2:""
        },
        errors: {},
      }
    },
    methods: {
      async handleSubmit() {
        this.errors = {};
  
        if (!this.formData.username) this.errors.username = "Username is required";
        if (!this.formData.password) this.errors.password = "Password is required";
        if (!this.formData.email) this.errors.email = "email is required";
        if(this.formData.password !== this.formData.password2) this.errors.password2 = "password do not match"

        
        if (Object.keys(this.errors).length === 0) {
          try {
            const response = axios.post('api/signup/',this.formData,)
            if (response.status === 201){
                this.toastStore.showToast(5000,`${response.data.message}`,'bg-emerald-500')
            }
            Object.keys(this.formData).forEach((key) => {
              this.formData[key] = "";
            });
            this.$router.push('/login')
  
  
          } catch (error) {
            console.error('Login error:', error);
          }
        }
      }
    }
  }
  </script>

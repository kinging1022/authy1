<template>
    <div class="flex w-full min-h-screen bg-emerald-50">
      <!-- Sidebar (reused from the dashboard) -->
      
      <!-- Main Content -->
      <div class="flex-1 p-8">
        <div class="max-w-2xl mx-auto">
          <h2 class="text-2xl font-semibold text-gray-800 mb-6">Edit Password</h2>
          
          <form @submit.prevent="handleSubmit" class="bg-white rounded-xl border border-emerald-100 p-6 shadow-sm">
            <div class="mb-4">
              <label for="current-password" class="block text-sm font-medium text-gray-700 mb-1">Current Password</label>
              <input
                id="current-password"
                v-model="currentPassword"
                type="password"
                required
                class="w-full px-3 py-2 border border-emerald-200 rounded-md focus:outline-none focus:ring-2 focus:ring-emerald-500"
              />
            </div>
            
            <div class="mb-4">
              <label for="new-password" class="block text-sm font-medium text-gray-700 mb-1">New Password</label>
              <input
                id="new-password"
                v-model="newPassword"
                type="password"
                required
                class="w-full px-3 py-2 border border-emerald-200 rounded-md focus:outline-none focus:ring-2 focus:ring-emerald-500"
              />
            </div>
            
            <div class="mb-6">
              <label for="confirm-password" class="block text-sm font-medium text-gray-700 mb-1">Confirm New Password</label>
              <input
                id="confirm-password"
                v-model="confirmPassword"
                type="password"
                required
                class="w-full px-3 py-2 border border-emerald-200 rounded-md focus:outline-none focus:ring-2 focus:ring-emerald-500"
              />
            </div>
            
            <div class="flex items-center justify-between">
              <button
                type="submit"
                class="px-4 py-2 bg-emerald-600 text-white rounded-md hover:bg-emerald-700 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:ring-offset-2 transition-colors duration-200"
              >
                Update Password
              </button>
              <button
                type="button"
                @click="resetForm"
                class="px-4 py-2 text-emerald-600 hover:text-emerald-700 focus:outline-none focus:underline transition-colors duration-200"
              >
                Reset
              </button>
            </div>
          </form>
  
          <!-- Success Message -->
          <div
            v-if="showSuccess"
            class="mt-4 p-4 bg-emerald-100 border border-emerald-200 text-emerald-700 rounded-md animate-fade-in"
          >
            Password updated successfully!
          </div>
  
          <!-- Error Message -->
          <div
            v-if="errorMessage"
            class="mt-4 p-4 bg-red-100 border border-red-200 text-red-700 rounded-md animate-fade-in"
          >
            {{ errorMessage }}
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
import axios from 'axios';
import { useToastStore } from '@/stores/toast';
import { useUserStore } from '@/stores/user';
import { Shield, LayoutDashboard, UserCircle, Settings, LogOut } from 'lucide-vue-next'
  
  export default {
    name: 'EditPassword',
    components: {
      Shield,
      LayoutDashboard,
      UserCircle,
      Settings,
      LogOut
    },
    setup() {
      const userStore = useUserStore();
      const toastStore = useToastStore();
  
      return {
        userStore,
        toastStore,
      };
    },
    data() {
      return {
        currentPassword: '',
        newPassword: '',
        confirmPassword: '',
        showSuccess: false,
        errorMessage: ''
      }
    },
    methods: {
      async handleSubmit() {
        // Reset messages
        this.showSuccess = false;
        this.errorMessage = '';
  
        // Basic validation
        if (this.newPassword !== this.confirmPassword) {
          this.errorMessage = 'New passwords do not match.';
          return;
        }
  
        if (this.newPassword.length < 8) {
          this.errorMessage = 'New password must be at least 8 characters long.';
          return;
        }

        try{

            const response = await axios.post('api/edit/password/',{
                current_password: this.currentPassword,
                new_password: this.newPassword,
                confirm_password: this.confirmPassword

            })
            
            this.toastStore.showToast(5000, `${response.data.message}`, "bg-emerald-500")
            setTimeout(() => {
            this.showSuccess = true;
            this.resetForm();
            }, 1000);
            

        }catch(error){
            if (error.response &&  error.response.data){
                this.errorMessage = error.response.data.error
                this.resetForm()
                this.toastStore.showToast(5000, `${error.response.data.error}`, "bg-red-500")
                

            }
        }
  
        
        
      },
      resetForm() {
        this.currentPassword = '';
        this.newPassword = '';
        this.confirmPassword = '';
      }
    }
  }
  </script>
  
  <style scoped>
  @keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
  }
  
  .animate-fade-in {
    animation: fadeIn 0.5s ease-out;
  }
  </style>
  
  

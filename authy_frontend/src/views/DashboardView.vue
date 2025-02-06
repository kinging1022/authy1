<template>
    <div class="flex w-full min-h-screen bg-emerald-50">
      <!-- Sidebar -->
      <div class="w-64 bg-white border-r border-emerald-100 p-4">
        <div class="flex items-center gap-2 mb-8">
          <Shield class="w-8 h-8 text-emerald-600" />
          <h1 class="text-xl font-semibold text-emerald-900">Authy Dashboard</h1>
        </div>
        <nav class="space-y-1">
          <a
            v-for="(item, index) in navItems"
            :key="index"
            href="#"
            :class="[
              'flex items-center gap-2 px-4 py-2 rounded-lg transition-colors duration-200',
              item.active
                ? 'text-emerald-900 bg-emerald-50'
                : 'text-gray-600 hover:bg-emerald-50'
            ]"
            @click.prevent="handleNavClick(item)"
          >
            <component :is="item.icon" class="w-5 h-5" />
            {{ item.label }}
          </a>
        </nav>
      </div>
  
      <!-- Main Content -->
      <div class="flex-1 p-8">
        <div class="max-w-6xl mx-auto">
          <!-- Welcome Message -->
          <div class="flex justify-between items-center mb-8">
            <div class="flex items-center gap-4">
              <div class="w-12 h-12 rounded-full bg-emerald-100 flex items-center justify-center">
                <UserCircle class="w-8 h-8 text-emerald-600" />
              </div>
              <div>
                <h2 class="text-2xl font-semibold text-gray-800">
                  Welcome back, {{ userStore.user.username }}
                </h2>
                <p class="text-gray-500">Authenticated User</p>
              </div>
            </div>
            <button class="p-2 hover:bg-emerald-50 rounded-full transition-colors duration-200">
              <Bell class="w-6 h-6 text-gray-600" />
            </button>
          </div>
  
          <!-- Dashboard Overview or Edit Password -->
          <div v-if="currentView === 'dashboard'" class="animate-fade-in">
            <div class="bg-white rounded-xl border border-emerald-100 p-6">
              <h3 class="text-lg font-medium text-gray-800 mb-4">Dashboard Overview</h3>
              <p class="text-gray-600 mb-4">
                This is a simplified dashboard overview. Add your custom content here.
              </p>
              <div 
                v-for="(item, index) in dashboardItems" 
                :key="index"
                class="bg-emerald-50 p-4 rounded-lg mb-4 transform transition-all duration-300 hover:scale-105"
                :style="{ animationDelay: `${index * 100}ms` }"
              >
                <h4 class="text-emerald-700 font-medium">{{ item.title }}</h4>
                <p class="text-emerald-600">{{ item.description }}</p>
              </div>
            </div>
          </div>
  
          <div v-else-if="currentView === 'editPassword'" class="animate-fade-in">
            <button
              @click="currentView = 'dashboard'"
              class="mb-4 px-4 py-2 bg-emerald-600 text-white rounded-md hover:bg-emerald-700 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:ring-offset-2 transition-colors duration-200"
            >
              Back to Dashboard
            </button>
            <EditPassword />
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { Shield, UserCircle, Bell, LayoutDashboard, Settings, LogOut } from 'lucide-vue-next'
  import EditPassword from "@/components/EditPassword.vue";  
  import { useUserStore } from "@/stores/user";
  import { useToastStore } from "@/stores/toast";
  export default {
    name: 'Dashboard',
    components: {
      Shield,
      UserCircle,
      Bell,
      LayoutDashboard,
      Settings,
      LogOut,
      EditPassword
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
        username: 'Alex',
        currentView: 'dashboard',
        navItems: [
          { label: 'Home', icon: LayoutDashboard, active: true },
          { label: 'Edit Password', icon: UserCircle, active: false },
          { label: 'Settings', icon: Settings, active: false },
          { label: 'Logout', icon: LogOut, active: false },
        ],
        dashboardItems: [
          { title: 'Item 1', description: 'Description for Item 1' },
          { title: 'Item 2', description: 'Description for Item 2' },
          { title: 'Item 3', description: 'Description for Item 3' },
        ]
      }
    },
    methods: {
      handleNavClick(item) {
        this.navItems.forEach(navItem => navItem.active = false);
        item.active = true;
  
        if (item.label === 'Edit Password') {
          this.currentView = 'editPassword';
        } else if(item.label === 'Home') {
          this.$router.push('/')
        }
        
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
  
  

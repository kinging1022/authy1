<template>
  <div class="w-full min-h-screen bg-white">
    <header>
      <nav class="bg-white shadow-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="flex justify-between h-16 items-center">
            <div class="flex-shrink-0 flex items-center">
              <RouterLink to="/">
                <span class="text-2xl font-bold text-emerald-800">Authy</span>
              </RouterLink>
            </div>
            <div class="hidden md:flex items-center space-x-8">
              <RouterLink to="/" class="block px-3 py-2 text-gray-600 hover:text-emerald-700">Home</RouterLink>
              
              <!-- Show these only if the user is authenticated -->
              <template v-if="userStore.user.isAuthenticated">
                <RouterLink to="/dashboard" class="text-gray-600 hover:text-emerald-700">Dashboard</RouterLink>
                <button @click="LogOut" class="text-gray-600 hover:text-emerald-700">Logout</button>
              </template>

              <!-- Show these only if the user is NOT authenticated -->
              <template v-else>
                <RouterLink to="/login" class="text-gray-600 hover:text-emerald-700">Login</RouterLink>
                <RouterLink to="/signup" class="text-gray-600 hover:text-emerald-700">Sign up</RouterLink>
              </template>
            </div>
          </div>
        </div>
      </nav>
    </header>

    <RouterView />
    <Toast />
  </div>
</template>

<script>
import { RouterLink, RouterView } from 'vue-router'
import Toast from "@/components/Toast.vue";
import { useUserStore } from "@/stores/user";

export default {
  name: 'App',
  components: {
    Toast,
  },
  setup() {
    const userStore = useUserStore();

    return {
      userStore,
    };
  },
  methods: {
    LogOut() {
      this.userStore.removeToken();
      this.$router.push('/');
    }
  },
  mounted() {      
    this.userStore.initStore();
  },
};
</script>


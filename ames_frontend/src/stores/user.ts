// stores/user.js
import { defineStore } from 'pinia'
import api from '@/api/axios'
        
export const useUserStore = defineStore('user', {
  state: () => ({
    user: null,
    loaded: false
  }),

  actions: {
    async fetchUser() {
      const token = localStorage.getItem("access")
      if (!token) return
      if (this.user && this.loaded) return  
      try {
        const res = await api.get('api/users/me')
        this.user = res.data
        this.loaded = true
      } catch (err) {
        console.error(err)
        this.loaded = false
        this.user = null
      }
    }
  }
})
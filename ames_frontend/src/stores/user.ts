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
      if (this.loaded) return  

      try {
        const res = await api.get('api/users/me')
        this.user = res.data
        this.loaded = true
      } catch (err) {
        console.error(err)
      }
    }
  }
})
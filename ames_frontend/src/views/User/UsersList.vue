<template>
    <admin-layout>
      <h1 class="text-center mb-3">Gestione Utenti</h1>
      <BasicTableUsers :data="users" :fetchUsers="fetchUsers" :apiUrl="apiUrl" />
    </admin-layout>
</template>

<script setup>
import AdminLayout from '@/components/layout/AdminLayout.vue'
import BasicTableUsers from '@/components/tables/basic-tables/BasicTableUsers.vue'
import { ref, onMounted } from 'vue'
import api from '@/api/axios'

const users = ref([])
const apiUrl = 'api/users/'

const fetchUsers = async (url = apiUrl) => {
  try {
    const response = await api.get(url)
    users.value = response.data
  } catch (err) {
    console.error(err)
  }
}

onMounted(() => {
  fetchUsers()
})
</script>

<template>
    <admin-layout>
    <h1 class="text-center mb-3">Gestione Corse</h1>
    <BasicTableOne :data="corse" :fetchCorse="fetchCorse" :apiUrl="apiUrl" />
    </admin-layout>

</template>

<script setup>
import AdminLayout from '@/components/layout/AdminLayout.vue'
import BasicTableOne from '@/components/tables/basic-tables/BasicTableOne.vue'
import { ref, onMounted } from 'vue'
import axios from 'axios'
import api from "@/api/axios";

const corse = ref([])
const errore = ref(null)
const apiUrl = 'api/corsas/'

// Funzione per recuperare le corse dal backend
// L’URL può già contenere query params costruiti dal figlio
const fetchCorse = async (url = apiUrl) => {
  try {
    const response = await api.get(url);
    corse.value = response.data;
    console.log(response.data);
  } catch (err) {
    console.error(err);
  }
}
// Carica dati iniziali
onMounted(() => {
  fetchCorse() // usa l’URL di default, senza filtri
})
</script>



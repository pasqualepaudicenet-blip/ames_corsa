<template>
    <admin-layout>
    <h1 class="text-center mb-3">Gestione Corse</h1>
    <BasicTableOne :data="corse" :fetchCorse="fetchCorse" :apiUrl="apiUrl" />
    </admin-layout>

</template>

<script setup>
import AdminLayout from '../components/layout/AdminLayout.vue'
import BasicTableOne from '../components/tables/basic-tables/BasicTableOne.vue'
import { ref, onMounted } from 'vue'
import axios from 'axios'

const corse = ref([])
const errore = ref(null)
const apiUrl = 'http://127.0.0.1:8000/api/corsas/'

// Funzione per recuperare le corse dal backend
// L’URL può già contenere query params costruiti dal figlio
const fetchCorse = async (url = apiUrl) => {
  try {
    const response = await axios.get(url)
    corse.value = response.data
  } catch (err) {
    errore.value = "Errore nel caricamento dati: " + err.message
  }
}

// Carica dati iniziali
onMounted(() => {
  fetchCorse() // usa l’URL di default, senza filtri
})
</script>






<template>
    <admin-layout>

    <h1 class="text-center mb-3">Gestione Corse</h1>
    <BasicTableOne :data="corse" />
    </admin-layout>

</template>

<script setup>
import AdminLayout from '../components/layout/AdminLayout.vue'
import BasicTableOne from '../components/tables/basic-tables/BasicTableOne.vue'
import { ref, onMounted } from 'vue'
import axios from 'axios'

const corse = ref([])
const errore = ref(null)

// Funzione per recuperare le corse dal tuo backend Django
const fetchCorse = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/api/corsas/')
    corse.value = response.data.results
  } catch (err) {
    errore.value = "Errore nel caricamento dati: " + err.message
  }
}
onMounted(() => {
  fetchCorse()
})
</script>
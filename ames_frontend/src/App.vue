<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import { ref, onMounted } from 'vue'
import axios from 'axios'

const corse = ref([])
const errore = ref(null)

// Funzione per recuperare le corse dal tuo backend Django
const fetchCorse = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/api/corsas/')
    console.log(response.data)
    corse.value = response.data
  } catch (err) {
    errore.value = "Errore nel caricamento dati: " + err.message
  }
}

onMounted(() => {
  fetchCorse()
})
</script>

<template>
  <main>
    <h1>Gestione Corse</h1>
    
    <div v-if="errore" style="color: red">{{ errore }}</div>

    <ul v-else>
      <li v-for="corsa in corse" :key="corsa.id">
        <strong>
            Descrizione: {{ corsa.description }}
          
        </strong> 
        <p>
          Tipo: {{ corsa.type }}
        </p>
        <!-- Se hai incluso i samples nel serializer -->
        <ul>
          <li v-for="s in corsa.samples" :key="s.sampleId">
            SampleName: {{ s.sampleName }}
          </li>
        </ul>
      </li>
    </ul>
  </main>
</template>
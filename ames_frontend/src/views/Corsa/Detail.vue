<template>
    <admin-layout>
        <div class="container-fluid d-flex flex-column align-items-center border  rounded shadow detail-card">
            <h1 class="mt-3 mb-4">Dettaglio corsa</h1>
            
            <ul v-if="corsa">
                <li>
                    <strong>ID</strong> = {{corsa.date}}
                </li>
                <li>
                    <strong>Descrizione</strong> = {{corsa.description}}
                </li>
                <li>
                    <strong>Tipo</strong>= {{corsa.type}}
                </li>
                <li>
                    <strong>Path di derivazione </strong>= {{corsa.derivation_path}}
                </li>
                <div v-if="corsa.samples.length > 0" class="mt-5 overflow-hidden rounded-xl  d-flex flex-column align-items-center">
                    <div>
                        <h2 ">Sample collegati</h2>
                    </div>
                    <div class="w-100">
                        <table class="vw-75 border border-gray-200 bg-white w-100 table-striped
                            dark:border-gray-800 dark:bg-white/[0.03] table-responsive table-bordered rounded-x1">
                            <thead >
                                <th class="px-5 py-3 text-center w-50" >ID</th>
                                <th class="px-5 py-3 text-center w-50">Nome</th>
                            </thead>
                            <tbody class="divide-y  divide-gray-200">
                                <tr v-for="sample in corsa.samples">
                                    <td class="py-4 sm:px-6  text-center ">{{ sample.sample_id }}</td>
                                    <td class="py-4 sm:px-6  text-center">{{ sample.sample_name }}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </ul>
        </div>
    </admin-layout>
    
</template>

<script setup>
import AdminLayout from '../../components/layout/AdminLayout.vue'
import { ref, onMounted, watch  } from 'vue'
import axios from 'axios'
import { useRoute } from 'vue-router'
import { isConstructorDeclaration } from 'typescript'

const route = useRoute()

const corsa = ref(null)
const errore = ref(null)

const getCorsa = async () => {
    const id = route.params.id
    const apiUrl = `http://127.0.0.1:8000/api/corsas/${id}`

    try {
      const response = await axios.get(apiUrl)
      corsa.value = response.data
    } catch (err) {
      errore.value = "Errore nel caricamento dati: " + err.message
    }
}
onMounted(() => {
  getCorsa() 
})

</script>
 <style>
 .detail-card:hover{overflow: auto;}
.detail-card{
    height: 100%;
    overflow: hidden;
}

</style>
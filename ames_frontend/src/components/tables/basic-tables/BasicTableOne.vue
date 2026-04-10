<template>
  <div class="container d-flex flex-column align-items-center">
     <div class=" input-group  mt-1 mb-2 d-flex justify-content-end"">
    <div class=" d-flex justify-content-around align-items-center ">
      <div class="d-flex flex-column justify-content-center mr-3">
        <svg width="24" height="24" fill="none" viewBox="0 0 24 24">
          <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19.25 19.25L15.5 15.5M4.75 11C4.75 7.54822 7.54822 4.75 11 4.75C14.4518 4.75 17.25 7.54822 17.25 11C17.25 14.4518 14.4518 17.25 11 17.25C7.54822 17.25 4.75 14.4518 4.75 11Z"></path>
        </svg>
      </div>
      <input v-model="searchDesc"  type="search" class="px-2   border border-top form-control mr-2"  placeholder="Descrizione">
      <input  v-model="searchType"  type="search" class="px-2   border border-top form-control"  placeholder="Tipo">
    </div>
  </div>
  <div class="overflow-hidden rounded-xl border border-gray-200 bg-white dark:border-gray-800 dark:bg-white/[0.03]" >
    <div class=" overflow-x-auto custom-scrollbar" >
      
      
      <table class="vw-75">
        <thead>
          <tr class="border-b border-gray-200 dark:border-gray-700">
            <th class="px-5 py-3 text-left w-3/11 sm:px-6">
              <p class="font-medium text-gray-500 text-theme-xs dark:text-gray-400">Data</p>
            </th>
            <th class="px-5 py-3 text-left w-2/11 sm:px-6">
              <p class="font-medium text-gray-500 text-theme-xs dark:text-gray-400">Descrizione</p>
            </th>
            <th class="px-5 py-3 text-left w-2/11 sm:px-6">
              <p class="font-medium text-gray-500 text-theme-xs dark:text-gray-400">Tipo</p>
            </th>
            <th class="px-5 py-3 text-left w-2/11 sm:px-6">
              <p class="font-medium text-gray-500 text-theme-xs dark:text-gray-400">Path di derivazione</p>
            </th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-200 dark:divide-gray-700">
          <tr v-for="corsa in data.results" :key="corsa.id" class="border-t border-gray-100 dark:border-gray-800">
            <td class=" py-4 sm:px-6">
              {{ corsa.date }}
            </td>
            <td class=" py-4 sm:px-6">
              <p class="text-gray-500 text-theme-sm dark:text-gray-400">{{ corsa.description }}</p>
            </td>
            <td class=" py-4 sm:px-6">
              <p class="text-gray-500 text-theme-sm dark:text-gray-400">{{ corsa.type }}</p>
            </td>
            <td class=" py-4 sm:px-6">
              <p class="text-gray-500 text-theme-sm dark:text-gray-400">{{ corsa.derivation_path }}</p>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div data-v-9b3943d3="" class="px-6 py-4 border-t border-gray-200 dark:border-white/[0.05]">
      <div data-v-9b3943d3="" class="flex items-center justify-between">
       <button  @click="props.fetchCorse(data.previous)">
          previous
       </button>
       <button  @click="props.fetchCorse(data.next)">
          NEXT
       </button>
      </div>
    </div>

  </div>



  </div>
 
</template>
<script setup>
import { ref, watch } from 'vue'
const props = defineProps({
  data: Object,
  fetchCorse: Function,
  apiUrl: Text,
});

const searchDesc = ref('')
const searchType = ref('')

let timeout
watch([searchDesc, searchType], () => {
  clearTimeout(timeout)
  
  timeout = setTimeout(() => {
    // Chiamata live solo se la lunghezza >=3 o campo vuoto (per resettare)
    if ((searchDesc.value.length >= 3 || searchDesc.value === '') &&
        (searchType.value.length >= 3 || searchType.value === '')) {
      let url = props.apiUrl || ''  
      const params = new URLSearchParams()
      if (searchDesc.value) params.append('description', searchDesc.value)
      if (searchType.value) params.append('type', searchType.value)
      if (url.includes('?')) {
        url = url.split('?')[0] + '?' + params.toString()
      } else if (params.toString()) {
        url = url + '?' + params.toString()
      }
      props.fetchCorse(url)
    }
  }, 300)
 }) 
</script>

<style scoped>
/* Add any additional styles here if needed */
</style>

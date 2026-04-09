<template>
  <div class="overflow-hidden rounded-xl border border-gray-200 bg-white dark:border-gray-800 dark:bg-white/[0.03]">
    <div class="max-w-full overflow-x-auto custom-scrollbar">
      <div class="search-bar">
        <div class="input-group">
            <input v-model="searchDesc"  type="search" class="px-2 ml-4 mt-2 border border-top form-control mr-sm-2"  placeholder="Descrizione">
            <button class="btn btn-outline-secondary" type="button" id="search-addon">
                    <i class="fas fa-search"></i>
                </button>
        </div>
    </div>
      
      <input  v-model="searchType"  type="search" class="px-2 ml-4 mt-2 border border-top form-control mr-sm-2"  placeholder="Tipo">
      <table class="min-w-full">
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
            <td class="px-5 py-4 sm:px-6">
              <p class="text-gray-500 text-theme-sm dark:text-gray-400">{{ corsa.date }}</p>
            </td>
            <td class="px-5 py-4 sm:px-6">
              <p class="text-gray-500 text-theme-sm dark:text-gray-400">{{ corsa.description }}</p>
            </td>
            <td class="px-5 py-4 sm:px-6">
              <p class="text-gray-500 text-theme-sm dark:text-gray-400">{{ corsa.type }}</p>
            </td>
            <td class="px-5 py-4 sm:px-6">
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

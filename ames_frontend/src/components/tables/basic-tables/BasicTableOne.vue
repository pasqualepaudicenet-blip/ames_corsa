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
  <div class="w-100 overflow-hidden rounded-xl border border-gray-200 bg-white dark:border-gray-800 dark:bg-white/[0.03] shadow"  >
    <div data-v-9b3943d3="" class="flex items-center justify-around p-3">
          <div  class="col-4 d-flex justify-content-start">
            <button v-if="data.previous" @click="props.fetchCorse(data.previous)" class="border border-grey px-3  bigger-on-hover" title="Pagina precedente">
               <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" height="24" width="24">
                  <g id="arrow-dash-left">
                    <path id="Union" fill="#000000" d="M8.54297 5.54333c0.39054 -0.39029 1.02361 -0.39044 1.41406 0 0.39037 0.39046 0.39027 1.02356 0 1.41407l-4.04297 4.043H12c0.5521 0.0001 1 0.4478 1 1 -0.0002 0.552 -0.448 0.9998 -1 1H5.91406l4.04297 4.0429c0.39037 0.3905 0.39027 1.0236 0 1.4141 -0.39049 0.3905 -1.02353 0.3904 -1.41406 0l-5.75 -5.75c-0.39053 -0.3905 -0.39053 -1.0235 0 -1.4141zM17 11.0004c0.5521 0.0001 1 0.4478 1 1 -0.0002 0.552 -0.448 0.9998 -1 1h-1c-0.5522 0 -0.9998 -0.4479 -1 -1 0 -0.5523 0.4477 -1 1 -1zm4 0c0.5521 0.0001 1 0.4478 1 1 -0.0002 0.552 -0.448 0.9998 -1 1 -0.5522 0 -0.9998 -0.4479 -1 -1 0 -0.5523 0.4477 -1 1 -1" stroke-width="1"></path>
                  </g>
              </svg>
              </button>
          </div>
          <div  class="col-4 d-flex justify-content-center">
              <button 
                v-for="page in data.total_pages" 
                @click="props.fetchCorse(get_url(page))" 
                class="border border-grey px-3 bigger-on-hover " 
                :class="{ 
                  'bg-primary text-white': data.current_page === page,
                  'bg-white': data.current_page !== page
                  }">
                    {{ page }}
              </button>
          </div>
        <div  class="col-4 d-flex justify-content-end"> 
          <button   v-if="data.next" @click="props.fetchCorse(data.next)" class="border border-grey px-3  bigger-on-hover">
              <svg class="rotate-180" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" height="24" width="24">
                  <g id="arrow-dash-left">
                    <path id="Union" fill="#000000" d="M8.54297 5.54333c0.39054 -0.39029 1.02361 -0.39044 1.41406 0 0.39037 0.39046 0.39027 1.02356 0 1.41407l-4.04297 4.043H12c0.5521 0.0001 1 0.4478 1 1 -0.0002 0.552 -0.448 0.9998 -1 1H5.91406l4.04297 4.0429c0.39037 0.3905 0.39027 1.0236 0 1.4141 -0.39049 0.3905 -1.02353 0.3904 -1.41406 0l-5.75 -5.75c-0.39053 -0.3905 -0.39053 -1.0235 0 -1.4141zM17 11.0004c0.5521 0.0001 1 0.4478 1 1 -0.0002 0.552 -0.448 0.9998 -1 1h-1c-0.5522 0 -0.9998 -0.4479 -1 -1 0 -0.5523 0.4477 -1 1 -1zm4 0c0.5521 0.0001 1 0.4478 1 1 -0.0002 0.552 -0.448 0.9998 -1 1 -0.5522 0 -0.9998 -0.4479 -1 -1 0 -0.5523 0.4477 -1 1 -1" stroke-width="1"></path>
                  </g>
            </svg>
        </button>
        </div>
       
      </div>
    <div class=" overflow-x-auto custom-scrollbar" >
      <table class=" table-fixed"  >
        <thead class="">
          <tr>
             <th  class=" px-5 py-3 text-left w-3/11 text-center sm:px-6">
              <p class="font-medium text-gray-500 text-theme-xs dark:text-gray-400 text-center">Data</p>
            </th>
            <th  class=" px-2 py-3 text-left w-2/11 text-center sm:px-6">
              <p class="font-medium text-gray-500 text-theme-xs dark:text-gray-400">Descrizione</p>
            </th>
            <th class=" px-2 py-3 text-left text-center w-2/11 sm:px-6 overlow-auto">
              <p class="font-medium text-gray-500 text-theme-xs dark:text-gray-400">Tipo</p>
            </th>
            <th class=" px-2 py-3 text-left text-center w-2/11 sm:px-6 overlow-auto">
              <p  class="font-medium text-gray-500 text-theme-xs dark:text-gray-400">Path di derivazione</p>
            </th>
            <th  class=" px- py-3 text-left text-center w-2/11 sm:px-6">
              <p class="text-center  font-medium text-gray-500 text-theme-xs dark:text-gray-400">Azioni</p>
            </th>
          </tr>
           
        </thead>
        <tbody class="divide-y divide-gray-200 dark:divide-gray-700">
          <tr v-for="corsa in data.results" :key="corsa.id" class="border-t border-gray-100 dark:border-gray-800">
            <td class=" py-4 sm:px-2 text-center" >
              {{ corsa.date }}
            </td>
            <td class=" text-center sm:px-2 cell-overable">
                {{ corsa.description }}
              
            </td>
            <td class=" py-4 text-center sm:px-2 cell-overable"             
                >
             {{ corsa.type }}
            </td>
            <td class=" text-center py-4 sm:px-2 cell-overable"             
                
            >
              {{ corsa.derivation_path }}
            </td>
            <td class=" py-4 sm:px-6 d-flex justify-content-center" >
              <router-link class="btn bg-primary bigger-on-hover" title="Dettagli" :to="{ name: 'CorsaDetail', params: { id: corsa.pk} }">
                <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="20" height="20" viewBox="0,0,256,256">
                  <g fill="none" fill-rule="nonzero" stroke="none" stroke-width="none" stroke-linecap="none" stroke-linejoin="none" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" font-family="none" font-weight="none" font-size="none" text-anchor="none" style="mix-blend-mode: normal"><g transform="scale(5.33333,5.33333)"><path d="M31.4,41c-2.3,1 -4.8,1.5 -7.4,1.5c-10.2,0 -18.5,-8.3 -18.5,-18.5c0,-4.5 1.6,-8.6 4.2,-11.8" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"></path><path d="M16.3,7.2c2.3,-1.1 5,-1.7 7.7,-1.7c10.2,0 18.5,8.3 18.5,18.5c0,4 -1.3,7.7 -3.4,10.7" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"></path><circle cx="24" cy="16" r="2" fill="#ffffff" stroke="none" stroke-width="1" stroke-linecap="butt" stroke-linejoin="miter"></circle><path d="M24,22.5v11" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round" stroke-linejoin="miter"></path></g></g>
                </svg>  
              </router-link>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div data-v-9b3943d3="" class="px-6 py-4 border-t border-gray-200 dark:border-white/[0.05]">
      <div data-v-9b3943d3="" class="flex items-center justify-around">
          <div class="col-4 d-flex justify-content-start">
            <button v-if="data.previous" @click="props.fetchCorse(data.previous)" class="border border-grey px-3  bigger-on-hover" title="Pagina precedente">
               <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" height="24" width="24">
                  <g id="arrow-dash-left">
                    <path id="Union" fill="#000000" d="M8.54297 5.54333c0.39054 -0.39029 1.02361 -0.39044 1.41406 0 0.39037 0.39046 0.39027 1.02356 0 1.41407l-4.04297 4.043H12c0.5521 0.0001 1 0.4478 1 1 -0.0002 0.552 -0.448 0.9998 -1 1H5.91406l4.04297 4.0429c0.39037 0.3905 0.39027 1.0236 0 1.4141 -0.39049 0.3905 -1.02353 0.3904 -1.41406 0l-5.75 -5.75c-0.39053 -0.3905 -0.39053 -1.0235 0 -1.4141zM17 11.0004c0.5521 0.0001 1 0.4478 1 1 -0.0002 0.552 -0.448 0.9998 -1 1h-1c-0.5522 0 -0.9998 -0.4479 -1 -1 0 -0.5523 0.4477 -1 1 -1zm4 0c0.5521 0.0001 1 0.4478 1 1 -0.0002 0.552 -0.448 0.9998 -1 1 -0.5522 0 -0.9998 -0.4479 -1 -1 0 -0.5523 0.4477 -1 1 -1" stroke-width="1"></path>
                  </g>
              </svg>
              </button>
          </div>
          <div class="col-4 d-flex justify-content-center">
              <button 
                v-for="page in data.total_pages" 
                @click="props.fetchCorse(get_url(page))" 
                class="border border-grey px-3 bigger-on-hover " 
                :class="{ 
                  'bg-primary text-white': data.current_page === page,
                  'bg-white': data.current_page !== page
                  }">
                    {{ page }}
              </button>
              
          </div>
         <div class="col-4 d-flex justify-content-end"> 
          <button   v-if="data.next" @click="props.fetchCorse(data.next)" class="border border-grey px-3  bigger-on-hover">
              <svg class="rotate-180" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" height="24" width="24">
                  <g id="arrow-dash-left">
                    <path id="Union" fill="#000000" d="M8.54297 5.54333c0.39054 -0.39029 1.02361 -0.39044 1.41406 0 0.39037 0.39046 0.39027 1.02356 0 1.41407l-4.04297 4.043H12c0.5521 0.0001 1 0.4478 1 1 -0.0002 0.552 -0.448 0.9998 -1 1H5.91406l4.04297 4.0429c0.39037 0.3905 0.39027 1.0236 0 1.4141 -0.39049 0.3905 -1.02353 0.3904 -1.41406 0l-5.75 -5.75c-0.39053 -0.3905 -0.39053 -1.0235 0 -1.4141zM17 11.0004c0.5521 0.0001 1 0.4478 1 1 -0.0002 0.552 -0.448 0.9998 -1 1h-1c-0.5522 0 -0.9998 -0.4479 -1 -1 0 -0.5523 0.4477 -1 1 -1zm4 0c0.5521 0.0001 1 0.4478 1 1 -0.0002 0.552 -0.448 0.9998 -1 1 -0.5522 0 -0.9998 -0.4479 -1 -1 0 -0.5523 0.4477 -1 1 -1" stroke-width="1"></path>
                  </g>
            </svg>
        </button>
        </div>
       
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
  apiUrl: String,
});

const searchDesc = ref('')
const searchType = ref('')
const current_url = ref('')
let timeout

current_url.value = props.apiUrl

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
      current_url.value = url
      props.fetchCorse(url)
    }
  }, 300)
 }) 


 function get_url(page){
   if (current_url.value.includes('?')) {
        current_url.value = current_url.value.split('?')[0] + '?' + current_url.value.split('?')[1]
        if(current_url.value.includes('page=')) {
          current_url.value = current_url.value.split('?')[0] + '?' + current_url.value.split('?')[1].split('&').filter(param => !param.startsWith('page=')).join('&')
        }
        current_url.value = current_url.value + '&' + 'page=' + page
    } else {
      current_url.value = current_url.value + '?' + 'page=' + page
    }
    return current_url.value
    }
</script>

<style>
:root {
  --zoom-1-2: 1.1;
}
.bigger-on-hover:hover{
  transform: scale(var(--zoom-1-2));
  transform-origin: center;
}
.table-fixed {
  table-layout: fixed;
  width: 100%;
}

.cell-overable{
  overflow: hidden;
}

.cell-overable:hover{
  overflow: auto;
}
</style>

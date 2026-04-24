<template>
    <admin-layout>
        <router-link :to="{ name : 'UsersList' }" class="btn btn-outline-primary  align-self-start px-3 py-1 my-2"> Torna alla lista</router-link>
            <h1 class="mt-3 mb-4 text-center">Dettaglio Utente</h1>

        <div class="container-fluid d-flex flex-column align-items-center border col-6 py-3 h-70 rounded shadow detail-card">

            <div v-if="user" class="" role="alert">
                <div>
                  <h6 class="d-inline"> Username: {{ user.username }}</h6> 
                </div>
                <div>
                  <p class="d-inline"> Email: {{ user.email }}</p> 
                </div>
                <div>
                 Superuser: 
                  <p v-if="user.is_superuser" class="d-inline"> 
                    <svg  class="d-inline" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" id="Check--Streamline-Ultimate" height="24" width="24">
                      <desc>
                        Check Streamline Icon: https://streamlinehq.com
                      </desc>
                      <path fill="#78eb7b" d="M1.98657 13.7043c-0.4235 0.4235 -0.4235 1.1101 0 1.5336l5.20337 5.2042c0.42414 0.4225 1.11017 0.4225 1.53441 0L22.013 7.1525c0.4235 -0.42341 0.4235 -1.10999 0 -1.53349l-2.0591 -2.05994c-0.4235 -0.42414 -1.1108 -0.42414 -1.5344 0L7.9571 14.0224l-2.37701 -2.3781c-0.42378 -0.4235 -1.11073 -0.4235 -1.53441 0l-2.05911 2.06Z" stroke-width="1"></path>
                      <path fill="#c9f7ca" d="M7.95731 17.1666 20.7591 4.3649l-0.8086 -0.8085c-0.4238 -0.42359 -1.1106 -0.42359 -1.5344 0L7.95731 14.0224 5.5803 11.6443c-0.42359 -0.424 -1.1109 -0.424 -1.5344 0l-0.8086 0.8086 4.72001 4.7137Z" stroke-width="1"></path>
                      <path stroke="#191919" stroke-linecap="round" stroke-linejoin="round" d="M1.98657 13.7043c-0.4235 0.4235 -0.4235 1.1101 0 1.5336l5.20337 5.2042c0.42414 0.4225 1.11017 0.4225 1.53441 0L22.013 7.1525c0.4235 -0.42341 0.4235 -1.10999 0 -1.53349l-2.0591 -2.05994c-0.4235 -0.42414 -1.1108 -0.42414 -1.5344 0L7.9571 14.0224l-2.37701 -2.3781c-0.42378 -0.4235 -1.11073 -0.4235 -1.53441 0l-2.05911 2.06Z" stroke-width="1"></path>
                    </svg>
                </p> 
                  <p v-else class="d-inline pl-3"> 
                    <svg  class="d-inline " xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" id="Remove-Bold--Streamline-Ultimate" height="24" width="24">
                      <desc>
                        Remove Bold Streamline Icon: https://streamlinehq.com
                      </desc>
                      <path fill="#ff808c" d="m7.4502 12 -6.3627 6.3627c-0.1895 0.1894 -0.296 0.4466 -0.296 0.7147s0.1065 0.5253 0.296 0.7148l3.1202 3.1203c0.1896 0.1894 0.4467 0.296 0.7148 0.296s0.5252 -0.1066 0.7148 -0.296L12 16.5498l6.3627 6.3627c0.1895 0.1894 0.4467 0.296 0.7148 0.296 0.268 0 0.5251 -0.1066 0.7147 -0.296l3.1203 -3.1203c0.1895 -0.1895 0.296 -0.4467 0.296 -0.7148s-0.1065 -0.5253 -0.296 -0.7147L16.5498 12l6.3627 -6.3627c0.1895 -0.1896 0.296 -0.4467 0.296 -0.7148s-0.1065 -0.5252 -0.296 -0.7148l-3.1203 -3.1202c-0.1896 -0.1895 -0.4467 -0.296 -0.7147 -0.296 -0.2681 0 -0.5253 0.1065 -0.7148 0.296L12 7.4502 5.6373 1.0875c-0.1896 -0.1895 -0.4467 -0.296 -0.7148 -0.296s-0.5252 0.1065 -0.7148 0.296L1.0875 4.2077c-0.1895 0.1896 -0.296 0.4467 -0.296 0.7148s0.1065 0.5252 0.296 0.7148L7.4502 12Z" stroke-width="1"></path>
                      <path fill="#ffbfc5" d="m1.0875 19.7922 1.5601 1.5601L21.3524 2.6476l-1.5602 -1.5601c-0.1896 -0.1895 -0.4467 -0.296 -0.7147 -0.296 -0.2681 0 -0.5253 0.1065 -0.7148 0.296L12 7.4502 5.6373 1.0875c-0.1896 -0.1895 -0.4467 -0.296 -0.7148 -0.296s-0.5252 0.1065 -0.7148 0.296L1.0875 4.2077c-0.1895 0.1896 -0.296 0.4467 -0.296 0.7148s0.1065 0.5252 0.296 0.7148L7.4502 12l-6.3627 6.3627c-0.1895 0.1894 -0.296 0.4466 -0.296 0.7147s0.1065 0.5253 0.296 0.7148Z" stroke-width="1"></path>
                      <path stroke="#191919" stroke-linecap="round" stroke-linejoin="round" d="m7.4502 12 -6.3627 6.3627c-0.1895 0.1894 -0.296 0.4466 -0.296 0.7147s0.1065 0.5253 0.296 0.7148l3.1202 3.1203c0.1896 0.1894 0.4467 0.296 0.7148 0.296s0.5252 -0.1066 0.7148 -0.296L12 16.5498l6.3627 6.3627c0.1895 0.1894 0.4467 0.296 0.7148 0.296 0.268 0 0.5251 -0.1066 0.7147 -0.296l3.1203 -3.1203c0.1895 -0.1895 0.296 -0.4467 0.296 -0.7148s-0.1065 -0.5253 -0.296 -0.7147L16.5498 12l6.3627 -6.3627c0.1895 -0.1896 0.296 -0.4467 0.296 -0.7148s-0.1065 -0.5252 -0.296 -0.7148l-3.1203 -3.1202c-0.1896 -0.1895 -0.4467 -0.296 -0.7147 -0.296 -0.2681 0 -0.5253 0.1065 -0.7148 0.296L12 7.4502 5.6373 1.0875c-0.1896 -0.1895 -0.4467 -0.296 -0.7148 -0.296s-0.5252 0.1065 -0.7148 0.296L1.0875 4.2077c-0.1895 0.1896 -0.296 0.4467 -0.296 0.7148s0.1065 0.5252 0.296 0.7148L7.4502 12Z" stroke-width="1"></path>
                    </svg>
                </p> 
                </div>
            </div>  
        </div>
    </admin-layout>
    
</template>

<script setup>
import AdminLayout from '../../components/layout/AdminLayout.vue'
import { ref, onMounted, watch  } from 'vue'
import axios from 'axios'
import { useRoute } from 'vue-router'
import { isConstructorDeclaration } from 'typescript'
import api from "@/api/axios";

const route = useRoute()

const user = ref(null)
const errore = ref(null)

const getUser = async () => {
    const id = route.params.id
    const apiUrl = `api/users/${id}`

    try {
      const response = await api.get(apiUrl)
      user.value = response.data
      console.log(user.value)
    } catch (err) {
      errore.value = "Errore nel caricamento dati: " + err.message
    }
}
onMounted(() => {
  getUser() 
})

</script>
 <style>
 .detail-card:hover{overflow: auto;}
.detail-card{
    height: 80%;
    overflow: hidden;
}

</style>
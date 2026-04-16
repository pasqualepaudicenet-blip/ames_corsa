<template>
    <div style="width:350px;height:300px" 
    class=" card rounded-2xl border border-gray-200 bg-white dark:border-gray-800 dark:bg-white/[0.03]  d-flex flex-column cards-hover"
    :class="isHovered ? 'shadow' : 'shadow-sm'"
    @mouseenter="isHovered = true"
    @mouseleave="isHovered = false"
    >
    <router-link :to="{ name: 'CorseList'}" class=" p-5 md:p-6 text-decoration-none h-100 link-dark d-flex flex-column align-items-center justify-content-center">
          <div class="h-25">
            <h3 class="text-center ">Gestione Corse</h3>  
          </div>
          <div class="text-center d-flex align-items-center justify-content-center" >
            <img class="h-50" src="https://img.icons8.com/?size=100&id=37678&format=png&color=000000">
          </div>
      </router-link>
    </div>
</template>

<script setup>
  import { ref } from 'vue'

  const isHovered = ref(false)

</script>
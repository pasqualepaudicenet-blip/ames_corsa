<template>
    <div class="container" @mouseleave="handleMouseLeave" style="position: relative; width: 350px; height: 300px;">
        <div style="width:350px;height:300px; position: relative;" id="run"
        class="card rounded-2xl border border-gray-200 bg-white dark:border-gray-800 dark:bg-white/[0.03] d-flex flex-column cards-hover"
        :class="isHovered ? 'shadow' : 'shadow-sm'"
        :style="{ transform: `translate(${position.x}px, ${position.y}px)` }"
        @mouseenter="isHovered = true"
        @mouseleave="isHovered = false"
        ref="runDiv"
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
    </div>
</template>

<script setup>
  import { ref, reactive } from 'vue'

  const isHovered = ref(false)
  const position = reactive({ x: 0, y: 0 })
  const runDiv = ref(null)

  const handleMouseMove = (event) => {
    if (!runDiv.value) return
    const rect = runDiv.value.getBoundingClientRect()
    const centerX = rect.left + rect.width / 2
    const centerY = rect.top + rect.height / 2
    const mouseX = event.clientX
    const mouseY = event.clientY
    const distance = Math.sqrt((mouseX - centerX) ** 2 + (mouseY - centerY) ** 2)
    const threshold = 700 // distance to start running away
    if (distance < threshold) {
      const angle = Math.atan2(mouseY - centerY, mouseX - centerX)
      const moveDistance = (threshold - distance) / 2
      position.x = -Math.cos(angle) * moveDistance
      position.y = -Math.sin(angle) * moveDistance
    } else {
      position.x = 0
      position.y = 0
    }
  }
</script>
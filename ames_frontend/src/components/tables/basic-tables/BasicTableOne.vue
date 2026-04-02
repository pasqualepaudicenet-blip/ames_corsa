<template>
  <div
    class="overflow-hidden rounded-xl border border-gray-200 bg-white dark:border-gray-800 dark:bg-white/[0.03]"
  >
    <div class="max-w-full overflow-x-auto custom-scrollbar">
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
          <tr
            v-for="corsa in data" :key="corsa.id"
            class="border-t border-gray-100 dark:border-gray-800"
          >
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
  </div>
</template>

<script setup>
import { ref } from 'vue'
    defineProps({
      data: Object
    });
</script>

<style scoped>
/* Add any additional styles here if needed */
</style>

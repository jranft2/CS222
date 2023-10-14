<script setup lang="ts"></script>
<template>
  <div class="w-full border border-gray-200 p-10 rounded-lg overflow-y-auto">
    <div
      class="h-48 w-48 bg-blue-100 rounded-full border-2 border-gray-200"
    ></div>
    <div class="flex gap-3 mt-10 flex-col">
      <div class="mb-6 w-64">
        <label
          for="default-input"
          class="block mb-2 text-sm font-medium text-gray-900"
          >Display Name</label
        >
        <input
          type="text"
          id="default-input"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
        />
      </div>
    </div>
    <uiButton color="blue"> Save </uiButton>
  </div>
</template>

<script lang="ts">
import uiButton from "../ui/uiButton.vue";

export default {
  components: {
    uiButton,
  },
};
</script>

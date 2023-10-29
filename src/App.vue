<script setup lang="ts">
import UserBubble from "./components/UserBubble.vue";
</script>
<template>
  <div class="w-full pt-5 px-5">
    <div class="flex justify-center">
      <div class="max-w-5xl w-full">
        <div class="flex relative items-center justify-between">
          <div class="text-3xl font-medium">{{ $route.name }}</div>
          <UserBubble />
        </div>
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

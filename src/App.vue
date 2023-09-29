<script setup lang="ts">
import UserProfile from "./components/UserProfile.vue";
import UsersList from "./components/UsersList.vue";
</script>

<template>
  <div class="flex justify-center w-full pt-10">
    <div class="flex w-full gap-4 items-start max-w-5xl">
      <UsersList />
      <UserProfile />
    </div>
  </div>
</template>

<style scoped></style>

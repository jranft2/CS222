<script setup lang="ts">
import UserProfile from "../components/UserProfile.vue";
import UsersList from "../components/UsersList.vue";
</script>
<template>
  <div>
    <div class="flex w-full gap-4 mt-3 items-start">
      <UsersList />
      <UserProfile />
    </div>
  </div>
</template>

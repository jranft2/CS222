<script setup lang="ts">
import UserProfile from "../components/UserProfile.vue";
import UsersList from "../components/UsersList.vue";
import UserBubble from "../components/UserBubble.vue";
</script>
<template>
  <div class="w-full pt-5 px-5">
    <div class="flex justify-center">
      <div class="max-w-5xl w-full">
        <div class="flex justify-end">
          <UserBubble />
        </div>
        <div class="flex w-full gap-4 mt-3 items-start">
          <UsersList />
          <UserProfile />
        </div>
      </div>
    </div>
  </div>
</template>

<template>
  <div class="flex w-full gap-4 items-start">
    <UsersList @user-selected="userSelected" />
    <UserProfile
      @hide-profile="hideProfile"
      v-show="profileVisible"
      :user="profUser"
    />
  </div>
</template>

<script setup lang="ts">
import UserProfile from "../components/UserProfile.vue";
import UsersList from "../components/UsersList.vue";

import { ref } from "vue";
let profileVisible = ref(false);
const profUser = ref();

const hideProfile = () => {
  profileVisible.value = false;
  console.log(profileVisible);
};

const userSelected = (user: any) => {
  console.log(profileVisible);
  profileVisible.value = true;
  profUser.value = user;
};
</script>

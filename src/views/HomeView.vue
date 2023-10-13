<template>
  <div class="w-full pt-5 px-5">
    <div class="flex justify-center">
      <div class="max-w-5xl w-full">
        <div class="flex relative justify-end">
          <UserBubble />
        </div>
        <div class="flex w-full gap-4 mt-3 items-start">
          <UsersList @user-selected="userSelected" />
          <UserProfile
            @hide-profile="hideProfile"
            v-show="profileVisible"
            :user="profUser"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import UserProfile from "../components/UserProfile.vue";
import UsersList from "../components/UsersList.vue";
import UserBubble from "../components/UserBubble.vue";
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
  // console.log(profUser.value.name);
};
</script>

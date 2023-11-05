<template>
  <!-- <div class="w-full flex justify-center mt-12 px-10"> -->
  <div class="w-full border border-gray-200 rounded-xl p-5">
    <!-- <router-link :to="{ name: 'home' }"> -->
    <div class="flex flex-col gap-1">
      <div class="text-xl font-medium">CS 241</div>
      <div>System Programming</div>
    </div>
  </div>
  <div class="mt-3">
    <div class="flex w-full gap-4 items-start">
      <UsersList @user-selected="userSelected" />
      <UserProfile
        @hide-profile="hideProfile"
        v-show="profileVisible"
        :user="profUser"
      />
    </div>
  </div>
</template>
<script setup>
import {
  ArrowSmallLeftIcon,
  PencilSquareIcon,
} from "@heroicons/vue/24/outline";
import UserProfile from "../components/UserProfile.vue";
import UsersList from "../components/UsersList.vue";
import { ref } from "vue";

let profileVisible = ref(false);
const profUser = ref();

const hideProfile = () => {
  profileVisible.value = false;
  console.log(profileVisible);
};

const userSelected = (user) => {
  console.log(profileVisible);
  profileVisible.value = true;
  profUser.value = user;
};
</script>

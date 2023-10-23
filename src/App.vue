<script setup lang="ts">
import UserBubble from "./components/UserBubble.vue";
import { HomeIcon } from "@heroicons/vue/24/outline";
</script>
<template>
  <div class="w-full pt-5 px-5">
    <div class="flex justify-center">
      <div class="max-w-5xl w-full">
        <div class="flex relative items-center justify-between">
          <div class="flex gap-4">
            <router-link v-if="$route.name != 'Users'" :to="{ name: 'Users' }">
              <div
                class="duration-75 border border-gray-200 cursor-pointer self-star sm:w-10 w-11 sm:h-10 h-11 hover:border-slate-300 rounded-xl"
              >
                <HomeIcon
                  class="p-2 duration-75 transform shrink-0 hover:scale-110"
                />
              </div>
            </router-link>

            <div class="text-3xl font-medium">{{ $route.name }}</div>
          </div>
          <UserBubble />
        </div>
        <div class="mt-2">
          <router-view></router-view>
        </div>
      </div>
    </div>
  </div>
</template>

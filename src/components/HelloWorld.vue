<template>
  <div class="w-full flex justify-center mt-12 px-10">
    <div class="w-full max-w-4xl border border-gray-200 rounded-xl p-5">
      <!-- <router-link :to="{ name: 'home' }"> -->
      <div class="flex justify-between items-center">
        <div
          class="duration-75 -mt-1 -ml-1 border border-gray-200 cursor-pointer self-star sm:w-10 w-11 sm:h-10 h-11 hover:border-slate-300 rounded-xl"
        >
          <ArrowSmallLeftIcon
            class="p-2 duration-75 transform shrink-0 hover:scale-110"
          />
        </div>
        <div
          class="-mt-1 -mr-1 flex items-center cursor-pointer gap-2 justify-center duration-75 border border-gray-200 self-star px-2 sm:h-10 h-11 hover:border-slate-300 rounded-xl"
        >
          <span class="font-medium underline text-gray-500 underline-offset-2"
            >Edit</span
          >
          <PencilSquareIcon class="w-6 h-6 text-gray-500" />
        </div>
      </div>
      <!-- </router-link> -->
      <div
        class="h-48 w-48 bg-blue-100 rounded-full mt-4 border-2 border-gray-200"
      ></div>
      <div class="text-3xl font-semibold mt-4">[Name]</div>
      <div class="text-xl font-medium mt-2">[Major]</div>

      <div class="flex gap-2 items-center mt-2.5">
        <div
          v-for="x of [1, 2, 3]"
          class="text-md font-md mt-2 bg-purple-200 rounded-full px-2.5 py-1 w-min"
        >
          [Tag{{ x }}]
        </div>
      </div>
    </div>
    <div></div>
  </div>
</template>

<script>
import {
  ArrowSmallLeftIcon,
  PencilSquareIcon,
} from "@heroicons/vue/24/outline";

export default {
  components: {
    ArrowSmallLeftIcon,
    PencilSquareIcon,
  },
};
</script>

<style scoped></style>

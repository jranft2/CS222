<template>
  <!-- <div class="w-full flex justify-center mt-12 px-10"> -->
  <div class="w-full max-w-4xl border border-gray-200 rounded-xl p-5">
    <!-- <router-link :to="{ name: 'home' }"> -->
    <div class="flex justify-between items-center">
      <div
        class="duration-75 -mt-1 -ml-1 border border-gray-200 cursor-pointer self-star sm:w-10 w-11 sm:h-10 h-11 hover:border-slate-300 rounded-xl"
      >
        <ArrowSmallLeftIcon @click="goBack()"
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
    <div v-if="user"
      :style="{background: user.color ?? 'defaultColor' , fontSize: '50px'}"
      class="h-48 w-48 items-center justify-center flex rounded-full mt-4 border-2 border-gray-200"
    >{{ getNameLetters(user.name ??'John Doe') }}</div>
    <div v-if="user" class="text-3xl font-semibold mt-4">{{user.name ??'John Doe'}}</div>
    <div class="text-xl font-medium mt-2">[Major]</div>

    <Tags :user="user" />
  </div>
  <!-- <div></div> -->
  <!-- </div> -->
</template>

<script>
import {
  ArrowSmallLeftIcon,
  PencilSquareIcon,
} from "@heroicons/vue/24/outline";
import Tags from "./Tags.vue";

export default {
  components: {
    ArrowSmallLeftIcon,
    PencilSquareIcon,
    Tags,
  },
  props: {
    user:Object,
  },
  methods: {
    goBack() {
      this.$emit("hideProfile")
    },
    getNameLetters(fullName) {
      const nameParts = fullName.split(" ");
      const firstName = nameParts[0];
      const lastName = nameParts.length > 1 ? nameParts[1] : null;

      if (lastName) {
        const firstInitial = firstName.charAt(0).toUpperCase();
        const lastInitial = lastName.charAt(0).toUpperCase();
        return firstInitial + lastInitial;
      } else {
        return firstName.slice(0, 2).toUpperCase();
      }
    },
  }
};

</script>

<style scoped></style>


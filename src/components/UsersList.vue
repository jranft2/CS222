<template>
  <!-- <div class="w-full max-w-4xl border border-gray-200 rounded-xl p-5"> -->
  <!-- <router-link :to="{ name: 'home' }"> -->

  <!-- </router-link> -->
  <div
    class="w-full flex border border-gray-200 p-10 rounded-lg overflow-y-auto"
  >
    <div class="flex gap-3 flex-col">
      <div class="flex gap-3 items-center -mt-2">
        <MagnifyingGlassIcon class="h-6 w-6" />
        <input
          type="email"
          name="email"
          id="email"
          class="block w-full shadow-none focus:border-0 focus:outline-none text-base h-8 border-none focus:ring-0 rounded-xl"
          placeholder="Search people"
        />
      </div>
      <div
        v-for="user of users"
        @click="$emit('user-selected', user)"
        class="flex items-center gap-4"
      >
        <User :user="user" />
      </div>
    </div>
  </div>
</template>

<script>
import { MagnifyingGlassIcon } from "@heroicons/vue/24/outline";
import User from "./User.vue";
export default {
  components: {
    User,
    MagnifyingGlassIcon,
  },
  data() {
    return {
      users: [
        { name: "Alice Johnson", color: "#7FFFD4" }, // Aqua
        { name: "Bob Smith", color: "#E6E6FA" }, // Lavender
        { name: "Charlie Davis", color: "#98FB98" }, // Mint Green
        { name: "David Wilson", color: "#87CEEB" }, // Sky Blue
        { name: "Emma Brown", color: "#FFD700" }, // Gold
        { name: "Frank Miller", color: "#FFDAB9" }, // PeachPuff
        { name: "Grace Lee", color: "#FFB6C1" }, // LightPink
        { name: "Henry Taylor", color: "#008080" }, // Teal
        { name: "Isabella Harris", color: "#DDA0DD" }, // Plum
        { name: "Jack Anderson", color: "#FF6B6B" }, // LightCoral
        { name: "Katherine Martinez", color: "#40E0D0" }, // Turquoise
        { name: "Liam Rodriguez", color: "#98FB98" }, // PaleGreen
        { name: "Mia Turner", color: "#FFA07A" }, // LightSalmon
        { name: "Noah White", color: "#CCCCFF" }, // Periwinkle
        { name: "Olivia Scott", color: "#DAA520" }, // Goldenrod
        { name: "Parker King", color: "#FFFACD" }, // LemonChiffon
        { name: "Quinn Adams", color: "#ADD8E6" }, // LightBlue
        { name: "Sophia Evans", color: "#DC143C" }, // Crimson
        { name: "Thomas Hall", color: "#E0B0FF" }, // Mauve
        { name: "Victoria Nelson", color: "#708090" }, // SlateGray
      ],
    };
  },
};
</script>

<style scoped></style>

<template>  <!-- <div class="w-full max-w-4xl border border-gray-200 rounded-xl p-5"> -->
  <!-- <router-link :to="{ name: 'home' }"> -->

  <!-- </router-link> -->
  <div
    class="w-full flex border border-gray-200 p-10 rounded-lg overflow-y-auto"
  >
    <div class="flex gap-3 flex-col">
      <div v-for="user of users" class="flex items-center gap-4">
        <div
          :style="{ background: user.color }"
          class="h-12 w-12 items-center justify-center flex font-medium rounded-full"
        >
          {{ getNameLetters(user.name) }}
        </div>

        <div class="flex justify-center flex-col">
          <div class="text-lg">{{ user.name }}</div>
          <!-- <div class="text-base font-medium">[Major]</div> -->
        </div>
      </div>
    </div>
  </div>
  <!-- <div></div> -->
  <!-- </div> -->
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
  methods: {
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

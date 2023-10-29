<template>
    <div
      :style="{ background: user.color }"
      class="h-12 w-12 items-center justify-center flex font-medium rounded-full"
    >
      {{ getNameLetters(user.name) }}
    </div>

    <div class="flex justify-center flex-col">
      <div class="text-lg">{{ user.name }}</div>
      <!-- <div class="text-base font-medium">[Major]</div>  -->
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
props: {
user: Object
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
};
</script>
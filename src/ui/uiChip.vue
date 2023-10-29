<template>
  <div
    class="inline-flex items-center px-3 py-1 rounded-full bg-purple-100 border-2 border-purple-300 text-black"
  >
    <span>{{ label }}</span>
    <button @click="remove" class="ml-2 focus:outline-none">
      <XMarkIcon class="h-6 w-6" />
    </button>
  </div>
</template>

<script>
import { XMarkIcon } from "@heroicons/vue/24/outline";

export default {
  components: {
    XMarkIcon,
  },
  props: {
    label: String,
  },
  methods: {
    remove() {
      // You can emit an event here to notify the parent component to remove this chip
      this.$emit("remove");
    },
  },
};
</script>

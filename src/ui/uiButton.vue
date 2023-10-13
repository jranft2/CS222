<template>
  <div
    type="button"
    class="inline-flex justify-center px-3 py-2 text-sm items-center gap-2 font-medium border border-transparent duration-75 rounded-md focus:outline-none focus-visible:ring-2 focus-visible:ring-offset-2"
    :class="buttonStyle?.classes"
  >
    <component v-if="icon" :is="icon" class="h-5 w-5" />
    <slot></slot>
  </div>
</template>

<script lang="ts">
type ButtonStyle = {
  name: "gray" | "blue" | "purple" | "red";
  classes: string;
};

import type { PropType } from "vue";

export default {
  props: {
    color: {
      type: String as PropType<ButtonStyle["name"]>,
      default: "blue",
      required: false,
    },
    icon: {
      required: false,
    },
  },

  mounted() {
    this.buttonStyle =
      this.buttonColors.find(
        (buttonStyle) => buttonStyle.name === this.color
      ) ?? this.buttonColors[0];
  },

  data() {
    return {
      buttonColors: [
        {
          name: "gray",
          classes:
            "bg-gray-100 hover:bg-gray-200 focus-visible:ring-gray-500 text-gray-900",
        },
        {
          name: "blue",
          classes:
            "bg-blue-100 hover:bg-blue-200 focus-visible:ring-blue-500 text-blue-900",
        },
        {
          name: "purple",
          classes:
            "bg-purple-100 hover:bg-purple-200 focus-visible:ring-purple-500 text-purple-900",
        },
        {
          name: "red",
          classes:
            "bg-red-100 hover:bg-red-200 focus-visible:ring-red-500 text-red-900",
        },
      ] as ButtonStyle[],
      buttonStyle: undefined as ButtonStyle | undefined,
    };
  },
};
</script>
<!-- <uiButton color="blue">Finish</uiButton> -->

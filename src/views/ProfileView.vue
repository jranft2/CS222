<script setup lang="ts"></script>
<template>
  <div class="border border-gray-200 p-10 rounded-lg overflow-y-auto">
    <img
      v-if="profileUrl"
      :src="profileUrl"
      class="h-48 w-48 bg-blue-100 rounded-full border-2 border-gray-200"
    />
    <div
      v-else
      class="h-48 w-48 bg-blue-100 rounded-full border-2 border-gray-200"
    ></div>
    <div class="mt-4">
      <input
        type="file"
        @change="uploadFile($event.target.files)"
        accept="image/*"
        class="hidden"
        id="file-upload"
      />

      <label for="file-upload">
        <uiButton color="gray"> Upload file </uiButton>
      </label>
    </div>

    <div class="flex gap-3 mt-10 flex-col">
      <div class="mb-6 w-64">
        <label
          for="default-input"
          class="block mb-2 text-sm font-medium text-gray-900"
          >Display Name</label
        >
        <input
          type="text"
          id="default-input"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
        />
      </div>
      <div>
        <label
          for="default-input"
          class="block mb-2 text-sm font-medium text-gray-900"
          >Classes</label
        >
        <div class="mb-6 w-64">
          <input
            v-model="classInputValue"
            v-on:keyup.enter="addClass()"
            type="text"
            placeholder="CS 222"
            id="default-input"
            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
          />
        </div>

        <div class="flex gap-2 flex-wrap">
          <uiChip
            v-for="(item, index) in chipItems"
            :key="index"
            :label="item"
          ></uiChip>
        </div>
      </div>
    </div>
    <div class="mt-8">
      <uiButton color="blue"> Save </uiButton>
    </div>
  </div>
</template>

<script lang="ts">
import uiButton from "../ui/uiButton.vue";
import uiChip from "../ui/uiChip.vue";
import { uploadFile } from "@uploadcare/upload-client";

export default {
  components: {
    uiButton,
    uiChip,
  },
  data() {
    return {
      profileUrl: "",
      chipItems: ["Tag 1", "Tag 2", "Tag 3"],
      classInputValue: "",
    };
  },
  methods: {
    addClass() {
      this.chipItems.push(this.classInputValue);
      this.classInputValue = "";
    },

    async uploadFile(fileData: any) {
      console.log("uploading");
      console.log(fileData);
      const result = await uploadFile(fileData[0], {
        publicKey: "a7cb2e537c7133cb5ac6",
        store: "auto",
      });
      if (result) {
        this.profileUrl = result.cdnUrl ?? "";
      }
    },
  },
};
</script>

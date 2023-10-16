<script setup lang="ts"></script>
<template>
  <div class="w-full border border-gray-200 p-10 rounded-lg overflow-y-auto">
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
    </div>
    <uiButton color="blue"> Save </uiButton>
  </div>
</template>

<script lang="ts">
import uiButton from "../ui/uiButton.vue";
import { uploadFile } from "@uploadcare/upload-client";

export default {
  components: {
    uiButton,
  },
  data() {
    return {
      profileUrl: "",
    };
  },
  methods: {
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

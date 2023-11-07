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
          >Github Username
        </label>
        <input
          v-model="githubValue"
          type="text"
          id="default-input"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
        />
      </div>
      <div class="mb-6 w-64">
        <label
          for="default-input"
          class="block mb-2 text-sm font-medium text-gray-900"
          >Leetcode Username</label
        >
        <input
          v-model="leetcodeValue"
          type="text"
          id="default-input"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
        />
      </div>
      <div class="mb-6 w-64">
        <label
          for="default-input"
          class="block mb-2 text-sm font-medium text-gray-900"
          >Display Name</label
        >
        <input
          v-model="nameValue"
          type="text"
          id="default-input"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
        />
      </div>
      <!-- <div>
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
        </div> -->
      <!-- </div> -->
    </div>
    <div class="mt-8">
      <uiButton color="blue" @click="saveUser()"> Save </uiButton>
    </div>
  </div>
</template>

<script>
import uiButton from "../ui/uiButton.vue";
import uiChip from "../ui/uiChip.vue";
import { uploadFile } from "@uploadcare/upload-client";
import { useUserStore } from "../stores/user";

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
      nameValue: "asdf",
      leetcodeValue: "",
      githubValue: "",
    };
  },

  async mounted() {
    console.log("mounting");
    const store = useUserStore();
    const user = await store.getCurrentUser();

    var myHeaders = new Headers();
    myHeaders.append("netidemail", user.email);

    var requestOptions = {
      method: "GET",
      headers: myHeaders,
      redirect: "follow",
    };

    fetch("http://127.0.0.1:8080/get_preferences", requestOptions)
      .then((response) => response.text())
      .then((result) => {
        const data = JSON.parse(result);
        this.profileUrl = data.pfp_url;
        this.nameValue = data.name;
        this.leetcodeValue = data.leetcode;
        this.githubValue = data.github;
      })
      .catch((error) => console.log("error", error));

    //       {
    //   "bio": "bio_val",
    //   "github": "josephshepin",
    //   "leetcode": "jshepin",
    //   "name": "Joey",
    //   "netid_email": "jshepin2@illinois.edu",
    //   "pfp_url": "https://ucarecdn.com/4de6a8b6-700b-4098-b4a5-218f66fb7dbc/"
    // }
  },

  methods: {
    addClass() {
      this.chipItems.push(this.classInputValue);
      this.classInputValue = "";
    },

    async saveUser() {
      const store = useUserStore();
      const user = await store.getCurrentUser();

      console.log(user.email);
      var myHeaders = new Headers();
      myHeaders.append("netidemail", user.email);
      myHeaders.append("name", this.nameValue);
      myHeaders.append("github", this.githubValue);
      myHeaders.append("leetcode", this.leetcodeValue);
      myHeaders.append("bio", "bio_val");
      myHeaders.append("pfpurl", this.profileUrl);

      var requestOptions = {
        method: "POST",
        headers: myHeaders,
        redirect: "follow",
      };

      fetch("http://127.0.0.1:8080/save-user-details", requestOptions)
        .then((response) => response.text())
        .then((result) => console.log(result))
        .catch((error) => console.log("error", error));
    },
    async uploadFile(fileData) {
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

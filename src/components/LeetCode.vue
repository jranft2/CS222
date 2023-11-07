<template>

    <div class="flex items-center border-b mb-1.5 border-gray-300">
        <img src="../assets/leetcode-logo.png" alt="LeetCode Icon" class="w-6 h-6 text-gray-600" />
        <span class="ml-2">LeetCode</span>
    </div>
    <h1>Problems Completed</h1>
    <h2 v-if="userInfo" class="pl-2">Easy:{{ userInfo.easySolved }}</h2>
    <h2 v-if="userInfo" class="pl-2">Medium:{{ userInfo.mediumSolved }}</h2>
    <h2 v-if="userInfo" class="pl-2">Hard:{{ userInfo.hardSolved }}</h2>

</template>

<script>
export default {
    data() {
        return {
            userInfo: null,
            username: "jranft2"
        }
    },
    props: {
        user:Object
    },
    async created() {
        fetch(`https://leetcodestats.cyclic.app/${this.username}`)
            .then(response => response.json())
            .then(data => {
                this.userInfo = data;
            })
            .catch(error => {
                console.error("Error fetching data:", error);
                this.userInfo = "Error fetching data.";
            });
    },
    methods: {
    }
}
</script>

<style scoped></style>
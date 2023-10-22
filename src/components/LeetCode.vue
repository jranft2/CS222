<template>
    <h2>LeetCode </h2>
    <h2 v-if="userInfo">Easy to Solve completed:{{ userInfo.easySolved }}</h2>
    <h2 v-if="userInfo">Medium to Solve completed:{{ userInfo.mediumSolved }}</h2>
    <h2 v-if="userInfo">Hard to Solve completed:{{ userInfo.hardSolved }}</h2>

</template>

<script>
export default {
    data() {
        return {
            userInfo: null,
        }
    },
    props: {
        user:Object
    },
    async created() {
        fetch(`http://172.22.154.189:8080//leetcode/jranft2`)
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
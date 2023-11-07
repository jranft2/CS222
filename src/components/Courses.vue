<template>

    <div class="flex items-center border-b mb-1.5 border-gray-300">
        <font-awesome-icon :icon="['fas', 'i']" style="color: orange;" />
        <span class="ml-2">Courses</span>
    </div>
    <div v-for="course of courses_fake">
        {{ course.number }}, {{ course.name }}
    </div>

</template>

<script>
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faI} from '@fortawesome/free-solid-svg-icons'
library.add(faI)
export default {
    data() {
        return {
            userInfo: null,
            courses_fake: [
                { number: "CS 124", name: "Introduction to Computer Science" },
                { number: "CS 173", name: " Discrete Structures"},
                { number: "CS 222", name: "Software Design Lab" },
                { number: "CS 225", name: "Data Structures"},
        ],
        }
    },
    components: {
        'font-awesome-icon': FontAwesomeIcon
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
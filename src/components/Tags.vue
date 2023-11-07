<template>
    <div class="container ">
        <div class="tag">
            <LeetCode :user="user"/>
        </div>
        <div class="tag col-span-2">
            <Github :user="user" />
        </div>
        <div class="tag col-span-2">
            <Courses :user="user"/>
        </div>
    </div> 
</template>


<script>
import LeetCode from "./LeetCode.vue";
import Github from "./Github.vue";
import Courses from "./Courses.vue";
export default {
    components: {
        LeetCode,
        Github,
        Courses,
    },
  props: {
    user:Object,
  },
}
</script>
<style>
.container {
    display: grid; 
    grid-template-columns: 1fr 1fr 1fr;
    gap: 0.5rem;  
    align-items: center; 
    margin-top: 2.5rem; 
}
.tag {
    margin: 5px auto;
    overflow: auto;
    border: 1px solid #e2e8f0; 
    padding: 10px; 
    border-radius: 8px;

}
</style>

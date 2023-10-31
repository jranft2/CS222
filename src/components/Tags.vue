<template>
    <div class="container ">
        <div class="tag">
            <LeetCode :user="user"/>
        </div>
        <div class="tag">
            <i class="fa-brands fa-github"></i>Github
        </div>
        <div class="tag">
            <i class="fa-sharp fa-solid fa-screen-users"></i>Courses 
        </div>
    </div> 
</template>


<script>
import LeetCode from "./LeetCode.vue";
export default {
    components: {
        LeetCode
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

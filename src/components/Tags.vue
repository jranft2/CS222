<template>
    <div class="flex gap-2 items-center mt-2.5">
        <div class="text-md font-md mt-2 bg-purple-200 rounded-full px-2.5 py-1 w-min">
            <LeetCode :user="user"/>
        </div>
        <div class="text-md font-md mt-2 bg-purple-200 rounded-full px-2.5 py-1 w-min">
        [Github]
        </div>
        <div class="text-md font-md mt-2 bg-purple-200 rounded-full px-2.5 py-1 w-min">
        [Courses]
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
<style scoped></style>

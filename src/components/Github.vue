<template>

    <div class="flex items-center border-b mb-1.5 border-gray-300">
        <font-awesome-icon :icon="['fab', 'github']" />
        <span class="ml-2">Github</span>
    </div>
    <div>
        <a :href="account_url" target="_blank" class="flex items-center text-blue-500">
            <img :src="avatar_url" alt="GithubIMG" class="rounded-full w-16 h-16 p-1" >{{ username }}
        </a>
    </div>

    <div class="flex">
      <div class="mr-4">
        Followers: {{ followers }}
      </div>
      <div class="mr-4">
        Following: {{ following }}
      </div>
      <div>
        Public Repos: {{ publicRepos }}
      </div>
    </div>

</template>

<script>
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faGithub } from '@fortawesome/free-brands-svg-icons';
import { library } from '@fortawesome/fontawesome-svg-core';
library.add(faGithub);
export default {
    data() {
        return {
            userInfo: null,
            avatar_url: null,
            account_url: null,
            followers: null,
            following: null,
            publicRepos: null,
            username: 'jranft2'
        }
    },
    components: {
        'font-awesome-icon': FontAwesomeIcon
    },
    props: {
        user:Object
    },
    async created() {
        fetch(`https://api.github.com/users/${this.username}`)
            .then(response => response.json())
            .then(data => {
                this.userInfo = data;
                this.avatar_url = data.avatar_url;
                this.account_url = data.html_url;
                this.followers = data.followers;
                this.following = data.following;
                this.publicRepos = data.public_repos;
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
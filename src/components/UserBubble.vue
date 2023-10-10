<template>
  <div>
    <!-- user: {{ user }} -->
    <div v-if="!loadingUser">
      <div
        v-if="!user"
        @click="signInWithIllinois()"
        class="flex w-full px-3 py-2 -mr-2 duration-150 rounded-lg cursor-pointer min-w-max hover:bg-gray-50"
      >
        Sign In
      </div>

      <Popover v-if="user">
        <PopoverButton class="focus:outline-none">
          <div class="p-2 duration-100 rounded-full hover:bg-gray-100">
            <UserCircleIcon class="w-7 h-7" />
          </div>
        </PopoverButton>
        <transition
          enter-active-class="transition duration-200 ease-out"
          enter-from-class="translate-y-1 opacity-0"
          enter-to-class="translate-y-0 opacity-100"
          leave-active-class="transition duration-150 ease-in"
          leave-from-class="translate-y-0 opacity-100"
          leave-to-class="translate-y-1 opacity-0"
        >
          <PopoverPanel
            v-slot="{ close }"
            class="absolute right-0 z-20 w-64 -mr-1"
          >
            <div
              class="overflow-hidden bg-white rounded-lg shadow-lg ring-1 ring-gray-200"
            >
              <div class="p-3 text-black bg-white">
                <div class="text-base">Account</div>
                <div v-if="user?.email" class="mt-0.5 text-sm text-gray-600">
                  {{ user?.email }}
                </div>
              </div>
              <hr />
              <div class="flex flex-col gap-1 p-1">
                <div
                  @click="
                    close();
                    openProfilePage();
                  "
                  class="flex w-full p-2 duration-150 rounded-md cursor-pointer hover:bg-gray-100"
                >
                  Settings
                </div>
                <div
                  @click="
                    close();
                    signOutUser();
                  "
                  class="flex w-full p-2 duration-150 rounded-md cursor-pointer hover:text-red-500 hover:bg-gray-100"
                >
                  Sign out
                </div>
              </div>
            </div>
          </PopoverPanel>
        </transition>
      </Popover>
    </div>
  </div>
</template>

<script lang="ts">
import { Popover, PopoverButton, PopoverPanel } from "@headlessui/vue";
import { UserCircleIcon } from "@heroicons/vue/24/outline";
import { useUserStore } from "../stores/user";
import { mapActions, mapState } from "pinia";

export default {
  components: {
    Popover,
    PopoverButton,
    PopoverPanel,
    UserCircleIcon,
  },

  computed: {
    ...mapState(useUserStore, ["user", "loadingUser"]),
  },

  methods: {
    ...mapActions(useUserStore, ["signInWithIllinois", "signOutUser"]),
    openProfilePage() {
      this.$router.push({ name: "Profile" });
    },
  },
};
</script>

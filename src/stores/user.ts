import { defineStore } from "pinia";
import {
  getAuth,
  signOut,
  OAuthProvider,
  signInWithPopup,
  onAuthStateChanged,
  type User,
} from "firebase/auth";

export const useUserStore = defineStore("user", {
  state: () => ({
    user: null as User | null,
    token: undefined as string | undefined,
    loadingUser: true as boolean,
    userDetails: null as any | null,
  }),

  actions: {
    async signInWithIllinois() {
      const oAuthProvider = new OAuthProvider("microsoft.com");
      oAuthProvider.setCustomParameters({
        prompt: "consent",
        tenant: "44467e6f-462c-4ea2-823f-7800de5434e3",
      });
      signInWithPopup(getAuth(), oAuthProvider).then(async (result) => {
        console.log(result.user);
        getAuth();
        this.user = await this.getCurrentUser();
        console.log("this user is ", this.user);
      });
    },

    signOutUser() {
      signOut(getAuth()).then(async () => {
        getAuth();
        this.user = null;
        this.setUserDetails(null);
        this.loadingUser = false;
      });
    },

    async refreshUser(): Promise<void> {
      this.user = await this.getCurrentUser();
      this.loadingUser = false;
    },

    setUserDetails(value: any | null) {
      this.userDetails = value;
    },

    setToken(newToken: string) {
      this.token = newToken;
    },

    getCurrentUser(): Promise<User | null> {
      return new Promise((resolve, reject) => {
        const auth = getAuth();
        const unsubscribe = onAuthStateChanged(
          auth,
          (user) => {
            unsubscribe();
            resolve(user);
          },
          reject
        );
      });
    },
  },
});

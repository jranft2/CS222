import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import ProfileView from "../views/ProfileView.vue";

import { useUserStore } from "../stores/user";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "Users",
      component: HomeView,
    },
    {
      path: "/",
      name: "Profile",
      component: ProfileView,
    },
  ],
});

router.beforeEach(async (_to, _from, next) => {
  // if (to.matched.some((record) => record.meta.requiresAuth)) {
  const store = useUserStore();
  store.refreshUser();
  const user = await store.getCurrentUser();

  if (user) {
    const newToken = await user?.getIdToken();

    store.setToken(newToken);
  }
  // next({
  //   name: "home",
  // });
  next();
});

export default router;

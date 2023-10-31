import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import { initializeApp } from "firebase/app";
import { createPinia } from "pinia";
import 'font-awesome/css/font-awesome.css';
import router from "./router";

/* code from our Firebase console */
const firebaseConfig = {
  apiKey: "AIzaSyDqJzb0IyYBYASxvtaws4e7tSHK59iRDSI",
  authDomain: "uiuc-ad.firebaseapp.com",
  projectId: "uiuc-ad",
  storageBucket: "uiuc-ad.appspot.com",
  messagingSenderId: "280663047030",
  appId: "1:280663047030:web:421dd3e1b363b406819857",
};

// Initialize Firebase
initializeApp(firebaseConfig);
const pinia = createPinia();

const app = createApp(App);

app.use(router);

app.use(pinia);
app.mount("#app");

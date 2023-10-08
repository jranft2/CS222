import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import { initializeApp } from "firebase/app";

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

createApp(App).mount("#app");

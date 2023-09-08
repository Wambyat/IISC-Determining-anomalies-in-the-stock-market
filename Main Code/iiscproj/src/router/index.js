import { createRouter, createWebHashHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import StockView from "../views/StockView.vue";
import ModelView from "../views/ModelView.vue";

const routes = [
    {
        path: "/",
        name: "home",
        component: HomeView,
    },
    {
        path: "/model",
        name: "model",
        component: ModelView,
    },
    {
        path: "/stock/:query",
        name: "search",
        component: StockView,
        props: true,
    },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

export default router;

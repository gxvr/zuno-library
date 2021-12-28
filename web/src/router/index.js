import { createWebHistory, createRouter } from "vue-router"

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
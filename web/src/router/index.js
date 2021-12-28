import { createWebHistory, createRouter } from "vue-router"
import Home from "@/views/Home.vue"
import PageNotFound from "@/views/PageNotFound.vue"
import Book from "@/views/Book.vue"

// Routes
const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
    },
    {
        path: '/book',
        name: "Book",
        component: Book,
    },
    {
        path: '/:catchAll(.*)*',
        name: "PageNotFound",
        component: PageNotFound,
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
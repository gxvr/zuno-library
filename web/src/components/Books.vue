<template>
  <div class="mt-10 mb-10 bg-white main-wrapper px-28">
    <div class="mx-auto max-w-screen-2xl">
      <div class="flex items-end justify-between gap-6 mb-6">
        <h3
          class="mb-2 text-xl font-bold primary-color md:text-2xl lg:text-3xl"
        >
          Popular Now
        </h3>
        <a
          href="#"
          class="inline-block px-4 py-2 text-sm font-semibold text-center text-gray-500 bg-white outline-none  md:text-base md:px-8 md:py-3"
          >Show more</a
        >
      </div>

      <div
        class="grid  sm:grid-cols-2 lg:grid-cols-5 xl:grid-cols-5 gap-x-4 md:gap-x-6 gap-y-6"
      >
        <!-- books start -->
        <div v-for="book in books" v-bind:key="book.bibnum" class="mt-2 mb-3">
          <router-link
            :to="'/books/' + book.media.bibnum"
            class="block mb-2 overflow-hidden bg-gray-100 rounded-lg shadow-lg  group h-84 lg:mb-3"
          >
            <img
              src="../assets/img/book-cover.jpg"
              alt="Book Cover"
              class="object-cover object-center w-full h-full"
            />
          </router-link>

          <div class="flex flex-col">
            <div
              href="#"
              class="text-lg font-bold text-gray-800 truncate  hover:text-gray-500 lg:text-lg"
            >
              <router-link :to="'/books/' + book.media.bibnum">
                {{ book.media.title }}
              </router-link>
            </div>
            <span class="text-gray-500 truncate">{{ book.media.author }}</span>

            <!-- stars -->
            <div class="flex gap-0.5 -ml-1">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="w-6 h-6 text-yellow-400"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
                />
              </svg>

              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="w-6 h-6 text-yellow-400"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
                />
              </svg>

              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="w-6 h-6 text-yellow-400"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
                />
              </svg>

              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="w-6 h-6 text-yellow-400"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
                />
              </svg>

              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="w-6 h-6 text-gray-300"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
                />
              </svg>
            </div>
            <!-- stars -->
          </div>
        </div>
        <!-- book end -->
      </div>
    </div>
  </div>
</template>

<script>
import LibraryDataService from "../services/LibraryDataService";

export default {
  name: "Books",
  data() {
    return {
      books: [],
    };
  },

  methods: {
    retrieveBooks() {
      LibraryDataService.getAll()
        .then((response) => {
          this.books = response.data;
          console.log(response.data);
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
  mounted() {
    this.retrieveBooks();
  },
};
</script>

<style scoped>
.truncate {
  width: 250px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>


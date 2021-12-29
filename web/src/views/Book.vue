//Single Book
<template>
  <div id="app">
    <Navbar />
    <div class="bg-white py-6 sm:py-8 lg:py-12">
      <div class="max-w-screen-xl mx-auto">
        <div class="grid md:grid-cols-2 gap-8">
          <!-- images - start -->
          <div class="grid lg:grid-cols-5 gap-4">
            <div
              class="
                lg:col-span-4
                bg-gray-100
                rounded-lg
                overflow-hidden
                relative
              "
            >
              <img
                src="../assets/img/book-cover.jpg"
                loading="lazy"
                alt=""
                class="w-full h-full object-cover object-center"
              />

              <span
                class="
                  bg-red-500
                  text-white text-sm
                  tracking-wider
                  uppercase
                  rounded-br-lg
                  absolute
                  left-0
                  top-0
                  px-3
                  py-1.5
                "
                >BEST SELLER</span
              >

              <a
                href="#"
                class="
                  inline-block
                  bg-white
                  hover:bg-gray-100
                  focus-visible:ring
                  ring-indigo-300
                  text-gray-500
                  active:text-gray-700
                  border
                  text-sm
                  md:text-base
                  font-semibold
                  text-center
                  rounded-lg
                  outline-none
                  transition
                  duration-100
                  absolute
                  right-4
                  top-4
                  px-3.5
                  py-3
                "
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="w-6 h-6"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
                  />
                </svg>
              </a>
            </div>
          </div>
          <!-- images - end -->

          <!-- content - start -->
          <div class="md:py-8">
            <!-- name - start -->
            <div class="mb-2 md:mb-3">
              <span class="inline-block text-gray-500 mb-0.5">
                Author: <b class="font-bold">{{ book.author }}</b>
              </span>

              <h2 class="text-gray-800 text-2xl lg:text-3xl font-bold mb-5">
                <h1>{{ book.title }}</h1>
              </h2>

              <!-- stars -->
              <div class="flex gap-0.5 -ml-1 mb-5">
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

              <p class="mb-5">
                Publisher: <b class="font-bold">{{ book.publisher }}</b>
              </p>

              <p class="mb-5">
                Publication: <b class="font-bold">{{ book.publicationyear }}</b>
              </p>

              <p class="mb-5">
                ISBN: <b class="font-bold">{{ book.isbn }}</b>
              </p>

              <p class="mb-5">Subjects: {{ book.subjects }}</p>
            </div>
            <!-- name - end -->

            <!-- rating - start -->
            <div class="flex items-center gap-3 mb-6 md:mb-10">
              <span class="text-gray-500 text-sm transition duration-100"
                >{{ book.itemtype }} Item Type</span
              >
              |
              <span class="text-gray-500 text-sm transition duration-100"
                >{{ book.itemcount }} Item Count</span
              >
            </div>
            <!-- rating - end -->

            <!-- buttons - start -->
            <div class="flex gap-2.5">
              <a
                href="#"
                class="
                  inline-block
                  flex-1
                  sm:flex-none
                  bg-indigo-500
                  hover:bg-indigo-600
                  active:bg-indigo-700
                  focus-visible:ring
                  ring-indigo-300
                  text-white text-sm
                  md:text-base
                  font-semibold
                  text-center
                  rounded-lg
                  outline-none
                  transition
                  duration-100
                  px-8
                  py-3
                "
                >Add to cart</a
              >

              <a
                href="#"
                class="
                  inline-block
                  bg-gray-200
                  hover:bg-gray-300
                  focus-visible:ring
                  ring-indigo-300
                  text-gray-500
                  active:text-gray-700
                  text-sm
                  md:text-base
                  font-semibold
                  text-center
                  rounded-lg
                  outline-none
                  transition
                  duration-100
                  px-8
                  py-3
                "
                >Buy now</a
              >
            </div>
            <!-- buttons - end -->
          </div>
          <!-- content - end -->
        </div>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script>
import Navbar from "../components/Navbar.vue";
import Footer from "../components/Footer.vue";
import LibraryDataService from "../services/LibraryDataService";

export default {
  name: "Book",
  components: {
    Navbar,
    Footer,
  },
  data() {
    return {
      book: "",
    };
  },

  methods: {
    getBook(bibnum) {
      LibraryDataService.get(bibnum)
        .then((response) => {
          this.book = response.data[0];
          console.log(response.data);
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },

  mounted() {
    this.getBook(this.$route.params.bibnum);
  },
};
</script>

<style scoped>
h1,
h2,
h3 {
  font-family: "Prompt", sans-serif;
}

nav a {
  font-size: 16px !important;
}

.wrapper-bg {
  background-color: #313047;
}

.primary-color {
  color: #313047;
}

.btn-primary:hover {
  background-color: #b19987;
}
</style>
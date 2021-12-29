<template>
  <div class="bg-white main-wrapper px-28">
    <div class="mx-auto max-w-screen-2xl">
      <div
        class="relative flex flex-col overflow-hidden  sm:flex-row wrapper-bg rounded-2xl"
      >
        <img
          src="../assets/img/scribble.svg"
          class="absolute object-cover w-52 h-52 bottom-48 left-1/2"
        />
        <!-- Hero Contents -->
        <div class="flex flex-col w-full p-14">
          <h2 class="mb-4 text-xl font-bold text-white md:text-3xl lg:text-5xl">
            Build your library
          </h2>

          <p class="w-full mb-8 text-lg text-gray-200 sm:w-2/4">
            Buy two selected books and get one for free
          </p>

          <div class="mt-auto">
            <a
              href="#"
              class="inline-block px-8 py-3 text-sm font-semibold text-center text-white transition duration-100 bg-indigo-500 rounded-lg outline-none  active:bg-gray-200 focus-visible:ring md:text-base"
              >View all</a
            >
          </div>
        </div>
        <!-- Hero Contents -->

        <!-- Image-->
        <div class="relative order-first w-full overflow-hidden sm:order-none">
          <img
            src="../assets/img/illustration.svg"
            alt="Zuno Libary illustration"
            class="object-center absolute -top-3.5 right-0"
            width="700"
          />
        </div>
        <!-- Image -->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Hero",
};
</script>

<style scoped>
</style>
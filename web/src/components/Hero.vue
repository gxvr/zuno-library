<template>
  <div class="main-wrapper bg-white px-28">
    <div class="max-w-screen-2xl mx-auto">
      <div
        class="flex flex-col sm:flex-row wrapper-bg rounded-2xl overflow-hidden"
      >
        <!-- Hero Contents -->
        <div class="w-full flex flex-col p-14">
          <h2 class="text-white text-xl md:text-3xl lg:text-5xl font-bold mb-4">
            Build your library
          </h2>

          <p class="text-gray-200 text-lg mb-8 sm:w-2/4 w-full">
            Buy two selected books and get one for free
          </p>

          <div class="mt-auto">
            <a
              href="#"
              class="
                inline-block
                text-white
                active:bg-gray-200
                focus-visible:ring
                text-sm
                md:text-base
                font-semibold
                text-center
                rounded-lg
                outline-none
                transition
                duration-100
                bg-indigo-500
                px-8
                py-3
              "
              >View all</a
            >
          </div>
        </div>
        <!-- Hero Contents -->

        <!-- Image-->
        <div class="w-full order-first sm:order-none overflow-hidden relative">
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
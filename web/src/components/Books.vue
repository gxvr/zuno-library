<template>
  <div class="main-wrapper bg-white px-28 mt-10 mb-10">
    <div class="max-w-screen-2xl mx-auto">
      <div class="flex justify-between items-end gap-6 mb-6">
        <h3
          class="primary-color text-xl md:text-2xl lg:text-3xl font-bold mb-2"
        >
          Popular Now
        </h3>
        <a
          href="#"
          class="
            inline-block
            bg-white
            text-gray-500 text-sm
            md:text-base
            font-semibold
            text-center
            outline-none
            px-4
            md:px-8
            py-2
            md:py-3
          "
          >Show more</a
        >
      </div>

      <div
        class="
          grid
          sm:grid-cols-2
          lg:grid-cols-6
          xl:grid-cols-6
          gap-x-4
          md:gap-x-6
          gap-y-6
        "
      >
        <!-- books start -->
        <div>
          <a
            href="#"
            class="
              group
              h-72
              block
              bg-gray-100
              rounded-lg
              overflow-hidden
              shadow-lg
              mb-2
              lg:mb-3
            "
          >
            <img
              src="../assets/img/cover.jpg"
              alt="Book Cover"
              class="w-full h-full object-cover object-center"
            />
          </a>

          <div class="flex flex-col">
            <a
              href="#"
              class="
                text-gray-800
                hover:text-gray-500
                text-lg
                lg:text-lg
                font-bold
              "
              >Tales of two Cities</a
            >
            <span class="text-gray-500">Simon Spotlight</span>
          </div>
        </div>
        <!-- book - end -->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Books",
};
</script>

<style scoped>
</style>


// 404
<template>
  <section class="bg-white py-44">
    <div class="max-w-5xl px-10 mx-auto xl:px-5">
      <div class="flex flex-col justify-center space-y-8">
        <p
          class="
            w-full
            -mb-3
            font-medium
            text-left text-blue-600
            uppercase
            md:text-center
          "
        >
          OOPS!
        </p>
        <h2
          class="
            w-full
            mx-auto
            text-4xl
            font-extrabold
            leading-none
            text-left text-gray-900
            sm:text-5xl
            md:text-7xl md:text-center
          "
        >
          404 - Not Found
        </h2>
        <p
          class="
            w-full
            max-w-3xl
            mx-auto
            text-xl text-left text-gray-500
            md:text-2xl md:text-center
          "
        >
          Looks like we are a bit lost. Not to worry click on the button below
          to go back to the home page.
        </p>
      </div>
      <p class="mt-5 text-gray-400 text-center">
        <router-link
          :to="{ name: 'Home' }"
          class="
            bg-indigo-700
            px-8
            py-4
            select-none
            rounded
            inline-block
            text-white
          "
          >Go to Homepage</router-link
        >
      </p>
    </div>
  </section>
</template>
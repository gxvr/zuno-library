// Home
<template>
  <div id="app">
    <Navbar />
    <Hero />
    <Books />
    <Footer />
  </div>
</template>

<script>
import Navbar from "../components/Navbar.vue";
import Hero from "../components/Hero.vue";
import Books from "../components/Books.vue";
import Footer from "../components/Footer.vue";

export default {
  name: "App",
  components: {
    Navbar,
    Hero,
    Books,
    Footer,
  },
};
</script>

<style>
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  font-family: "Inter", sans-serif !important;
  font-size: 16px;
  font-weight: 300;
}

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

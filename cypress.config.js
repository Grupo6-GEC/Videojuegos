const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {

    baseUrl: "http://localhost:9081",

    supportFile: false

  },
});
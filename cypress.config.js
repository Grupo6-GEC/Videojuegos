const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {

    baseUrl: "http://172.17.0.1:6106",
    supportFile: false

  },
});

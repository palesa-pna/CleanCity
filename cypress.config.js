const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    baseUrl: 'http://localhost:3000',  // set your base URL here
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});

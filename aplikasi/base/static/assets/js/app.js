
// Place third party dependencies in the lib folder
//
// Configure loading modules from the lib directory,
console.log("app.js");
requirejs.config({
    "baseUrl": "js/vendor",
    "paths": {
      "app": "../captchas"
    },
    "shim": {
        "backbone": ["jquery", "underscore"],
        "bootstrap": ["jquery"],
        "plugins": ["jquery"]
    }
});

// Load the main app module to start the app
requirejs(["captcha/mains"]);
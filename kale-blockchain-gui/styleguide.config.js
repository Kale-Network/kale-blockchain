const path = require("path");
const { version } = require("./package");

module.exports = {
  components: "src/components/**/[A-Z]*.js",
  styleguideComponents: {
    Wrapper: path.join(__dirname, "src/StyleguidistMuiWrapper"),
  },
  ribbon: {
    url: "https://github.com/Kale-Network/kale-blockchain",
  },
  version,
};

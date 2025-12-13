module.exports = {
  content: [
    "./templates/**/*.html",  // Scans all HTML in templates/
    "./events/templates/**/*.html",  // If templates are app-specific
    "./static/**/*.js",  // If using JS files with classes
  ],
  theme: { extend: {} },
  plugins: [],
}
# web-1st-sem-final-assignment


## tailwind.config.js (coppy & paste it)
module.exports = {
  mode : "jit",
  purge : ["../views/*.html"],
  content: [],
  theme: {
    extend: {},
  },
  plugins: [],
}

# Install tailwind
create tailwindcss dir and follow the following steps
- cd tailwindcss
- npm install -d tailwindcss@latest postcss@latest autoprefixer@latest
- npx tailwindcss init

Set these 3 lines in the tailwindcss.css file:
@tailwind base;
@tailwind components;
@tailwind utilities;

npx tailwindcss -i tailwindcss.css -o ../app.css --watch
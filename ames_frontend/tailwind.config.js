/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  darkMode: 'class',
  theme: {
    extend: {
      fontFamily: {
        outfit: ['Outfit', 'sans-serif'],
      },
      colors: {
        brand: {
          50: '#ecf3ff',
          100: '#dde9ff',
          500: '#465fff',
          600: '#3641f5',
          // Aggiungi gli altri colori che avevi nel CSS seguendo questo schema
        },
        gray: {
          25: '#fcfcfd',
          50: '#f9fafb',
          // ... eccetera
        }
      },
      screens: {
        '2xsm': '375px',
        'xsm': '425px',
        '3xl': '2000px',
      },
    },
  },
  plugins: [],
}

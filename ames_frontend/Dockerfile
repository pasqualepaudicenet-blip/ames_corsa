FROM node:lts-alpine

WORKDIR /app

# Installiamo le dipendenze
COPY package*.json ./
RUN npm install

# Copiamo il resto dei file
COPY . .

# Espone la porta di sviluppo di Vite/Vue CLI
EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"] 
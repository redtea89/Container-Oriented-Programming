FROM node:18-alpine
# FROM node:18-slim
WORKDIR /app

COPY package*.json .

RUN npm install
COPY . .
EXPOSE 3001
CMD ["node", "app.js"]

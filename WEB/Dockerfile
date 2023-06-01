FROM node:19 as build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM node:19 AS deploy-node
WORKDIR /app
COPY --from=build /app/package*.json ./
COPY --from=build /app/build ./
RUN npm install --production
CMD ["node", "index.js"]

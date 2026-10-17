# Remediated image: current LTS Node on a minimal Alpine base, running as a non-root user.
FROM node:22-alpine

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci --omit=dev

COPY server.js ./
COPY views ./views

USER node
EXPOSE 3000
CMD ["node", "server.js"]

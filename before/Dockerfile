# INTENTIONALLY OUTDATED base image (Node 14 on Debian buster, both end-of-life).
# Snyk will report many OS-level CVEs in this image. Used for the "before" scan only.
FROM node:14

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY server.js ./
COPY views ./views

EXPOSE 3000
CMD ["node", "server.js"]

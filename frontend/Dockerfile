FROM node:19.9.0-bullseye-slim

ENV LANG ja_JP.UTF-8
ENV NUXT_HOST 0.0.0.0
ENV NUXT_PORT 3000

COPY ./ /app
WORKDIR /app

RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y python3 make g++ \
  && yarn \
  && yarn build \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

CMD [ "yarn", "start" ]

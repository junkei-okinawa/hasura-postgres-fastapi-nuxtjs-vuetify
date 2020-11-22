FROM ubuntu:20.04

EXPOSE ${CONTAINER_PORT}
CMD ["bash"]

ENV DEBIAN_FRONTEND=noninteractive

ARG WORKDIR=/front
ARG CONTAINER_PORT=$FRONT_PORT
ARG API_URL=http://project:$API_PORT

ENV HOME=/${WORKDIR} \
    LANG=C.UTF-8 \
    TZ=Asia/Tokyo \
    HOST=0.0.0.0 \
    API_URL=${API_URL} \
    NPM_CONFIG_PRODUCTION=false

# ENV check
RUN echo ${HOME}
RUN echo ${CONTAINER_PORT}
RUN echo ${API_URL}

WORKDIR ${HOME}

# install vim & curl & setting TIMEZONE
RUN apt update && apt-get update && \
    apt install vim -y && \
    apt-get install curl zsh sudo wget g++ build-essential -y && \
    apt-get install tzdata && dpkg-reconfigure tzdata && dpkg-reconfigure tzdata && \
    apt-get clean

# install git & pip
RUN printf '6\n79\n' | apt install software-properties-common dirmngr gnupg-agent -y && \
    printf '\n' | add-apt-repository ppa:git-core/ppa && \
    apt update && \
    apt install git -y && \
    rm -rf /var/lib/apt/lists/*

# install nodejs
ENV NODE_VERSION 14.0.0
RUN curl --compressed "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" > /tmp/node.tar.xz && \
    tar -xJf /tmp/node.tar.xz -C /usr/local --strip-components=1 && \
    ln -s /usr/local/bin/node /usr/local/bin/nodejs && \
    rm /tmp/node.tar.xz

# install yarn
ENV YARN_VERSION 1.22.5
RUN curl -L --compressed "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" > /tmp/yarn.tar.gz && \
    tar -xzf /tmp/yarn.tar.gz -C /opt && \
    ln -s /opt/yarn-v$YARN_VERSION/bin/yarn /usr/local/bin/yarn && \
    ln -s /opt/yarn-v$YARN_VERSION/bin/yarnpkg /usr/local/bin/yarnpkg && \
    rm /tmp/yarn.tar.gz

### 初回はこの部分をコメントアウトして実行後、 ###
### 以下のコマンドを実行する　参考｜https://blog.cloud-acct.com/posts/u-docker-create-nuxtjs/
### docker-compose exec front bash # コンテナに入る
### yarn create nuxt-app app # nuxtプロジェクトを作成（対話型でいくつか質問が入るので、参考URLを見て回答）
### mv -rf app/* ./ && rm app # app内のmodule郡を1つ上の階層に移動しappフォルダを削除
### exit # コンテナを抜ける
###########################################
COPY . .
RUN yarn install && yarn run build
CMD exec yarn run dev
###########################################
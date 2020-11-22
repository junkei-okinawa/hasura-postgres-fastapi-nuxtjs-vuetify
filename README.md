# hasura-postgres-fastapi-nuxtjs-vuetify
Template docker-compose.

# Overview
docker-compose & Dockerfile template.
- database - postgres & hasura(Debian GNU 10 buster)
- frontend - Nuxtjs & Vuetify (ubuntu20.04)
- backend - python & fastapi (ubuntu20.04)

## Usage
```docker-compose
docker-compose up
```
It may take up to 10 minutes to start up the first time
 - database UI(hasura) → http://localhost:8080
 - frontend UI(Vuetify) → http://localhost:8888
 - api UI(fastapi) → http://localhost:8000

**If you want to build a Nuxtjs project with different contents, delete all files in the front directory except Dockerfile and follow the steps below.**

### 1. Delete Nuxt Project
'''bash
bash Delete_Nuxt_Project.hs
'''

### 2. Comment out the following part of front / Dockerfile
 front/Dockerfile:
 ```Dockerfile
 COPY . .
 RUN yarn install && yarn run build
 CMD exec yarn run dev
 ```
 ↓
 ```Dockerfile
 # COPY . .
 # RUN yarn install && yarn run build
 # CMD exec yarn run dev
 ```
### 3. Create a Nuxt project
 ```docker-compose
 docker-compose up
 docker-compose exec front yarn create nuxt-app app # Answer some questions for creating the Nuxt Project
 docker-compose exec front mv -rf app/* ./ && rm app
 ```
 An error comment may be displayed at the end of the Nuxt Project creation command, but you can ignore it.

### 4. Uncomment the commented out part of the Dockerfile in the front directory and execute the following command
 front/Dockerfile:
 ```Dockerfile
 # COPY . .
 # RUN yarn install && yarn run build
 # CMD exec yarn run dev
 ```
 ↓
 ```Dockerfile
 COPY . .
 RUN yarn install && yarn run build
 CMD exec yarn run dev
 ```

 ```docker-compose
 docker-compose up
 ```
 - hasura → http://localhost:8080
 - front(Vuetify) → http://localhost:8888
 - api ui(fastapi) → http://localhost:8000

## Supplement
If you want to change the port of each tool or the password of postgres, edit ".env"

## Contents used
- Nuxtjs & Vuetify https://blog.cloud-acct.com/posts/u-docker-create-nuxtjs/
- postgres & hasura https://hasura.io/docs/1.0/graphql/core/getting-started/docker-simple.html
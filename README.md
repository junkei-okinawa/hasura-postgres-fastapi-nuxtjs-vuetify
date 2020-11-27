# hasura-postgres-fastapi-nuxtjs-vuetify
Template docker-compose.

# Overview
docker-compose & Dockerfile template.
- database - postgres & hasura(Debian GNU 10 buster)
- frontend - Nuxtjs & Vuetify (ubuntu20.04)
- backend - python & fastapi (ubuntu20.04)

## Usage
### First time build container & Create Nuxtjs project
#### 1. 
```bash
docker-compose up -d # It may take up to 5 minutes to start up the first time
docker-compose exec front yarn create nuxt-app app # Answer some questions for creating the Nuxt Project
find ./front/app -not -name 'Dockerfile' -maxdepth 1 | xargs -I {} mv -f {} ./front ; rm -d ./front/app
```
An error comment may be displayed at the end of the Nuxt Project creation command, but you can ignore it.

#### 2.
front/nuxt.config.js
'''js
export default {
  // Disable server-side rendering (https://go.nuxtjs.dev/ssr-mode)
  ssr: false,
'''
↓
’’’
export default {
  server: {
       port: 8888, // デフォルト: 3000
       host: 'localhost' // デフォルト: localhost
  },
  // Disable server-side rendering (https://go.nuxtjs.dev/ssr-mode)
  ssr: false,
'''

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

#### 3.
```docker-compose
docker-compose up -d
```
 - database UI(hasura) → http://localhost:8080
 - frontend UI(Vuetify) → http://localhost:8888
 - api UI(fastapi) → http://localhost:8000


**If you want to build a Nuxtjs project with different contents, delete all files in the front directory except Dockerfile and follow the steps below.**
### 1. Delete Nuxt Project
'''bash
bash Delete_Nuxt_Project.sh
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

### 3.
Repeat steps 1 to 3 same as the first time

## Supplement
If you want to change the port of each tool or the password of postgres, edit ".env"

## Contents used
- Nuxtjs & Vuetify https://blog.cloud-acct.com/posts/u-docker-create-nuxtjs/
- postgres & hasura https://hasura.io/docs/1.0/graphql/core/getting-started/docker-simple.html

# API

REST API using Django REST Framework

### API Actions

-   [ ] List Boards
-   [ ] Filter Boards
-   [ ] Search By Coords
-   [ ] Login
-   [ ] Create Account
-   [ ] See Boards
-   [ ] Add Boards to Favourites
-   [ ] See Favs
-   [ ] See Profile
-   [ ] Edit Profile

# 1. Setup 20-11-20

-   git clone https://github.com/nomadcoders/airbnb-api --branch blueprint --single-branch new-airbnb-api
-   디렉토리에서 rm -rf .git
-   git init
-   pipenv install
-   pipenv install djangorestframework
-   config/settings 에 third party app 추가
-   THIRD_PARTY_APPS = ["rest_framework",]
-   django-admin startapp boards (게시판 앱 추가)
    -> model, view, url, serializer 등 추가
-   makemigrations / migrate

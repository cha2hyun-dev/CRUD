# API

REST & GraphQL API of the Airbnb Clone using Django REST Framework and Graphene GraphQL

### API Actions

-   [ ] List Rooms
-   [ ] Filter Rooms
-   [ ] Search By Coords
-   [ ] Login
-   [ ] Create Account
-   [ ] See Room
-   [ ] Add Room to Favourites
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
-   makemigrations / migrate

from django.conf.urls import url, include
from django.contrib import admin
import books.views as book_views 
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token


router = DefaultRouter()
router.register(r'book', book_views.BookViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', obtain_jwt_token),
]


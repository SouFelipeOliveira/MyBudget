from django.urls import path

from .views import getUser

urlpatterns = [
    path('hello/', getUser.as_view(),name='hello')
]
from django.urls import path, include

from users.views import UserInfoViews
urlpatterns = [
    path('userinfo/', UserInfoViews.as_view(), name='userinfo'),
]
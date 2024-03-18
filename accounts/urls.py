from django.urls import path
from accounts.social_views.kakao_login import KakaoLoginView, KakaoCallbackView, KakaoLoginToDjango

urlpatterns = [
    path("kakao/login/", KakaoLoginView.as_view(), name="kakao_login"),
    path("kakao/callback/", KakaoCallbackView.as_view(), name="kakao_callback"),
    path(
        "kakao/login/finish/",
        KakaoLoginToDjango.as_view(),
        name="kakao_login_to_django",
    ),
]

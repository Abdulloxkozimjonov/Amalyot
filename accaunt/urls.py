from django.urls import path
from . import views

urlpatterns = [
    path("sing-up-account", views.singup_view),
    path("sing-in-view", views.singin_view),
    path("edit_user", views.UpdateUser.as_view()),
    path("logo-out", views.logoout),
]

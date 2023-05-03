"""URL mapping for user API

/api/user/create
"""

from django.urls import path, re_path
from . import views

app_name = "user"

urlpatterns = [
    # named-urls
    re_path(r'cr[a-z]+te', views.CreateUserView.as_view(), name="create"),
    path("token/", views.CreateTokenView.as_view(), name="token"),
    path("me/", views.ManageUserView.as_view(), name="me")
]


"""URLs for job API"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from job import views

# `DefaultRouter` provided by DRF automatically creates URL routing for us
# TODO - Refer
# https://www.django-rest-framework.org/api-guide/routers/#defaultrouter

router = DefaultRouter()

# this app name will be utilized in reverse function
app_name = "jobtitle"
router.register("jobtitles", views.JobTitleViewSet)

print(f"router.urls :: {router.urls}")

urlpatterns = [
    path("", include(router.urls))
]
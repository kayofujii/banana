from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TestResultDetailApiView, TestResultListApiView, UserViewSet

router = DefaultRouter()
router.register("user", UserViewSet)

urlpatterns = [
    path("result/", TestResultListApiView.as_view()),
    path("result/<int:result_id>/", TestResultDetailApiView.as_view()),
    path("", include(router.urls)),
]

from django.urls import include, path

from .views import TestResultDetailApiView, TestResultListApiView

urlpatterns = [
    path("", TestResultListApiView.as_view()),
    path("<int:result_id>/", TestResultDetailApiView.as_view()),
]

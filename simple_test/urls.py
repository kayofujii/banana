from django.urls import include, path

urlpatterns = [
    path("api/", include("simple_test.api.urls")),
]

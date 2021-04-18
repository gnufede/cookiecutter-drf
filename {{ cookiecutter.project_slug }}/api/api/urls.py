from django.urls import path, re_path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter


# Extend this router with your own routes
# E.g.: router.registry.extend(your_router.registry)
router = DefaultRouter()


# API URL configuration
app_urls = [
    # API
    path("", include(router.urls)),
    # API Authentication
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path("auth/oauth/", include("rest_framework_social_oauth2.urls")),
    path("auth/oauth/", include("oauth2_provider.urls")),
]


# Schema URL configuration
schema_urls = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="api:schema"),
        name="schema-swagger-ui",
    ),
    path(
        "schema/redoc/",
        SpectacularRedocView.as_view(url_name="api:schema"),
        name="schema-redoc",
    ),
]


# Final URL configuration
app_name = "api"
urlpatterns = app_urls + schema_urls

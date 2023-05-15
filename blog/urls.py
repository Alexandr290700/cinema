from django.urls import path

# from rest_framework.authtoken import views

from .views import *


urlpatterns = [
    path("api-token-auth/", AuthTokenView.as_view(), name="api_token_auth"),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("users_list/", GenerateRandomUserView.as_view(), name="users_list"),
    path("movie/", MovieViewSet.as_view({
        "get": "list",
        "post": "create"
    }), name="movie_list_create"),
    path("movie/<int:pk>/", MovieViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "delete": "destroy"
    }), name="movie_detail"),
    path("saloon/", SaloonViewSet.as_view({
        "get": "list",
        "post": "create"
    }), name="saloon_list_create"),
    path("saloon/<int:pk>//", SaloonViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "delete": "destroy"
    }), name="saloon_detail"),
    path("seans/", SeansViewSet.as_view({
        "get": "list",
        "post": "create"
    }), name="seans_list_create"),
    path("seans/<int:pk>/", SeansViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "delete": "destroy"
    }), name="seans_detail"),
    path("job_title/", JobTitleViewSet.as_view({
        "get": "list",
        "post": "create"
    }), name="job_title_list_create"),
    path("job_title/<int:pk>/", JobTitleViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "delete": "destroy"
    }), name="job_title_detail"),
    path("places/", PlacesViewSet.as_view({
        "get": "list",
        "post": "create",
    }), name="places_list_create"),
    path("places/<int:pk>/", PlacesViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "delete": "destroy"
    }), name="places_detail"),
    path("sector_saloon/", SectorSaloonViewSet.as_view({
        "get": "list",
        "post": "create"
    }), name="sector_saloon_list_create"),
    path("sector_saloon/<int:pk>/", SectorSaloonViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "delete": "destroy"
    }), name="sector_saloon_detail"),
    path("employees/", EmployeesViewSet.as_view({
        "get": "list",
        "post": "create"
    }), name="employees_list_create"),
    path("employees/<int:pk>/", EmployeesViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "delete": "destroy"
    }), name="employees_detail"),
    path("price_for_tickets/", PriceForTicketsViewSet.as_view({
        "get": "list",
        "post": "create"
    }), name="price_for_tickets_list_create"),
    path("price_for_tickets/<int:pk>", PriceForTicketsViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "delete": "destroy"
    }), name="price_for_tickets_detail"),
    path(
        "moving_tickets/",
        MovingTicketsListCreateAPIView.as_view(),
        name="moving_tickets",
    ),
    path(
        "moving_tickets/<int:pk>/",
        MovingTicketsRetrieveAPIVew.as_view(),
        name="moving_tickets_retrieve",
    ),
    path("movie_template", MovieTemplateView.as_view(), name="movie_template"),
]

from django.urls import path
# from rest_framework.authtoken import views

from .views import *

urlpatterns = [
    path("api-token-auth/", AuthTokenView.as_view(), name='api_token_auth'),


    path('movie/', MovieListAPIView.as_view()),
    path('saloon/', SaloonListAPIViews.as_view()),
    path('seans/',SeansListAPIViews.as_view()),
    path('seans/create/', SeansCreateAPIViews.as_view()),
    path('job_title/', JobTitleListAPIViews.as_view()),
    path('employees/', EmployeesListAPIViews.as_view()),
    path('employees/create/', EmployeesCreateAPIViews.as_view()),
    path('movie/create/', MovieCreateAPIViews.as_view()),
    path('movie/<int:pk>/', MovieRetrieveAPIView.as_view(), name='movie_retrieve'),
    path('seans/<int:pk>/', SeansRetrieveAPIView.as_view(), name='seans_retrieve'),
    path('employees/<int:pk>/', EmployeesRetrieveAPIView.as_view(), name='employee_retrieve'),
    path('job_title/<int:pk>/', JobTitleRetrieveAPIViews.as_view(), name='jobtitle_retrieve'),
    path('job_title/create/', JobTitleCreateAPIViews.as_view()),
    path('saloon/create/', SaloonCreateAPIViews.as_view()),
    path('saloon/<int:pk>/', SaloonRetrieveAPIViews.as_view(), name='saloon_retrieve'),
    path('places/', PlacesListAPIViews.as_view()),
    path('places/create/', PlacesCreateAPIViews.as_view()),
    path('places/<int:pk>/', PlacesRetrieveAPIViews.as_view(), name='places_retrieve'),
    path('sector_saloon/', SectorSaloonListAPIViews.as_view()),
    path('sector_saloon/create/', SectorSaloonCreateAPIViews.as_view()),
    path('sector_saloon/<int:pk>/', SectorSaloonRetrieveAPIViews.as_view(), name='sector_saloon_retrieve'),
    path('price_for_tickets/', PriceForTicketsListAPIViews.as_view()),
    path('price_for_tickets/create/', PriceForTicketsCreateAPIViews.as_view()),
    path('price_for_tickets/<int:pk>/', PriceForTicketsRetrieveAPIViews.as_view(), name='price_for_tickets_retrieve'),
    path('moving_tickets/', MovingTicketsListCreateAPIView.as_view(), name='moving_tickets'),
    path('moving_tickets/<int:pk>/', MovingTicketsRetrieveAPIVew.as_view(), name='moving_tickets_retrieve'),
    path('movie_template', MovieTemplateView.as_view(), name='movie_template'),
    path('movie_detail/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('movie_create/', MovieCreateView.as_view(), name='movie_create'),
    
]

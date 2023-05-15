import django_filters
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework import filters, generics, status

from django.contrib.auth.models import User
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

from .models import *
from .serializers import *
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from rest_framework import viewsets
from django.urls import reverse
from .forms import *


# auth
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


from .tasks import create_random_user_accounts
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.contrib import messages


class GenerateRandomUserView(FormView):
    template_name = "blog/generate_random_users.html"
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data.get("total")
        create_random_user_accounts.delay(total)
        messages.success(
            self.request,
            "We are generating your random users! Wait a moment and refresh this page.",
        )
        return redirect("users_list")


class AuthTokenView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
                "user_id": user.pk,
                "email": user.email,
                "name": user.first_name,
            }
        )


class RegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializers

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )
        token, created = Token.objects.get_or_create(user=user)
        return Response({"username": user.username, "token": token.key})


class MovieTemplateView(ListView):
    template_name = "blog/blog.html"
    model = Movie
    # queryset = Movie.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["movies"] = self.model.objects.all()
        return context


class MovieFilter(django_filters.FilterSet):
    start_date = django_filters.NumberFilter(field_name="rental_start_date__year")
    class Meta:
        model = Movie
        fields = ("start_date", )

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
        django_filters.rest_framework.DjangoFilterBackend,
    )
    filterset_class = MovieFilter
    filterset_fields = ("sales_company", )
    search_fields = ("name", "sales_company")
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return MovieDetailSerializer
        return MovieSerializers


class SaloonFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Saloon
        fields = ("name",)


class SaloonViewSet(viewsets.ModelViewSet):
    queryset = Saloon.objects.all()
    serializer_class = SaloonSerializers
    filter_backends = (filters.SearchFilter,
                       filters.OrderingFilter,
                       django_filters.rest_framework.DjangoFilterBackend,
                       )
    filterset_class = SaloonFilter
    filterset_fields = ("name", )
    search_fields = ("name", )
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SaloonDetailSerializers
        return SaloonSerializers



class SeansFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name="date")

    class Meta:
        model = Seans
        fields = ("start_date",)


class SeansViewSet(viewsets.ModelViewSet):
    queryset = Seans.objects.all()
    serializer_class = SeansSerializers
    filter_backends = (filters.SearchFilter,
                       filters.OrderingFilter,
                       django_filters.rest_framework.DjangoFilterBackend,
                       )
    filterset_class = SeansFilter
    filterset_fields = ("start_date", )
    search_fields = ("movie", "saloon")
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SeansDetailSerializers
        return SeansSerializers


class TitleFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name="title", lookup_expr="icontains"
    )

    class Meta:
        model = JobTitle
        fields = ("title",)


class JobTitleViewSet(viewsets.ModelViewSet):
    queryset = JobTitle.objects.all()
    serializer_class = JobTitleSerializers
    filter_backends = (filters.SearchFilter,
                       filters.OrderingFilter,
                       django_filters.rest_framework.DjangoFilterBackend,
                       )
    filterset_class = TitleFilter
    filterset_fields = ("title", )
    search_fields = ("title", )

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return JobTitleDetailSerializers
        return JobTitleSerializers


class PlacesFilter(django_filters.FilterSet):
    saloon_name = django_filters.CharFilter(
        field_name="saloon", lookup_expr="name"
    )

    class Meta:
        model = Places
        fields = ("saloon_name",)


class PlacesViewSet(viewsets.ModelViewSet):
    queryset = Places.objects.all()
    serializer_class = PlaceSerializers
    filter_backends = (filters.SearchFilter,
                       filters.OrderingFilter,
                       django_filters.rest_framework.DjangoFilterBackend,
                       )
    filterset_class = PlacesFilter
    filterset_fields = ("saloon_name", )
    search_fields = ("saloon", "row_number", "row_place")
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PlacesDetailSerializers
        return PlaceSerializers


class SectorSaloonFilter(django_filters.FilterSet):
    sector_name = django_filters.CharFilter(
        field_name="name", lookup_expr="name"
    )

    class Meta:
        model = SectorSaloon
        fields = ("name",)


class SectorSaloonViewSet(viewsets.ModelViewSet):
    queryset = SectorSaloon.objects.all()
    serializer_class = SectorSaloonSerializers
    filter_backends = (filters.SearchFilter,
                       filters.OrderingFilter,
                       django_filters.rest_framework.DjangoFilterBackend,
                       )
    filterset_class = SectorSaloonFilter
    filterset_fields = ("name", )
    search_fields = ("name", "saloon")

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SectorSaloonDetailSerializers
        return SectorSaloonSerializers


class EmployeesFilter(django_filters.FilterSet):
    employee_name = django_filters.CharFilter(
        field_name="name", lookup_expr="name"
    )

    class Meta:
        model = Employees
        fields = ("name",)


class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializers
    filter_backends = (filters.SearchFilter,
                       filters.OrderingFilter,
                       django_filters.rest_framework.DjangoFilterBackend,
                       )
    filterset_class = EmployeesFilter
    filterset_fields = ("name", )
    search_fields = ("name", "title")

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return EmployeeDetailSerializers
        return EmployeesSerializers


class PriceForTicketsFilter(django_filters.FilterSet):
    seans = django_filters.CharFilter(
        field_name="seanse", lookup_expr="icontains"
    )

    class Meta:
        model = PriceForTickets
        fields = ("seans",)


class PriceForTicketsViewSet(viewsets.ModelViewSet):
    queryset = PriceForTickets.objects.all()
    serializer_class = PriceForTickets
    filter_backends = (filters.SearchFilter,
                       filters.OrderingFilter,
                       django_filters.rest_framework.DjangoFilterBackend,
                       )
    filterset_class = PriceForTicketsFilter
    filterset_fields = ("seans")
    search_fields = ("seans", "sector")

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PriceForTicketsDetailSerializers
        return PriceForTicketsSerializers


class MovingTicketsListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = MovingTicketsSerializers
    queryset = MovingTickets.objects.all()
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


class MovingTicketsRetrieveAPIVew(
    generics.RetrieveAPIView, generics.DestroyAPIView, generics.UpdateAPIView
):
    serializer_class = MovingTicketsSerializers
    queryset = MovingTickets.objects.all()
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def update(self, request, *args, **kwargs):
        # береме запись
        isinstance = self.get_object()
        # Проверяем, что пользователь является создателем записи
        if isinstance.seller == request.user:
            return super().update(request, *args, **kwargs)
        else:
            return Response(
                status=status.HTTP_403_FORBIDDEN,
                data={"message": "You are not the owner of this record"},
            )

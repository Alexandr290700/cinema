from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserRegistrationSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    password2 = serializers.CharField()

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Пароли не совпадают")
        return data


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            "id",
            "name",
            "duration",
            "rental_start_date",
            "rental_finish_date",
            "sales_company",
        )

    # def create(self, validated_data):
    #     movie_name = validated_data.pop('name').get('name')                         ### ДЛЯ FOREIGN KEY!!!
    #     film = Movie.objects.create(name=movie_name, **validated_data)
    #     return film


class MovieSessionSerializers(serializers.ModelSerializer):
    saloon = serializers.StringRelatedField()

    class Meta:
        model = Seans
        fields = ["id", "saloon", "date"]


class MovieDetailSerializer(serializers.ModelSerializer):
    movie_session = MovieSessionSerializers(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = (
            "id",
            "name",
            "duration",
            "rental_start_date",
            "rental_finish_date",
            "sales_company",
            "movie_session",
        )


class SaloonSerializers(serializers.ModelSerializer):
    name = serializers.StringRelatedField()

    class Meta:
        model = Saloon
        fields = (
            "id",
            "name",
            "count_place",
            "description",
            "number_of_rows",
            "number_of_places",
        )

    # def create(self, validated_data):
    #     saloon_name = validated_data.pop('name').get('name')                         ### ДЛЯ FOREIGN KEY!!!
    #     saloon = Saloon.objects.create(saloon_name=saloon_name, **validated_data)
    #     return saloon


class RoomSerializers(serializers.ModelSerializer):
    name = serializers.StringRelatedField()

    class Meta:
        model = Saloon
        fields = (
            "id",
            "name",
            "count_place",
            "description",
            "number_of_rows",
            "number_of_places",
        )


class SaloonDetailSerializers(serializers.ModelSerializer):
    saloon_name = RoomSerializers(many=True, read_only=True)
    name = serializers.StringRelatedField()

    class Meta:
        model = Saloon
        fields = (
            "id",
            "name",
            "count_place",
            "description",
            "number_of_rows",
            "number_of_places",
            "saloon_name",
        )


class SeansSerializers(serializers.ModelSerializer):
    saloon = serializers.StringRelatedField()
    movie = serializers.StringRelatedField()

    class Meta:
        model = Seans
        fields = (
            "id",
            "saloon",
            "date",
            "time",
            "movie",
        )

    # def create(self, validated_data):
    #     movie_name = validated_data.pop('movie').get('movie')                         ### ДЛЯ FOREIGN KEY!!!
    #     film = Seans.objects.create(movie=movie_name, **validated_data)
    #     return film


class SeansMovieSerializers(serializers.ModelSerializer):
    saloon = serializers.StringRelatedField()
    movie = serializers.StringRelatedField()

    class Meta:
        model = Seans
        fields = ["id", "saloon", "movie", "date"]


class SeansDetailSerializers(serializers.ModelSerializer):
    seans_movie = SeansMovieSerializers(many=True, read_only=True)
    saloon = serializers.StringRelatedField()
    movie = serializers.StringRelatedField()

    class Meta:
        model = Seans
        fields = ("id", "saloon", "date", "time", "movie", "seans_movie")


class JobTitleSerializers(serializers.ModelSerializer):
    title = serializers.StringRelatedField()

    class Meta:
        model = JobTitle
        fields = ("title",)

        # def create(self, validated_data):
        #     job_title = validated_data.pop('title').get('title')                         ### ДЛЯ FOREIGN KEY!!!
        #     title = JobTitle.objects.create(title=job_title, **validated_data)
        #     return title


class JobTitlesSerializers(serializers.ModelSerializer):
    title = serializers.StringRelatedField()

    class Meta:
        model = JobTitle
        fields = ("title",)


class JobTitleDetailSerializers(serializers.ModelSerializer):
    title = serializers.StringRelatedField()
    job_title = JobTitlesSerializers(many=True, read_only=True)

    class Meta:
        model = JobTitle
        fields = ("id", "title", "job_title")


class PlacesSerializers(serializers.ModelSerializer):
    saloon = serializers.StringRelatedField()

    class Meta:
        model = Places
        fields = (
            "saloon",
            "row_number",
            "row_place",
        )

    # def create(self, validated_data):
    #     saloon_name = validated_data.pop('saloon').get('saloon')
    #     saloon = Saloon.objects.get(saloon=saloon_name)                         ### ДЛЯ FOREIGN KEY!!!
    #     place = Employees.objects.create(place=saloon, **validated_data)
    #     return place


class PlaceSerializers(serializers.ModelSerializer):
    saloon = serializers.StringRelatedField()

    class Meta:
        model = Places
        fields = ["saloon", "row_number", "row_place"]


class PlacesDetailSerializers(serializers.ModelSerializer):
    saloon = serializers.StringRelatedField()
    place = PlaceSerializers(many=True, read_only=True)

    class Meta:
        model = Places
        fields = ["saloon", "row_number", "row_place", "place"]


class SectorSaloonSerializers(serializers.ModelSerializer):
    saloon = serializers.StringRelatedField()
    name = serializers.StringRelatedField()

    class Meta:
        model = SectorSaloon
        fields = (
            "saloon",
            "name",
            "description",
        )

    # def create(self, validated_data):
    #     saloon_name = validated_data.pop('saloon').get('saloon')
    #     saloon = Saloon.objects.get(saloon=saloon_name)                         ### ДЛЯ FOREIGN KEY!!!
    #     sector = SectorSaloon.objects.create(sector=saloon, **validated_data)
    #     return sector


class SaloonSectorSerializers(serializers.ModelSerializer):
    saloon = serializers.StringRelatedField()
    name = serializers.StringRelatedField()

    class Meta:
        model = SectorSaloon
        fields = [
            "saloon",
            "name",
            "description",
        ]


class SectorSaloonDetailSerializers(serializers.ModelSerializer):
    saloon = serializers.StringRelatedField()
    name = serializers.StringRelatedField()
    sector_saloon = SaloonSectorSerializers(many=True, read_only=True)

    class Meta:
        model = SectorSaloon
        fields = ["saloon", "name", "description", "sector_saloon"]


class EmployeesSerializers(serializers.ModelSerializer):
    title = serializers.CharField(source="title.title")

    class Meta:
        model = Employees
        fields = (
            "name",
            "title",
            "password",
        )

    # def create(self, validated_data):
    #     title_name = validated_data.pop('title').get('title')
    #     job = JobTitle.objects.get(title=title_name)                         ### ДЛЯ FOREIGN KEY!!!
    #     employee = Employees.objects.create(title=job, **validated_data)
    #     return employee


class EmployeeJobSerializers(serializers.ModelSerializer):
    title = serializers.CharField(source="title.title")

    class Meta:
        model = Employees
        fields = ["id", "name", "title", "password"]


class EmployeeDetailSerializers(serializers.ModelSerializer):
    employee = EmployeeJobSerializers(many=True, read_only=True)
    title = serializers.CharField(source="title.title")

    class Meta:
        model = Employees
        fields = ["id", "name", "title", "password", "employee"]


class PriceForTicketsSerializers(serializers.ModelSerializer):
    seanse = serializers.StringRelatedField()
    sector = serializers.StringRelatedField()
    price = serializers.StringRelatedField()

    class Meta:
        model = PriceForTickets
        fields = (
            "seanse",
            "sector",
            "price",
        )

    # def create(self, validated_data):
    #     price = validated_data.pop('price').get('price')
    #     seans = Seans.objects.get(sector=price)                         ### ДЛЯ FOREIGN KEY!!!
    #     sector = SectorSaloon.objects.create(sector=seans, **validated_data)
    #     return sector


class PriceTicketSerializers(serializers.ModelSerializer):
    seanse = serializers.StringRelatedField()
    sector = serializers.StringRelatedField()

    class Meta:
        model = PriceForTickets
        fields = (
            "seanse",
            "sector",
            "price",
        )


class PriceForTicketsDetailSerializers(serializers.ModelSerializer):
    seanse = serializers.StringRelatedField()
    sector = serializers.StringRelatedField()
    price_for_tickets = PriceTicketSerializers(many=True, read_only=True)

    class Meta:
        model = PriceForTickets
        fields = ("seanse", "sector", "price", "price_for_tickets")


class MovingTicketsSerializers(serializers.ModelSerializer):
    ticket = serializers.CharField(source="ticket.number")

    # employee = serializers.CharField(source='employee.name')
    class Meta:
        model = MovingTickets
        fields = (
            "id",
            "moving_tickets",
            "ticket",
            "date_create",
            "operation",
        )
        read_only_fields = (
            "id",
            "date_create",
        )

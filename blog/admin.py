from django.contrib import admin
from .models import Movie, Saloon, Seans, JobTitle, Places, SectorSaloon, Employees, PriceForTickets, Tickets, MovingTickets


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'duration', 'rental_start_date', 'rental_finish_date', 'sales_company')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'duration')
    list_filter = ('id', 'rental_start_date')

class SaloonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'count_place', 'description', 'number_of_rows', 'number_of_places')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    list_filter = ('id', 'count_place')

class SeansAdmin(admin.ModelAdmin):
    list_display = ('id', 'saloon', 'date', 'time', 'movie')
    list_display_links = ('id', 'saloon')
    search_fields = ('saloon', )
    list_filter = ('saloon', 'movie')

class JobTitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_filter = ('id', )

class PlacesAdmin(admin.ModelAdmin):
    list_display = ('id', 'saloon', 'row_number', 'row_place')
    list_display_links = ('id', 'saloon')
    search_fields = ('saloon', )
    list_filter = ('id', 'saloon')

class SectorSaloonAdmin(admin.ModelAdmin):
    list_display = ('id', 'saloon', 'name', 'description')
    list_display_links = ('id', 'saloon', 'name')
    search_fields = ('saloon', 'name')
    list_filter = ('id', 'saloon', 'name')

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'password')
    list_display_links = ('id', 'name', 'title')
    search_fields = ('name', 'title')
    list_filter = ('id', 'name', 'title')

class PriceForTicketsAdmin(admin.ModelAdmin):
    list_display = ('id', 'seanse', 'sector', 'price')
    list_display_links = ('id', 'seanse', 'sector')
    search_fields = ('seanses', 'sector')
    list_filter = ('id', 'seanse', 'sector')

class TicketsAdmin(admin.ModelAdmin):
    list_display = ('ticket_number', 'date_created', 'seanses', 'places', 'played', 'booking', 'creashed')
    list_display_links = ('ticket_number', 'date_created', 'seanses')
    search_fields = ('seanses', 'ticket_number')
    list_filter = ('ticket_number', 'date_created', 'seanses')

class MovingTicketsAdmin(admin.ModelAdmin):
    list_display = ('id', 'moving_tickets', 'ticket', 'date_create', 'operation', )
    list_display_links = ('id', 'moving_tickets','ticket', )
    search_fields = ('ticket', )
    list_filter = ('id', 'ticket')
    

admin.site.register(Movie, MovieAdmin)
admin.site.register(Saloon, SaloonAdmin)
admin.site.register(Seans, SeansAdmin)
admin.site.register(JobTitle, JobTitleAdmin)
admin.site.register(Places, PlacesAdmin)
admin.site.register(SectorSaloon, SectorSaloonAdmin)
admin.site.register(Employees, EmployeesAdmin)
admin.site.register(PriceForTickets, PriceForTicketsAdmin)
admin.site.register(Tickets, TicketsAdmin)
admin.site.register(MovingTickets, MovingTicketsAdmin)


    

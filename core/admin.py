from django.contrib import admin
from .models import Customer, Driver, Booking


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'created_at')
    search_fields = ('full_name', 'email', 'phone_number')


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'license_number', 'is_available')
    search_fields = ('full_name', 'phone_number', 'license_number')
    list_filter = ('is_available',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'driver', 'pickup_location', 'dropoff_location', 'pickup_time', 'status', 'created_at')
    search_fields = ('customer__full_name', 'driver__full_name', 'pickup_location', 'dropoff_location')
    list_filter = ('status', 'created_at', 'pickup_time')
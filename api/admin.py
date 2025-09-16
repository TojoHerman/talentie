from django.contrib import admin
from .models import OrgProfile, Event, MediaItem, Course, RegistrationRequest, BookingRequest

@admin.register(OrgProfile)
class OrgProfileAdmin(admin.ModelAdmin):
    list_display = ("naam", "start_jaar", "email", "telefoon")
    search_fields = ("naam", "beschrijving", "missie", "visie", "email", "telefoon")

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("titel", "start_at", "locatie", "is_published", "allow_registration")
    list_filter = ("is_published", "allow_registration")
    search_fields = ("titel", "beschrijving", "locatie")

@admin.register(MediaItem)
class MediaItemAdmin(admin.ModelAdmin):
    list_display = ("title", "kind", "is_published", "published_at")
    list_filter = ("kind", "is_published")
    search_fields = ("title", "url")

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("titel", "docent", "is_published")
    list_filter = ("is_published",)
    search_fields = ("titel", "beschrijving", "docent")

@admin.register(RegistrationRequest)
class RegistrationRequestAdmin(admin.ModelAdmin):
    list_display = ("type", "naam", "email", "telefoon", "created_at")
    list_filter = ("type",)
    search_fields = ("naam", "email", "telefoon", "bericht")

@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    list_display = ("organisator", "contact_email", "contact_tel", "event_datum", "locatie", "created_at")
    search_fields = ("organisator", "contact_email", "contact_tel", "locatie", "bericht")

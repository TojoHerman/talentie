from rest_framework import serializers
from .models import OrgProfile, Event, MediaItem, Course, RegistrationRequest, BookingRequest

class OrgProfileSer(serializers.ModelSerializer):
    class Meta: model = OrgProfile; fields = "__all__"

class EventSer(serializers.ModelSerializer):
    class Meta: model = Event; fields = "__all__"

class MediaSer(serializers.ModelSerializer):
    class Meta: model = MediaItem; fields = "__all__"

class CourseSer(serializers.ModelSerializer):
    class Meta: model = Course; fields = "__all__"

class RegistrationSer(serializers.ModelSerializer):
    class Meta: model = RegistrationRequest; fields = "__all__"

class BookingSer(serializers.ModelSerializer):
    class Meta: model = BookingRequest; fields = "__all__"

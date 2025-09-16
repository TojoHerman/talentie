from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import OrgProfile, Event, MediaItem, Course, RegistrationRequest, BookingRequest
from .serializers import *

@api_view(["GET"])
def health(_request):
    return Response({"status": "ok"})

# Public read-only
class ProfileViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = OrgProfile.objects.all()
    serializer_class = OrgProfileSer

class EventViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Event.objects.filter(is_published=True).order_by("start_at")
    serializer_class = EventSer

class MediaViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = MediaItem.objects.filter(is_published=True).order_by("-published_at")
    serializer_class = MediaSer

class CourseViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Course.objects.filter(is_published=True).order_by("-created_at")
    serializer_class = CourseSer

# Public forms (POST only)
class RegistrationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = RegistrationRequest.objects.all()
    serializer_class = RegistrationSer

class BookingViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = BookingRequest.objects.all()
    serializer_class = BookingSer
    

from django.db import models

class OrgProfile(models.Model):
    naam = models.CharField(max_length=120, default="Gadoe Talentie")
    start_jaar = models.IntegerField(null=True, blank=True)
    missie = models.TextField(blank=True)
    visie = models.TextField(blank=True)
    beschrijving = models.TextField(blank=True)
    foto_url = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    telefoon = models.CharField(max_length=50, blank=True)
    adres = models.CharField(max_length=200, blank=True)
    website_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    logo_url = models.URLField(blank=True, null=True)


class Event(models.Model):
    titel = models.CharField(max_length=200)
    beschrijving = models.TextField(blank=True)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField(null=True, blank=True)
    locatie = models.CharField(max_length=200, blank=True)
    cover_url = models.URLField(blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    allow_registration = models.BooleanField(default=False)
    registration_note = models.CharField(max_length=200, blank=True)  # optional helper text

    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.titel

class MediaItem(models.Model):
    KIND_CHOICES = (("image","image"),("video","video"),("link","link"))
    kind = models.CharField(max_length=10, choices=KIND_CHOICES)
    title = models.CharField(max_length=200, blank=True)
    url = models.URLField()
    thumb_url = models.URLField(blank=True)
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-published_at", "-id"]

    def __str__(self):
        return self.title or f"{self.kind}: {self.url}"

class Course(models.Model):
    titel = models.CharField(max_length=200)
    beschrijving = models.TextField(blank=True)
    docent = models.CharField(max_length=120, blank=True)
    prijs_srd = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    duur_text = models.CharField(max_length=80, blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class RegistrationRequest(models.Model):
    TYPE_CHOICES = (("lid","lid"),("cursus","cursus"),("algemeen","algemeen"))
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default="algemeen")
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.SET_NULL)
    naam = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    telefoon = models.CharField(max_length=50, blank=True)
    bericht = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class BookingRequest(models.Model):
    organisator = models.CharField(max_length=200, blank=True)
    contact_email = models.EmailField(blank=True)
    contact_tel = models.CharField(max_length=50, blank=True)
    event_datum = models.DateField(null=True, blank=True)
    locatie = models.CharField(max_length=200, blank=True)
    aantal_optredens = models.IntegerField(default=1)
    budget_srd = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    bericht = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

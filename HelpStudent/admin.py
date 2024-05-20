from django.contrib import admin
from .models import Logement, Event, Publication, StageOffer,Transport

# Register your models here.
admin.site.register(Logement)
admin.site.register(Event)
admin.site.register(StageOffer)
admin.site.register(Transport)
admin.site.register(Publication)

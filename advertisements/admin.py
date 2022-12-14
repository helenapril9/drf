from django.contrib import admin

# Register your models here.
from .models import Advertisement, AdvertisementStatusChoices



@admin.register(Advertisement)
class AdvertisementsAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'description',  'creator', 'created_at', 'updated_at']

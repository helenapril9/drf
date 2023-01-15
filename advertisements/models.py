from django.conf import settings
from django.db import models
from django_filters import DateFromToRangeFilter
from django_filters.filterset import BaseFilterSet


class AdvertisementStatusChoices(models.TextChoices):
    """Статусы объявления."""
    OPEN = "OPEN", "Открыто"
    CLOSED = "CLOSED", "Закрыто"

class Advertisement(models.Model):
    """Объявление."""
    title = models.TextField()
    description = models.TextField(default='')
    status = models.TextField(
        choices=AdvertisementStatusChoices.choices,
        default=AdvertisementStatusChoices.OPEN
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name= 'creator'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

class F(BaseFilterSet):
    created_at = DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at']

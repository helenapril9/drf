from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.viewsets import ModelViewSet
from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOrReadOnly
from advertisements.serializers import AdvertisementSerializer
from advertisements.filters import AdvertisementFilter

class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class=AdvertisementFilter
    filterset_fields = ['status']
    permitions_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serialiser):
        def set_creator(self, request, pk=None):
            creator =self.get_object()
        serialiser.save(creator=self.request.user)

    def get_permissions(self):
       if self.action in ("create","update", "partial_update", "destroy"):
         return [IsAuthenticated(), IsOwnerOrReadOnly()]
       return[]





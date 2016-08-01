from Sansa import  models,serializer
from rest_framework import serializers,viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializer.UserSerializer

class AssetViewSet(viewsets.ModelViewSet):
    queryset = models.Asset.objects.all()
    serializer_class = serializer.AssetSerializer

class ManufactoryViewSet(viewsets.ModelViewSet):
    queryset = models.Manufactory.objects.all()
    serializer_class = serializer.ManufactorySerializer
from Sansa import models
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('url','email','name','is_staff')

class AssetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Asset
        depth = 2
        fields = ('url','sn','name','asset_type','manufactory','create_date')

class ManufactorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Manufactory
        fields = ('url','manufactory','support_num','memo')
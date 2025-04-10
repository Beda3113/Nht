from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(read_only=True)

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator', 'status', 'created_at')
        read_only_fields = ('created_at',)

    def create(self, validated_data):
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        request = self.context.get("request")
        
        if request.method == 'POST' or (request.method in ['PUT', 'PATCH'] and data.get('status') == 'OPEN'):
            user = request.user
            open_ads_count = Advertisement.objects.filter(
                creator=user,
                status='OPEN'
            ).count()
            
            if self.instance and self.instance.status != 'OPEN':
                open_ads_count += 1
            
            if open_ads_count >= 10:
                raise ValidationError("Нельзя иметь больше 10 открытых объявлений")
        
        return data

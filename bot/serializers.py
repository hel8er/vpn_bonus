from rest_framework import serializers
from .models import TgUser
from rest_framework import serializers
from .schemas import Chat


class TgUserSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    username = serializers.CharField(max_length=50)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    queryset = TgUser.objects.all()

    class Meta:
        model = TgUser




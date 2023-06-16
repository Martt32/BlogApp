from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserPublicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email =serializers.CharField(read_only= True)
    profile = serializers.CharField(read_only=True)

    # def get_related_fields(self, obj):
    #     user = obj
    #     my_games_qs = Product.objects.all()[:4]
    #     return UserGameInlineSerializer(my_games_qs,
    #     many=True,
    #     context=self.context).data

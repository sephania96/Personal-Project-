from rest_framework import serializers
from movies import models


class moviesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "title",
            "content",
            "rating",
            "created_at",
        )
        model = models.movies
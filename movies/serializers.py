from rest_framework import serializers
from .models import Movie
from movies.models import RatingMovie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, required=False)
    rating = serializers.ChoiceField(
        choices=RatingMovie.choices,
        default=RatingMovie.G
    )
    synopsis = serializers.CharField(required=False, default=None)
    added_by = serializers.SerializerMethodField()

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)
    
    def get_added_by(self, obj: Movie) -> str:
        return obj.user.email

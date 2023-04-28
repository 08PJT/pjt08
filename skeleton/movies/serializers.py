from .models import Movie, Genre
from rest_framework import serializers

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        
class MovieSerializer(serializers.ModelSerializer):
    # name = GenreSerializer(read_only=True, source='genre_set')
    class Meta:
        model = Movie
        fields = '__all__'
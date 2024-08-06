from rest_framework import serializers
from django.db.models import Avg
from movies.models import Movie


class MovieModelSerializer(serializers.ModelSerializer):

    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        
        if rate:
            return round(rate, 1)
        
        return None

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('A data de lancamento nao pode ser anterior a 1900.')
        return value
    
    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('campo de resumo nao pode ter mais de 500 caracteres.')
        return value
    
class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movie_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()
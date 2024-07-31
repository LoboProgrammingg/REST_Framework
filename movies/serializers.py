from rest_framework import serializers
from movies.models import Movie


class MovieModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1970:
            raise serializers.ValidationError('A data de lancamento nao pode ser anterior a 1970.')
        return value
    
    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('campo de resumo nao pode ter mais de 200 caracteres.')
        return value
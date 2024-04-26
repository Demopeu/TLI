from rest_framework import serializers
from .models import Actor,Movie,Review

class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ['id','name',]

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['title','overview',]

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

class ReviewSerializer2(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['title','content',]

class ActorDetailSerializer(serializers.ModelSerializer):
    class MovieTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ['title',]
    movies = MovieTitleSerializer(many=True, read_only=True)
    class Meta:
        model = Actor
        fields = ['id','name','movies',]

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['title','overview',]

class MovieDetailSerializer(serializers.ModelSerializer):
    class ActorsNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ['name',]
    actors = ActorsNameSerializer(many = True,read_only = True)
    review_set = ReviewSerializer(many = True,read_only = True)
    class Meta:
        model = Movie
        fields = ['id','actors','review_set',]

class ReviewDetailSerializer(serializers.ModelSerializer):
    class MovieTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ['title',]
    movie = MovieTitleSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ['id','movie','title','content',]
        read_only_fields = ('movie',)
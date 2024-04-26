from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from .models import Actor,Movie,Review
from rest_framework import status
from .serializers import ActorSerializer,MovieSerializer,ActorDetailSerializer, MovieDetailSerializer,ReviewSerializer2,ReviewDetailSerializer
# Create your views here.

@api_view(['GET'])
def actor_list(request):
    actors = Actor.objects.all()
    serializers = ActorSerializer(actors, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def actor_detail(request,actor_pk):
    actor = Actor.objects.get(pk=actor_pk)
    serializers = ActorDetailSerializer(actor)
    return Response(serializers.data)

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializers = MovieSerializer(movies,many = True)
    return Response(serializers.data)

@api_view(['GET'])
def movie_detail(request,movie_pk):
    movies = Movie.objects.get(pk=movie_pk)
    serializers =  MovieDetailSerializer(movies)
    return Response(serializers.data)

@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializers =  ReviewSerializer2(reviews,many = True)
    return Response(serializers.data)

@api_view(['GET','PUT','DELETE'])
def review_detail(request,review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == 'GET':
        serializers = ReviewDetailSerializer(review)
        return Response(serializers.data)
    elif request.method == 'PUT':
        serializers = ReviewDetailSerializer(review, data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response({"message": f"review {review_pk} is deleted."},status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_review(request,movie_pk):
    movie = Movie.objects.get(pk = movie_pk)
    serializers = ReviewDetailSerializer(data=request.data)
    if serializers.is_valid(raise_exception=True):
        serializers.save(movie=movie)
    return Response(serializers.data,status=status.HTTP_201_CREATED)
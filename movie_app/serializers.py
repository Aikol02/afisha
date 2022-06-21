from .models import Director, Movie, Review, Genre, Tag
from rest_framework import serializers


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "id name ".split()



class DirectorDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"




class ReviweSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "id text movie stars rating ".split()


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "id ganre".split()


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "id htag".split()


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "id title ".split()


class MovieDetailSerializer(serializers.ModelSerializer):
    ganre = GenreSerializer()
    tag = TagSerializer(many=True)
    review = ReviweSerializer(many=True)

    class Meta:
        model = Movie
        fields = "id title ganre tag tag_list review".split()

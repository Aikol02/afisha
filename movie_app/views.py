from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import (
    DirectorSerializers,
    DirectorDetailSerializers,
    MovieSerializer,
    MovieDetailSerializer,
    ReviweSerializer,ReviewDetailSerializer
)
from .models import Director, Movie, Review
from rest_framework import status


@api_view(["GET","POST"])
def director_list_view(request):
    if request.method == "GET":
        persons = Director.objects.all()
        data = DirectorSerializers(persons, many=True).data
        return Response(data=data)
    else:
        name = (request.data.get('name', ''))
        first_name = (request.data.get('first_name', ''))
        age = (request.data.get('age','0'))


        directory = Director.objects.create(
            name=name,
            first_name=first_name,
            age=age,
        )
        return Response(status=status.HTTP_201_CREATED,
                        data={'message': DirectorSerializers(directory).data})

@api_view(["GET","PUT","DELETE"])
def director_detail_view(request, id):
    try:

        persons = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(
            data={"error": "Did not Director"}, status=status.HTTP_404_NOT_FOUND
        )
    if request.method == "GET":
        data = DirectorDetailSerializers(persons, many=False).data
        return Response(data=data)
    elif request.method == "DELETE":
        persons.delete()
        return Response(data={"message":"Director remove"})
    else:
        persons.name = (request.data.get('name', ''))
        persons.first_name = (request.data.get('first_name', ''))
        persons.age = (request.data.get('age', '0'))

        persons.save()

        return Response(data=DirectorDetailSerializers(persons).data)


@api_view(["GET","POST"])
def movie_list_view(request):
    if request.method == "GET":
        mov = Movie.objects.all()
        data = MovieSerializer(mov, many=True,).data
        return Response(data=data)
    else:
        ganre = (request.data.get("ganre",None))
        tag = (request.data.get('tag',[]))
        title = (request.data.get("title",""))
        description = (request.data.get("description",""))
        duration = (request.data.get("duration",1))
        director = (request.data.get("director",None))

        mov = Movie.objects.create(
            ganre=ganre,
            title=title,
            description=description,
            duration=duration,
            director=director,
        )
        mov.tag.set(tag)
        mov.save()

        return Response(status=status.HTTP_201_CREATED,
                        data={'message':MovieSerializer(mov).data})





@api_view(["GET","PUT","DELETE"])
def movie_detail_view(request, id):
    try:

        move = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(
            data={"error": "Did not movie "}, status=status.HTTP_404_NOT_FOUND
        )
    if request.method == "GET":
        data = MovieDetailSerializer(move, many=False).data
        return Response(data=data)
    elif request.method == "DELETE":
        move.delete()
        return Response(data={"Message":"Movie on delete"})
    else:
        move.ganre = (request.data.get("ganre", None))
        move.tag.set(request.data.get('tags',[]))
        move.title = (request.data.get("title", ""))
        move.description = (request.data.get("description", ""))
        move.duration = (request.data.get("duration", 1))
        move.director = (request.data.get("director", None))


        move.save()

        return Response(data=MovieDetailSerializer(move).data)

@api_view(["GET","POST"])
def review_list_view(request):
    persons = Review.objects.all()
    if request.method == "GET":
        data = ReviweSerializer(persons, many=True).data
        return Response(data=data)
    else:
        stars = (request.data.get("stars"))
        text = (request.data.get('text'))
        movie = (request.data.get("movie"))

        rew = Review.objects.create(
            stars=stars,
            text=text,
            movie=movie,
        )
        return Response(status=status.HTTP_201_CREATED,
                        data={'message': ReviweSerializer(rew).data})

@api_view(["GET","PUT","DELETE"])
def review_detail_view(request,id):
    try:

        rew = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(
            data={"error": "Did not Review "}, status=status.HTTP_404_NOT_FOUND
        )
    if request.method == "GET":
        data = ReviewDetailSerializer(rew,many=False).data
        return Response(data=data)
    elif request.method == "DELETE":
        rew.delete()
        return Response(data={"message":"Review removed"})
    else:
        rew.stars = (request.data.get("stars"))
        rew.text = (request.data.get('text'))
        rew.movie = (request.data.get("movie"))

        rew.save()

        return Response(data=MovieDetailSerializer(rew).data)
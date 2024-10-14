from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Choclate
from .serializer import ChoclateSerializer

@api_view(['GET'])
def get_chocolates(request):
    objs = Choclate.objects.all()
    serializer = ChoclateSerializer(objs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_chocolate(request):
    data = request.data
    serializer = ChoclateSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['PUT'])
def update_chocolate(request, id):
    obj = Choclate.objects.get(id=id)
    data = request.data
    serializer = ChoclateSerializer(obj, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['PATCH'])
def partial_update_chocolate(request, id):
    obj = Choclate.objects.get(id=id)
    data = request.data
    serializer = ChoclateSerializer(obj, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def delete_chocolate(request, id):
    obj = Choclate.objects.get(id=id)
    obj.delete()
    return Response({"message": "Chocolate is deleted"})

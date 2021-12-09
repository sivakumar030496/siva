from rest_framework.decorators import api_view
from .models import employees
from .serializers import employeesSerializer,GroupSerializer
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def details(request):
    action=employees.objects.all()
    serializer=employeesSerializer(action,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create(request):
   home=GroupSerializer(data=request.data)
   if home.is_valid():
       Group=home.save()
   request.data['Branch'] =Group.id
   TTT=employeesSerializer(data=request.data)
   if TTT.is_valid():
       TTT.save()
   return Response(TTT.data)


@api_view(['DELETE'])
def delete1(request,id):
    details=employees.objects.get(id=id)
    details.delete()
    return Response('deleted')

@api_view(['PATCH'])
def update(request,id):
    apidetails=employees.objects.get(id=id)
    serializer=employeesSerializer(instance=apidetails,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
from django.shortcuts import render
from rest_framework.views import APIView
from serializers import NewUserSerializer
from rest_framework.response import Response
from Apps.BackendApp.models import NewUser

# Create your views here.



class SaveUsers(APIView):
    def post(self,request):
        NewUserSerializerObj = NewUserSerializer(data= request.data)

        if NewUserSerializerObj.is_valid():
            NewUserSerializerObj.save()

        return Response("New user got created")
    

class RenderUser(APIView):
    def get(self,request):
        UserObj = NewUser.objects.all()
        if len(UserObj) ==0:
            return Response("No contact added yet")
        
        else:
            UserObjects = []
            for obj in UserObj:
                UserObjects.append({"name": obj.name, "email": obj.email})

            return Response({"userData":UserObjects})



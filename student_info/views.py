from django.shortcuts import render
from .models import Student
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.

@api_view(['POST'])
def insertData(request):
    data = StudentSerializer(data=request.data)
    if data.is_valid():
        data.save()
        return Response({"message":"Successfully Inserted"})
    else:
        return Response({"message": "Something went Wrong!!!"})


@api_view(['GET'])
def viewData(request):
    # ide = request.POST['id']
    data = Student.objects.all()
    serializer = StudentSerializer(data,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def updateData(request,pk):
    # ide = request.POST['id']
    data = Student.objects.get(id=pk)
    serializer = StudentSerializer(instance=data,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Updated!!"})
    else:
        return Response({"message": "Not valid!!"})

@api_view(['POST'])
def customUpdate(request):
    ide = request.POST['id']
    name = request.POST['name']
    data = Student.objects.filter(id = ide)
    if data.exists():
        data.update(name =name)
        return Response({"message":"Updated Successfully"})
    else:
        return Response({"message": "Vai bondo kor!!"})

@api_view(['POST'])
def deleteData(request):
    ide = request.POST['id']
    data = Student.objects.filter(id=ide)
    if data.exists():
        data.delete()
        return Response({"message":"Delete Successfully"})
    else:
        return Response({"message": "Something wrong"})

# @api_view(['POST'])
# def custom_login(request):
#     email = request.POST['mail']
#     name = request.POST['name']
#     user = Student.objects.filter(Q(name=name) & Q(mail=email))
#     if user.exists():
#         return Response("OKay Done")

@api_view(['POST'])
def user_login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']

    _,token = AuthToken.objects.create(user)

    return Response({
        "user_info":{
            "id":user.id,
            "username": user.username,
            "email": user.email
        },
        "token":token
    })

@api_view(['GET'])
def user_token_check(request):
    user = request.user
    if user.is_authenticated:
        return Response({
        "user_info":{
            "id":user.id,
            "username": user.username,
            "email": user.email
        },
    })

@api_view(['POST'])
def student_login(request):
    serializer = StuSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    student = serializer.validated_data['student']
    _,token = AuthToken.objects.create(student)

    return Response({
        "user_info":{
            "id": student.id,
            "name":student.name,
            "email":student.mail
        },
        "token":token
    })


@api_view(['POST'])
def user_registration(request):
    serializer = RegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()

    _,token = AuthToken.objects.create(user)
    return Response({
        "user_info":{
            "id": user.id,
            "name":user.username,
            "email":user.email
        },
        "token":token
    })


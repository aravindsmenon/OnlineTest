from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import JSONParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from TestApp.models import *
from TestApp.serializers import *
import os
import json

class FileTraverse(APIView):

    def get(self, request):

        for (dirpath, dirnames, filenames) in os.walk('.'):
            for f in filenames:
                filename = os.path.join(dirpath, f)
                print('FILE :', filename)

                filepath = os.path.abspath(filename)
                print("path:", filepath)

                file_stats = os.stat(filename)
                filesize = file_stats.st_size
                print("filesize in bytes:", filesize)

                extension = os.path.splitext(filename)[1]
                print("ext:", extension)

        serializer = UserSerializer(data=(filename,filepath,filesize,extension)) #request.data -> json
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)




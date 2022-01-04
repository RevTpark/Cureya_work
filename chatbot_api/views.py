from django.shortcuts import render
from rest_framework.views import APIView
import json
from django.http import JsonResponse
from rest_framework import status

# Create your views here.

class BotSolutions(APIView):

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))["message"]
        # solutions = manipulated data...
        return JsonResponse({"solutions": "THIS IS ALL THE SOLUTIONS"}, status=status.HTTP_200_OK)

from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def apihome(request,*args,**kwargs):
    return JsonResponse({'message': 'hi this is JsonResponse right!'})


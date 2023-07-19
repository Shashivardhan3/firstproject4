from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def fun1(request):
    return HttpResponse('first response')

def fun2(request):
    return HttpResponse('second response')

def fun3(request):
    return HttpResponse("shashi vardhan")
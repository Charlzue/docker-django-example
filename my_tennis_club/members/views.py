from django.shortcuts import render
from django.http import HttpResponse
 
def members(request):
    return HttpResponse("<h1>Hello world! Tigil na natin itong Term 2</h1>")
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse


def hello_view(request):
    return HttpResponse("hello world")

def time_now(request):
    return HttpResponse(datetime.now().isoformat())
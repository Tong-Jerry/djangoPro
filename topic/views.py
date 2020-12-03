from django.shortcuts import render
from django.http import JsonResponse
from tools.send_code import GetCode
from topic.models import Topics
# Create your views here.

def create_topic(request):
    if request.method == "POST":
        pass
    else:
        return JsonResponse(GetCode(12002))

def delect_topic(request, topic_id):
    if request.method == "POST":
        pass
    else:
        pass

def update_topic(request, topic_id):
    if request.method == "POST":
        pass
    else:
        pass


def select_topics(request):
    if request.method == "POST":
        pass
    else:
        pass


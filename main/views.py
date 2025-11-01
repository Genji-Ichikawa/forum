from django.shortcuts import render

from main.models import *


def index(request):
    topic_list = Topic.objects.all()
    context = {"topics": topic_list}
    return render(request, "main/index.html", context)

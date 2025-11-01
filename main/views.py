from django.shortcuts import render

from main.models import *


def index(request):
    topic_list = Topic.objects.all()
    context = {"topics": topic_list}
    return render(request, "main/index.html", context)


def forum(request, topic_name):
    topic = Topic.objects.get(name=topic_name)
    messages = Message.objects.filter(topic=topic).order_by("created_at")
    context = {
        "messages": messages,
        "topic": topic,
    }
    return render(request, "main/forum.html", context)

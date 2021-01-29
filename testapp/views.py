from django.shortcuts import render
from .models import Rubric


def nested_set(request):
    return render(request, "testapp/nested_set.html", {'rubrics': Rubric.objects.all()})


def get_rubrick(request):
    pass
from django.db.models import F, Sum
from django.shortcuts import render
from .models import *


def upravlenie(request):
    data = ConsumingOtoplenie.objects.all()
    otk = ConsumingOtoplenie.objects.annotate(min=F('limit') - F('fact'))
    return render(request, 'upravlenie/test.html', {'data': data, 'otk': otk })

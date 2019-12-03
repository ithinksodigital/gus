from django.shortcuts import render
from .models import *
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    d = Divorces2018.objects.order_by('divorces_2018')[:5]
    con = dict()
    # context = {'d':d}
    for i in d:
        con[i.region] = i.divorces_2018
    print(con)
    return JsonResponse(con)
    # return render(request,'tache/homepage.html', context)


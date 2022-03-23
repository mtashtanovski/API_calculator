from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def index_view(request):
    # if request.method == "GET":
    return render(request, 'index.html')

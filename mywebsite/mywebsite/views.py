from django.http import HttpResponse 
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

#function view about 
def about(request):
    return HttpResponse("ini halaman about")
from django.http import HttpResponse
from .models import movies
from django.shortcuts import render, redirect
from .forms import movieform

# Create your views here.
def index(request):
    movie=movies.objects.all()
    context={
        'movie_list': movie

    }
    return render(request,'index.html',context)

def details(request,movie_id):
    movie1=movies.objects.get(id=movie_id)
    return render(request,'details.html',{'m':movie1})

def add_movie(request):
    if request.method == 'POST':
        # name=request.POST.get('name')
        # desc=request.POST.get('desc')
        # year=request.POST.get('year')
        name=request.POST['name']
        desc=request.POST['desc']
        year=request.POST['year']
        img=request.FILES['img']
        m=movies(name=name,desc=desc,year=year,img=img)
        m.save()
    return render(request,'add.html')

def update(request,id):
    m=movies.objects.get(id=id)
    form1=movieform(request.POST or None,request.FILES,instance=m)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form1,'movie':m})

def delete(request,id):
    if request.method=='POST':
        m=movies.objects.get(id=id)
        m.delete()
        return  redirect('/')
    return render(request,'delete.html')
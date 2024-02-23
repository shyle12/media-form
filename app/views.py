from django.shortcuts import render,HttpResponse
from app.forms import movieform
from app.models import movie
# Create your views here.

def insert(request):
    if request.method=='GET':
        var=movieform()
        return render(request,'ins.html',{'var':var})
    elif request.method=='POST' and request.FILES:
        form=movieform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('DATA STORED IN A TABLE')
        
def up(request,pk):
    a=movie.objects.get(id=pk)
    if request.method=='GET':
        var=movieform(instance=a)
        return render(request,'ins.html',{'var':var})
    elif request.method=='POST' or request.FILES:
        form=movieform(request.POST,request.FILES,instance=a)
        if form.is_valid():
            form.save()
            return HttpResponse('DATA UPDATED IN A TABLE')
        
def delete(request,pk):
    movie.objects.filter(id=pk).delete()
    return HttpResponse('DATA DELETED IN A TABLE')

def read(request):
    a=movie.objects.all()
    return render(request,'read.html',{'var':a})
        

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Football
from .forms import FootballForm

# Create your views here.
def index(request):
    team=Football.objects.all()
    context={
        'team_list':team
    }
    return render(request, 'index.html', context)

def detail(request,team_id):
    team=Football.objects.get(id=team_id)
    return render(request,"detail.html",{'team':team})

def add_team(request):
    if request.method=='POST':
        team_name=request.POST.get('team_name',)
        coach_name = request.POST.get('coach_name', )
        desc = request.POST.get('desc', )
        year = request.POST.get('year', )
        img = request.FILES['img']

        team=Football(team_name=team_name,coach_name=coach_name,desc=desc,year=year,img=img)
        team.save()
    return render(request,'add.html')

def update(request,id):
    team=Football.objects.get(id=id)
    form=FootballForm(request.POST or None,request.FILES, instance=team)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'team':team})

def delete(request,id):
    if request.method=='POST':
        team=Football.objects.get(id=id)
        team.delete()
        return redirect('/')
    return render(request,'delete.html')
from unicodedata import category
from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from django.views import generic
# from django.urls import reverse_lazy
from .models import Projects1,Pelcon,Content, ProjectsEnrolled
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from Home.models import SiteSettings
from django.http import   HttpResponseRedirect
from math import ceil
import os

# from NB.Projects1 import models
# Create your views here.

def Input(request):
        if request.method == "POST" and "projectinpform":
            projname = request.POST.get('projname')
            categ = request.POST.get('category')
            desc = request.POST.get('desc')
            creatorname = request.POST.get('creatorname')
            dateandtime = request.POST.get('dateandtime')
            purpose = request.POST.get('Purpose')
            avail = request.POST.get('Availability')
            rating = request.POST.get('rating')
            if len(request.FILES) != 0:
                proj_img = request.FILES['projimage']
            if len(request.FILES) != 0:
                proj_video = request.FILES['projvideo']
            print(projname,categ,desc,creatorname,dateandtime,avail,rating,proj_img,proj_video)

            Projec = Projects1(
                projectname = projname,
                category = categ,
                desc = desc,
                creator = creatorname,
                datecreated =dateandtime,
                purpose = purpose,
                Availability =  avail,
                Image = proj_img,
                rating = rating,
                introvideo = proj_video
            )
            Projec.save()

        return render(request,'Projects1/input.html')

def GetSiteInfo(SiteId=1):
    return SiteSettings.objects.filter(id=SiteId).values()[0]

def Home1(request):
    try:
        params = {"CurrSiteInfo":GetSiteInfo()}
        allprojects = []
        project = Projects1.objects.values('categoryF','projectid')
        proj = []
        cate = {pj['categoryF'] for pj in project}
        cate = list(cate)
        dio = {key : 0 for key in cate}
        for produ in project:
            dio[produ['categoryF']] += 1

        for pro in dio.keys():
            ppjj = Projects1.objects.filter(categoryF = pro)
            n = dio[pro]
            nslides = n//3 + ceil((n/3)-(n//3))
            allprojects.append([ppjj,range(1,n), nslides])        
        if len(allprojects):
            params['project'] = allprojects
            return render(request,'Projects1/index.html',params)
        return render(request,'generalPages/commingSoonPage.html',params)
    except:
        return render(request,'ErrorPages\Error504.html',params)

def get_project_by_user(project,user):
    try:
        print(project,user)
        return ProjectsEnrolled.objects.get(profileId=user,courseid=project)
    except :
        return None
    
def get_user_info(user_name):
     return User.objects.filter(username=user_name).values('id', 'username', 'email', 'is_superuser')[0]

def NotEnrolled(request):
    return render(request,'generalPages/NotEnrolled.html')

def projview(request,pid):
    try:
        user_info = get_user_info(request.user)
        params = {"CurrSiteInfo":GetSiteInfo()}
        params['userInfo'] = user_info
        project1 = Projects1.objects.get(projectid = pid)
        project_by_user = get_project_by_user(project1,request.user)
        if project_by_user is None:
            if not user_info['is_superuser']:
                return HttpResponseRedirect("/project/notenrolled")
        project = Projects1.objects.get(projectid = pid)
        fileup = Content.objects.filter(projasso = pid).values()
        params['project'] = project
        params['filesup'] = fileup
        return render(request,'Projects1/projview.html',params)
    except :
        return render(request,'ErrorPages\Error504.html',params)


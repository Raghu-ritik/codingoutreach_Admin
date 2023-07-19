from unicodedata import category
from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from django.views import generic
# from django.urls import reverse_lazy
from .models import Projects1,Pelcon,Content
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

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

def Home1(request):
    try:
        allprojects = []
        project = Projects1.objects.values('category','projectid')
        proj = []
        cate = {pj['category'] for pj in project}
        cate = list(cate)
        dio = {key : 0 for key in cate}
        for produ in project:
            dio[produ['category']] += 1
        print(dio)
        for pro in dio.keys():
            ppjj = Projects1.objects.filter(category = pro)
            n = dio[pro]
            nslides = n//3 + ceil((n/3)-(n//3))
            allprojects.append([ppjj,range(1,n), nslides])
        #     print("ppjj :: ", ppjj)
        #     print("nslides :: ",nslides)
        #     print("n",n)

        # print("Project :: ",project)
        # print("proj :: ",proj)
        # print("allprojects :: ",allprojects)
        
        return render(request,'Projects1/index.html',{'project':allprojects})
    except:
        return HttpResponse("There is some error at server please try again later !")

def projview(request,pid):
    try:
        ppjj = Projects1.objects.filter(projectid = pid).values()
        fileup = Content.objects.filter(projasso = pid).values()
        ppjj = ppjj[0]

        # print(fileup)
        return render(request,'Projects1/projview.html',{'project':ppjj,'filesup':fileup})
    except:
        return HttpResponse("There is some error at server please try again later !")

# class pelconView(generic.ListView):
#     model = Pelcon
#     template_name = 'Projects1/Pelcon.html'
#     context_object_name = 'files'
#     paginate_by = 2

#     def get_queryset(self):
#         return Pelcon.objects.order_by('id') 


# class FileView(generic.ListView):
#     model = Content
#     template_name = 'Projects1/Pelcon.html'
#     context_object_name = 'files'
#     paginate_by = 2

#     def get_queryset(self):

#         return Pelcon.objects.order_by('id')

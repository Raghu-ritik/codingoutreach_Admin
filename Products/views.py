from unicodedata import category
from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from django.views import generic
# from django.urls import reverse_lazy
from .models import Products,Content,ProductsEnrolledUser
from django.conf import settings
from django.contrib.auth.models import User
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

            Projec = Products(
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

def ProductIndex(request):
    # try:
        allproducts = []
        products = Products.objects.values('categoryF','productid')
        proj = []
        cate = {pj['categoryF'] for pj in products}
        cate = list(cate)
        dio = {key : 0 for key in cate}
        for produ in products:
            dio[produ['categoryF']] += 1
        for pro in dio.keys():
            ppjj = Products.objects.filter(categoryF = pro)
            n = dio[pro]
            nslides = n//3 + ceil((n/3)-(n//3))
            allproducts.append([ppjj,range(1,n), nslides])
            
        if len(allproducts):
            return render(request,'Products/index.html',{'Projects':allproducts})
        return render(request,'generalPages/commingSoonPage.html')
    # except:
    #     return HttpResponse("There is some error at server please try again later !")

def get_project_by_user(product,user):
    try:
        return ProductsEnrolledUser.objects.get(profileId=user,productid=product)
    except :
        return None

def Productview(request,pid):
    try:
        productObj = Products.objects.get(productid = pid)
        product_by_user = get_project_by_user(productObj,request.user)
        if product_by_user is None:
            return render(request,'generalPages/NotEnrolled.html')

        ppjj = Products.objects.filter(productid = pid).values()
        fileup = Content.objects.filter(projasso = pid).values()
        ppjj = ppjj[0]

        # print(fileup)
        return render(request,'Products/productview.html',{'project':ppjj,'filesup':fileup})
    except:
        return HttpResponse("There is some error at server please try again later !")

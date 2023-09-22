from django.shortcuts import render

# Create your views here.
from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from .models import notes1,notesfile
from django.conf import settings
from django.contrib import messages
from math import ceil

def Home2(request):
    # project = Projects1.objects.all()
    allnss = []
    allnotes = notes1.objects.values('category','notesid')
    proj = []
    cate = {pj['category'] for pj in allnotes}
    cate = list(cate)
    dio = {key : 0 for key in cate}
    for produ in allnotes:
        dio[produ['category']] += 1
    print(dio)
    for pro in dio.keys():
        ppjj = notes1.objects.filter(category = pro)
        n = dio[pro]
        nslides = n//3 + ceil((n/3)-(n//3))
        allnss.append([ppjj,range(1,n), nslides])
    #     print("ppjj :: ", ppjj)
    #     print("nslides :: ",nslides)
    #     print("n",n)

    # print("Project :: ",allnotes)
    # print("proj :: ",proj)
    if len(allnss):
        return render(request,'Study/Home2.html',{'allnos':allnss} )
    return render(request,'generalPages/commingSoonPage.html')

def notesview(request,nkid):
    ppjj = notes1.objects.filter(notesid = nkid).values()
    fileup = notesfile.objects.filter(Nfileif = nkid).values()
    ppjj = ppjj[0]

    # print(fileup)
    return render(request,'Study/notesview.html',{'notes':ppjj,'filesup':fileup})
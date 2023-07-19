from django.shortcuts import render

# Create your views here.
from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from .models import LearnMODEL,notesfile
from django.conf import settings
from django.contrib import messages
from math import ceil

def Home2(request):
    # project = Projects1.objects.all()
    allnss = []
    allnotes = LearnMODEL.objects.values('SubLearnHeading','LearnTitle')
    proj = []
    cate = {pj['SubLearnHeading'] for pj in allnotes}
    cate = list(cate)
    dio = {key : 0 for key in cate}
    for produ in allnotes:
        dio[produ['SubLearnHeading']] += 1
    print(dio)
    for pro in dio.keys():
        ppjj = LearnMODEL.objects.filter(SubLearnHeading = pro)
        n = dio[pro]
        nslides = n//3 + ceil((n/3)-(n//3))
        allnss.append([ppjj,range(1,n), nslides])
    return render(request,'LearnWithUS/Home2.html',{'allnos':allnss} )

def notesview(request,nkid):
    ppjj = LearnMODEL.objects.filter(LearnModelid = nkid).values()
    fileup = notesfile.objects.filter(Nfileif = nkid).values()
    ppjj = ppjj[0]

    print(fileup)
    return render(request,'LearnWithUS/notesview.html',{'notes':ppjj,'filesup':fileup})
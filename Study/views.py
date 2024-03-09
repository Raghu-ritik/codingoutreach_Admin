from django.shortcuts import render

# Create your views here.
from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from .models import notes1,notesfile
from Home.models import SiteSettings
from django.conf import settings
from django.contrib import messages
from math import ceil

def GetSiteInfo(SiteId=1):
    return SiteSettings.objects.filter(id=SiteId).values()[0]

def Home2(request):
    params = {"CurrSiteInfo":GetSiteInfo()}
    allNotes = []
    allnotes = notes1.objects.values('category','notesid')
 
    cate = {pj['category'] for pj in allnotes}
    cate = list(cate)
    dio = {key : 0 for key in cate}
    for produ in allnotes:
        dio[produ['category']] += 1
    for pro in dio.keys():
        ppjj = notes1.objects.filter(category = pro)
        n = dio[pro]
        nslides = n//3 + ceil((n/3)-(n//3))
        allNotes.append([ppjj,range(1,n), nslides])

    if len(allNotes):
        params['allnos'] = allNotes
        return render(request,'Study/Home2.html',params )
    return render(request,'generalPages/commingSoonPage.html',params)

def notesview(request,nkid):
    params = {"CurrSiteInfo":GetSiteInfo()}
    Notes = notes1.objects.filter(notesid = nkid).values()
    fileup = notesfile.objects.filter(Nfileif = nkid).values()
    Notes = Notes[0]
    params['notes'] = Notes
    params['filesup'] = fileup
    return render(request,'Study/notesview.html',params)
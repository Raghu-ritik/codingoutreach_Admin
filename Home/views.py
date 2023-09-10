from django.core.exceptions import NON_FIELD_ERRORS
from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .forms import Contactusfrom
from django.contrib.auth.models import User
from Projects1.models import Projects1
from Products.models import Products

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import Group
from django.db import IntegrityError
from .models import Student_B,SocialLinks,ProjectsEnrolled
from django.contrib import messages
from random import randint
import re,math

from NB import settings
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.core.mail import send_mail
# from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text, force_text
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.template.loader import render_to_string

def Home(request):


    lastProjectID,lastProductID = 0,0
    allproducts = []
    allprojects = []
    products = Products.objects.values('productid')
    n = len(products)
    subList = []
    count = 0
    for index, productId in enumerate(products):
        ppjj = Products.objects.filter(productid = productId['productid']).values()
        subList.append(ppjj[0])
        if (index+1)%3 ==0 :
            allproducts.append({count:subList})
            subList = []
            count += 1
        elif index == 4 or index == len(products)-1:
            lastProductID = ppjj[0]['productid']
            allproducts.append({count:subList})
            subList = []
            count += 1
            break
    projects = Projects1.objects.values('projectid')
    subList = []
    count = 0
    for index, projectId in enumerate(projects):
        ppjj = Projects1.objects.filter(projectid = projectId['projectid']).values()
        subList.append(ppjj[0])
        if (index+1)%3 ==0 :# or index == len(projects)-1:
            allprojects.append({count:subList})
            subList = []
            count += 1
        elif index==4 or index == len(projects)-1:
            lastProjectID = ppjj[0]['projectid']
            allprojects.append({count:subList})
            subList = []
            count += 1
            break
    return render(request,'Home/index.html',{"allproducts":allproducts,"allprojects":allprojects,"lastProjectID":lastProjectID,'lastProductID':lastProductID})

def valiemail(emailva):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.fullmatch(regex, emailva)

def login(request):
    try:
        if request.method=="POST" and "loginform":
            loginusername=request.POST['usrname']
            loginpassword=request.POST['passwd']
            try:
                if valiemail(loginusername):
                    email1 = User.objects.filter(email=loginusername)
                    user=authenticate(username= email1[0], password= loginpassword)
                else:
                    user=authenticate(username= loginusername, password= loginpassword)
                if user is not None:
                    auth_login(request, user)
                    messages.success(request, "Successfully Logged In")
                    return redirect("/")
                else:
                    messages.error(request, "Invalid credentials! Please try again")
                    return redirect("/login")
            except IndexError:
                messages.error(request, "Invalid credentials! Please try again")
                return redirect("/login") 
        return render(request,'Home/login.html',{})
    except:
        return HttpResponse("There is some error at server please try again later !")

def Logout(request):
    try:
        logout(request)
        messages.success(request, "Sucessfully logged out ")
        return redirect('/')
    except:
        return HttpResponse("There is some error at server please try again later !")


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def register(request):
        if request.method == 'POST' and "Student_B" :
            email=request.POST.get('email')
            passwd1=request.POST.get('passwd1')
            passwd2=request.POST.get('passwd2')
            fomtype = "Student"
            # Medium=request.POST.get('Medium')
            # github=request.POST.get('github')
            # linkedin=request.POST.get('linkedin')

            # fname=request.POST.get('Fname')
            # lname=request.POST.get('Lname')
            # mobno=request.POST.get('mobno')
            # print(Medium,github,linkedin)
            # print(fname,lname,mobno)
            # print(email,passwd1,passwd2)

            if len(email) > 200:
                messages.error(request, " Your user name must be under 200 characters")
                return redirect('/register')

            if (passwd1!= passwd2):
                messages.error(request, " Passwords do not match")
                return redirect('/register')
            username = 'U'+ email[:3]+str(random_with_N_digits((len(email)%5)+1))

            print(fomtype)
            if fomtype == "Student":
                # Create the user
                user_email=email
                try:
                    existing_user = User.objects.get(email = user_email)
                    if(existing_user.is_active == False ):
                        existing_user.delete()
                    else:
                        messages.error(request, " Username/Email Already Exists")
                        return redirect('/register')                      
                except:
                    pass            
                try:
                    myuser = User.objects.create_user(username, email, passwd1)
                    myuser.is_active = False
                    myuser.save()
                    group = Group.objects.get(name=fomtype)
                    myuser.groups.add(group)
                    Student_B.objects.create(User=myuser,Susername=username,name="",email=myuser.email,password=myuser.password,usertype=fomtype)
                except :
                    messages.error(request, " Username/Email Already Exists")
                    return redirect('/register')                      
                    #############Check for again email ################

            userem = User.objects.get(email=user_email)
            userem.is_active = False
            userem.save()
            current_site = get_current_site(request) ## www.wondershop.in:8000
            mail_sibject = 'Active your account.'
            message = render_to_string('MailValidation/acc_active_email.html',{
                    'user':userem,
                    'domain':current_site.domain,
                    'uid':urlsafe_base64_encode(force_bytes(userem.pk)),
                    'token':account_activation_token.make_token(userem),
            })
            to_mail = user_email
            try:
                send_mail(
                        subject = mail_sibject,
                        message = message,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list= [to_mail],
                        fail_silently=False,    # if it fails due to some error or email id then it get silenced without affecting others
                    )
                messages.success(request, "link has been sent to your email id. please check your inbox and if its not there check your spam as well.")
            except:
                messages.error(request, "Error Occured In Sending Mail, Try Again")
        return render(request,'Home/registeration.html',{} )

def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist)as e:
        user = None
        print(e)
    if user is not None and account_activation_token.check_token(user,token):
        user.is_active=True
        user.save()
        messages.success(request, "Successfully Logged In")
        auth_login(request, user)
        return redirect('/')

    else:
        return HttpResponse('Activation link is invalid or your account is already verified ! Try to Login')
    


def contactus(request):
    try:
        if request.method == "POST":
            name = request.POST.get('Fulname')
            email = request.POST.get('emailadd')
            contactno = request.POST.get('contctno')
            descrip = request.POST.get('descrip')
            print(name,email,contactno,descrip)
        return render(request,'Home/contactus.html',{} )
    except:
        return HttpResponse("There is some error at server please try again later !")

def contactus2(request):
    if request.method == 'POST':
        form = Contactusfrom(request.POST)
        query = form
        if form.is_valid(): #clean data 
            if len(form.cleaned_data.get('query'))>10:
                form.add_error('query' ,"Query length is not right ")
            print(form.cleaned_data.get('email'))
            form.save() 
            return HttpResponse("Form is submitted ☺")
            
        else:
            if len(form.cleaned_data.get('query'))>10:
                form.add_error('query' ,"Query length is not right ")
                form.errors['query'] = 'query lenght is not right .It shoud be more than 10 digits'
            return render(request,'Home/contactus2.html',{'form':form})
    return render(request,'Home/contactus2.html',{'form':Contactusfrom})



def aboutus(request):
    return render(request,'Home/aboutus.html',{} )


def Userpage(request,usrname):
        profile = Student_B.objects.filter(Susername=usrname)
        loginuser1 = User.objects.get(username = usrname)
        courlled,refrealproj,messagepro = 0,0,0

        # fileup = Content.objects.filter(projasso = pid).values()
        # fileup = Content.objects.filter(projasso = pid).values()
      
        # print(couenrl[0])
        courseenrol = []
        try:
            couenrl =  ProjectsEnrolled.objects.filter(profileId=loginuser1).values()
            ccc = ProjectsEnrolled.objects.get(CEid=3)
            allenrol = ccc.courseid.all().values()
            
            for i in range(0,len(allenrol)):
                courseenr = allenrol[i]
                courseenrol.append(courseenr)
        # print(courseenrol)
                courlled = len(allenrol)
        except:
            print("Not enrolled in any course ! ")

        if request.method == 'POST' and 'update_image':
            mobno = profile.mobno
            if len(request.FILES) != 0:
                profile.profile_pic = request.FILES['profilepic']
            profile.mobno = mobno
            profile.save()
            messages.success(request,"Your profile Image had been updated sucessfully ")

        if request.method == 'POST' and 'phone_number':
            profile.mobno = request.POST.get("phonenumber")
            profile.save()
            messages.success(request,"Your phone number had been updated sucessfully ")

        print(courlled)
        return render(request,'Home/userview.html',{'profile':profile,"courenorl":courseenrol,'courlled':courlled,'refrealproj':refrealproj,'messagepro':messagepro})


def adminpage(request):

    return render(request,'Home/Admintemp/admin_page.html',{})

def projin(request):

        allprojects = []
        project = Projects1.objects.values('category','projectid')
        proj = []
        cate = {pj['category'] for pj in project}
        cate = list(cate)
        dio = {key : 0 for key in cate}
        for produ in project:
            dio[produ['category']] += 1
        # print(dio)
        for pro in dio.keys():
            ppjj = Projects1.objects.filter(category = pro)
            n = dio[pro]
            nslides = n//3 + math.ceil((n/3)-(n//3))
            allprojects.append([ppjj,range(1,n), nslides])
        # print(allprojects)
        for ij,lk,il in allprojects:
            print(ij)
            print(ij,lk,il)
            # print(ij.projectname)
            for ik in ij:
                print(ik.projectname)
            #     print(ik.category)
            #     print(ik.creator)
        return render(request,'Home/Admintemp/material.html',{"project":allprojects})


def search(request):
    query=request.GET['query']
    if len(query)>78:
        allprojalop=Projects1.objects.none()
    else:
        allprojTitle= Projects1.objects.filter(projectname=query)
        allprojcreat= Projects1.objects.filter(creator=query)
        allprojCategory =Projects1.objects.filter(category=query)
        allprojesc = Projects1.objects.filter(desc=query)
        allprojalop=  allprojTitle.union( allprojcreat,allprojCategory, allprojesc)
    if allprojalop.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'project': allprojalop, 'query': query}
    return render(request, 'Projects1\search.html', params)

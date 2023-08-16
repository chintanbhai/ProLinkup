from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password,check_password
from .forms import UserProfileForm

# Create your views here.

def home(request):
    
    all_data = job.objects.all()
    length = len(all_data)
    return render(request,'application/index.html',{'length': length,'key1':all_data})

@login_required(login_url='login')
def job1(request):
    all_data = job.objects.all()
    # print(all_data)
    return render(request,'application/job.html',{'key1':all_data})

@login_required(login_url='login')
def empDetails(request):
    return render(request,'application/employers-details.html')

@login_required(login_url='login')
def candidate1(request):
    prof = profile.objects.all()
    # user = User.objects.all()

    # matched_data = []
    # for user in user:
    #     for prof in profile:
    #         if user.id == prof.id :
    #             matched_data.append((user,prof))
                 
    return render(request,'application/candidate.html',{'key1':prof})

@login_required(login_url='login')
def candidateDetails(request,pk):
    candidate_profile = profile.objects.get(id=pk)
    # candidate_profile2 = 
    return render(request,'application/candidate-details.html',{'key1':candidate_profile})

def blog(request):
    return render(request,'application/blog.html')

def blogDetails(request):
    return render(request,'application/blog-details.html')

def registration(request):
    if request.method == "POST" :
        user = request.POST['user']
        mail = request.POST['email']
        password1 = request.POST['password']
        cpassword = request.POST['c_password']
        
        if ' ' in user:
            message = 'Username cannot contain spaces.'
            return render(request, 'application/registration.html', {'msg': message})
        
        if User.objects.filter(username=user).exists():
            message = 'An account with this username already exists.'
            return render(request, 'application/registration.html', {'msg': message})

        if User.objects.filter(email=mail).exists():
            message = 'An account with this email already exists.'
            return render(request, 'application/registration.html', {'msg': message})

        if len(password1)<8 :
            message = 'Please Enter 8 digit Password'
            return render(request,'application/registration.html',{'msg':message})
        
        if password1!=cpassword :
            message = 'Please Enter Same Password'
            return render(request,'application/registration.html',{'msg':message})
        
        my_user = User.objects.create_user(user ,mail , password1)
        my_user.save()
        return render(request,'application/login.html',{'msg':"Successfully Registration"})
    
    return render(request,'application/registration.html')

# def Dataregister(request):
    # if request.method == "POST" :
    #     user = request.POST['username']
    #     mail = request.POST['email']
    #     password1 = request.POST['password']
    #     cpassword = request.POST['c_password']
        
    #     if ' ' in user:
    #         message = 'Username cannot contain spaces.'
    #         return render(request, 'application/registration.html', {'msg': message})
        
    #     if User.objects.filter(username=user).exists():
    #         message = 'An account with this username already exists.'
    #         return render(request, 'application/registration.html', {'msg': message})

    #     if User.objects.filter(email=mail).exists():
    #         message = 'An account with this email already exists.'
    #         return render(request, 'application/registration.html', {'msg': message})

    #     if len(password1)<8 :
    #         message = 'Please Enter bigger Password'
    #         return render(request,'application/registration.html',{'msg':message})
        
    #     if password1!=cpassword :
    #         message = 'Please Enter Same Password'
    #         return render(request,'application/registration.html',{'msg':message})
        
    #     my_user = User.objects.create_user(user ,mail , password1)
    #     my_user.save()
    #     return render(request,'application/login.html')
        

def login1(request):
    return render(request,'application/login.html')

def Datalogin(request):
    if request.method == "POST" :
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('profilepage')
        else:
            message = 'Invalid Username or Password'
            return render(request,'application/login.html',{'msg':message})
        

def logout123(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def aboutUs(request):
    return render(request,'application/about-us.html')

@login_required(login_url='login')
def contact1(request):
    return render(request,'application/contact.html')

def Addcontact(request):
    success_message = None  # Initialize success_message outside of the if block

    if request.method == 'POST':
        name = request.POST['con_name']
        email = request.POST['con_email']
        subject = request.POST['subject']
        message = request.POST['con_message']
        
        add = contact.objects.create(name=name, email=email, subject=subject, message=message)
        success_message = "Message sent successfully!"  # Create a success message

    return render(request, 'application/contact.html', {'success_message': success_message})


@login_required(login_url='login')
def ShowCompany(request ,pk):
    
    all = job.objects.get(id = pk)
    # print(all)
    return render(request,'application/job-details.html',{'key1':all})
    

def saveprofile(request,pk,user):
    
        company = job.objects.get(id=pk)
        user = User.objects.get(id=user)
        
        new_profile = applyjobs.objects.create(emp_id=user, jobs=company.company_name)
        return redirect('job')

@login_required(login_url='login')
def profilepage(request):
    user_profile, created = profile.objects.get_or_create(user=request.user)
    jobs = applyjobs.objects.filter(emp_id=user_profile.user)
    return render(request, 'application/profilepage1.html', {'user_profile': user_profile, 'jobs': jobs})


@login_required
def edit_profile(request):
    user_profile, created = profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            
            languages = request.POST.getlist('dynamic_language')
            user_profile.language = ','.join(languages)
            form.save()
            return redirect('profilepage')
    else:
        form = UserProfileForm(instance=user_profile)
    
    existing_languages = user_profile.language.split(',') if user_profile.language else []

    return render(request, 'application/editprofile1.html', {'form': form , 'existing_languages': existing_languages})


# -=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#                               For Admin Page 
# -=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def adminSignUp(request):
    if request.method == "POST" :
        username = request.POST['username']
        mail = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        hashpassword = make_password(password)

        if len(password)<8:
            message = "Please Enter Bigger Password"
            return render(request,"admin/signUP.html",{'msg':message})
        
        user = Adminregister.objects.filter(email=mail)
        if user:
            message = "User already exist"
            return render(request,"admin/signUP.html",{'msg':message})
        else:
            if password == cpassword:
                new = Adminregister.objects.create(username=username , email=mail , password=hashpassword)
                message = "User registration Successfully"
                return render(request,"admin/signIn.html")
            else:
                message = "Password Does Not Same"
                return render(request,"admin/signUP.html",{'msg':message})
    return render(request,'admin/signUP.html')

def adminSignIn(request):
    return render(request,'admin/signIn.html')

def DataadminSignIn(request):
    # if request.method == "post":
        mail = request.POST['email']
        password = request.POST['password']

        # print(mail)
        data = Adminregister.objects.filter(email=mail)
        if not data:
            message = "please first register Your Account"
            return render(request,"admin/signIn.html",{'msg':message})

        user = Adminregister.objects.get(email = mail)

        if user:
            if check_password(password , user.password):
                # request.session['email'] = user.email
                return redirect('Adminhome')
                # return render(request,"application/home.html")
            else:
                message = "Invalid password. Please enter valid password"
                return render(request,"admin/signIn.html",{'msg':message})
        else:
            message = "Please first register your account"
            return render(request,"admin/signIn.html",{'msg':message})


def forgot(request):
    return render(request,'admin/forgotPassword.html')

def Adminhome(request):
    return render(request,'admin/home.html')

def Admincompany(request):
    all_data = job.objects.all()
    return render(request,'admin/company.html',{'key1':all_data})

def addcompany(request):
    if request.method == "POST" :
        company_image = request.FILES['image']
        company_name = request.POST['company_name']
        city = request.POST['city']
        email = request.POST['email']
        time = request.POST['time']
        developer = request.POST['developer']
        salary = request.POST['salary']
        languages = request.POST['languages']
        
        add = job.objects.create(company_image = company_image ,email = email , address = city , company_name = company_name,time = time,developer = developer,salary = salary ,languages = languages )
        # add1 = showcompany.objects.create(company_image = company_image ,email = email , address = city , company_name = company_name,time = time,developer = developer,salary = salary ,languages = languages )
        return redirect('Admincompany')

def deletecompany(request,pk):
    data = job.objects.get(id = pk)
    data.delete()
    return redirect('Admincompany')

def editcompany(request,pk):
    data = job.objects.get(id = pk )
    return render(request,'admin/editcompany.html',{'key1':data})

def updatedata(request,pk):
    data = job.objects.get(id = pk)
    data.company_image = request.POST['image']
    data.company_name = request.POST['company_name']
    data.email = request.POST['email']
    data.address = request.POST['city']
    data.time = request.POST['time']
    data.languages = request.POST['languages']
    data.salary = request.POST['salary']
    data.developer = request.POST['developer']
    data.save()
    
    return redirect('Admincompany')


def manageUser(request):
    all = User.objects.all()
    
    return render(request,'admin/manageUser.html')

def Admincontact(request):
    return render(request,'admin/Admincontact.html')
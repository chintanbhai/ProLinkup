from django.contrib import admin
from django.urls import path
from .import views 

urlpatterns = [
    path('',views.home,name='home'),
    path('job/',views.job1,name='job'),
    path('jobDetails/<int:pk>',views.ShowCompany,name='Showcompany'),   #show details
    path('Emplyers-Details',views.empDetails,name='empDetail'),
    path('candidate/',views.candidate1,name='candidate'),
    path('candidateDetails/<int:pk>',views.candidateDetails,name='candidateDetails'),
    path('blog/',views.blog,name='blog'),
    path('blogDetails/',views.blogDetails,name='blogDetails'),
    path('Registration/',views.registration,name='registration'),
    # path('DataRegister/',views.Dataregister,name='Dataregister'),
    path('Login/',views.login1,name='login'),
    path('DataLogin/',views.Datalogin,name='Datalogin'),
    path('logout/',views.logout123,name='logout'),
    path('aboutUs/',views.aboutUs,name='aboutus'),
    path('contact/',views.contact1,name='contact'),
    path('Addcontact/',views.Addcontact,name='addcontact'),
    path('saveprofile/<int:pk>/<int:user>',views.saveprofile,name='saveprofile'),
    path('profilepage/',views.profilepage,name='profilepage'),
    path('editprofilepage/',views.edit_profile,name='editprofilepage'),
    
    # -=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    #                   Admin
    # -=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    
    path('Admin-SignUp/',views.adminSignUp,name='Adminsignup'),
    path('Admin-SignIn/',views.adminSignIn,name='Adminsignin'),
    path('DataAdmin-SignIn/',views.DataadminSignIn,name='DataAdminsignin'),
    path('Admin-Change-password/',views.forgot,name='Adminforgot'),
    path('Admin-home/',views.Adminhome,name='Adminhome'),
    path('Admin-company/',views.Admincompany,name='Admincompany'),
    path('Admin-add-company/',views.addcompany,name="addcompany"),  #Add company
    path('Admin-Delete-company/<int:pk>',views.deletecompany,name="deletecompany"),  #delete company
    path('Admin-Edit-company/<int:pk>',views.editcompany,name="editcompany"),  #edit company
    path('Admin-update-company/<int:pk>',views.updatedata,name="update"),  #update company
    path('Admin-User/',views.manageUser,name='Adminuser'),
    path('Admin-contact',views.Admincontact,name='Admincontact'),
    
]

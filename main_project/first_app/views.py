from django.shortcuts import render,redirect
from . forms import register_form
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == "POST":
        form = register_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user_login")
    else :
        form=register_form()
    return render(request,"./register_page.html",{'form':form})

# user login section 
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass= form.cleaned_data['password']
            user = authenticate(username=user_name,password=user_pass)
            if user is not None:
                login(request,user)
                messages.success(request,"logged in successfully")
                return redirect("profile_page")
           
    else:
        form = AuthenticationForm()
    return render(request,'./login_form.html',{'form':form})

# profile section 
def profile(request):
    return render(request,'./profile_page.html')

# logout section
def user_logout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully")
    return redirect("user_login")

def password_change(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect("profile_page")
    else:
        form = PasswordChangeForm(user = request.user)
    return render(request,"./pass_change.html",{'form':form})
# password change without old password 

def password_change2(request):
    if request.method == "POST":
        form = SetPasswordForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect("profile_page")
    else:
        form = SetPasswordForm(user = request.user)
    return render(request,"./pass_change.html",{'form':form})
    


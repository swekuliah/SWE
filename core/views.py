from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.
# dashboard
def dashboard(request):
    return render(request, "dashboard.html")

# profile page
def profile(request):
    # take current user username and email
    myname = request.user.username
    mymail = request.user.email
    return render(request, "profilepage.html", {"username":myname, "email":mymail})

def register(request):
    # try catch is good for exception
    try:
        if request.method == "POST":
            # this will take the form value
            myemail = request.POST.get("email")
            ## open this for debugging purpose
            # print(myemail)
            myname = request.POST.get("username")
            ## open this for debugging purpose
            # print(myname)
            mypassword = request.POST.get("password")
            ## open this for debugging purpose
            # print(mypassword)

            # condition for user, chech email exist, username exist, pass length < 8
            # email exist
            if User.objects.filter(email=myemail).exists():
                messages.info(request, "Email Already Used")
                return redirect('register')
            # username exist
            elif User.objects.filter(username=myname).exists():
                messages.info(request, "username Already exist")
                return redirect('register')
            # password lacking
            elif len(mypassword)<8:
                messages.info(request, "password must contain at least 8 characters")
                return redirect('register')
            else:
                # create entity and save to database
                users = User.objects.create_user(username=myname, email=myemail, password=mypassword)
                users.save();
                return redirect('http://127.0.0.1:8000/login/')
        else:
            # if forum method !POST 
            print("error, forum method not POST")
    except Exception as e:
        error_message = str(e)  # Convert the exception to a string
        return render(request, "error.html", {'error_message': error_message})
    
    return render(request, "registrations.html")

def login(request):
    try:
        if request.method == "POST":
           # this will take the form value
            myname = request.POST.get("username")
            ## open this for debugging purpose
            # print(myname)
            mypassword = request.POST.get("password")
            ## open this for debugging purpose
            # print(mypassword)

            # authenticate user
            user = auth.authenticate(username=myname, password=mypassword)
            # if user is not authenticated then user = None
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
            else:
                # this will appear ini 
                messages.info(request, "Invalid username or password")
                return redirect("login")
        else:
            # if forum method !POST 
            print("error, forum method not POST")
    except Exception as e:
        error_message = str(e)  # Convert the exception to a string
        return render(request, "error.html", {'error_message': error_message})
    
    return render(request, "login.html")

def edit_profile(request):
    user_id = request.user.id
    try:
        print("hello")
    except Exception as e:
        error_message = str(e)  # Convert the exception to a string
        return render(request, "error.html", {'error_message': error_message})
    
    return render(request, "editprofilepage.html", {"id":user_id})

def logout_user(request):
    logout(request)
    return redirect("register")
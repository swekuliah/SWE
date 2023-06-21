from django.shortcuts import render

# Create your views here.
def show_forum(request):
    return render(request, "forum.html")

def discussion(request):
    myname = request.user.username
    return render(request, "discussion.html", {"username":myname})
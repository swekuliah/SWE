from django.shortcuts import render, redirect, get_object_or_404
from courses.models import notes
from django.contrib import messages
from courses.models import materials


# Create your views here.
def mynote(request):
    return render(request, "mynotes.html")

def upload_notes(request):
    # try catch to handle error
    try:
        # take POST value from forum
        if request.method == "POST":
            text = request.POST.get("titles")
            descript = request.POST.get("description")
            files = request.FILES.get("user_note")
            privacy = request.POST.get("availability", False)=='on'
            # get the author name
            myname = request.user.username
            note = notes(title=text,description=descript,note_file=files, is_private=privacy, author=myname)
            note.save()
            messages.info(request, "successfully created new note")
        else:
            # if forum method !POST 
            print("error, forum method not POST")
    except Exception as e:
        return e
    # give the upload note page
    return render(request, "mynotes.html")

def note_contents(request, note_id):
    note = get_object_or_404(notes, id=note_id)
    return render(request, 'content.html', {'note': note})

# def note_content(request):
#     return render(request, "content.html")

def collection(request):
    collections = notes.objects.all()
    user = request.user
    if len(collections)==0:
        redirect("mynotes")
    return render(request, "collection.html", {"collections":collections, "user":user})

def public_notes(request):
    collections = notes.objects.all()
    if len(collections)==0:
        redirect("mynotes")
    return render(request, "public_note.html", {"collections":collections})

def my_course(request):
    return render(request, "myCourse.html")

def material(request):
    collections = materials.objects.all()
    if len(collections)==0:
        redirect("mycourse")
    return render(request, "materials.html", {"collections":collections})
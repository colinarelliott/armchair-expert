from django.shortcuts import render
from armchair.models import Document
from django.http import HttpResponse
from .forms import UploadFileForm

def chat(request):
    return render(request, 'armchair.html')

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        #form.user = request.user
        #print("form submission from: ", form.user)
        print("form data: ", form.data)
        if form.is_valid():
            print("form is valid.")
            form.save()
            return HttpResponse(("<p style='color:green;'>200 - form is  valid.</p>"))
    else:
        form = UploadFileForm()
    return render(request, "upload.html", {"form": form})

def send(request):
    return render(request, 'armchair.html')

from django.shortcuts import render
from armchair.models import Document
from django.http import HttpResponseRedirect
from .forms import UploadFileForm

def chat(request):
    return render(request, 'armchair.html')

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            print("success.")
            form.save()
            return HttpResponseRedirect("/success/url/")
    else:
        form = UploadFileForm()
    return render(request, "upload.html", {"form": form})

def send(request):
    return render(request, 'armchair.html')

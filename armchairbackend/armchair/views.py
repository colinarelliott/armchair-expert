from django.shortcuts import render
from armchair.models import Document, Chat

def chat(request):
    return render(request, 'armchair.html')

def upload(request):
    # not a page view, just submits the file and puts it in the Documents model, then returns a response
    file = request.FILES['document']
    document = Document(user=request.user, document=file)
    document.save()
    return render(request, 'armchair.html')


def send(request):
    return render(request, 'armchair.html')

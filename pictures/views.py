from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm

#from .models import User



# Create your views here.
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form_is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('index')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form':form})

class PictureView(View):
    
    def get(self,request):
        
        return render(request, 'UserManagementTool/simple_upload.html', {'user':'Hallor',})
        
        
def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
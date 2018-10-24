from django.shortcuts import render
from django.views import View
#<<<<<<< HEAD
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
        
        
#def handle_uploaded_file(f):
#    with open('some/file/name.txt', 'wb+') as destination:
#        for chunk in f.chunks():
#            destination.write(chunk)
#=======
from django.views.generic import TemplateView
from django.template import loader
from django.http import HttpResponse

# Create your views here.

class IndexView(TemplateView):
    template_name = 'pictures/picture_index.html'


    def get(self,request):
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render({}, request))
#>>>>>>> a12aa38c2b414a10edd9c4391940eee2708e4fcc

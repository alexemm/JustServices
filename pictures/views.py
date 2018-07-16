from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.template import loader
from django.http import HttpResponse

# Create your views here.

class IndexView(TemplateView):
    template_name = 'pictures/picture_index.html'


    def get(self,request):
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render({}, request))

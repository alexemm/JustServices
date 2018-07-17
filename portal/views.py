from django.shortcuts import render

from django.views.generic import View
from django.template import loader
from django.http import HttpResponse

# Create your views here.

'''
View to see the Dashboard/ Index page
'''
class IndexView(View):
    template_name = 'portal/index.html'


    def get(self, request):
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render({}, request))

'''
    View to show the About Page
'''

class AboutView(View):
    template_name = 'portal/about.html'

    def get(self, request):
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render({}, request))
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView



class AboutView(TemplateView):
    template_name = 'clydefarm/about.html'


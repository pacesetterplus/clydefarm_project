from django.http.response import HttpResponse
from django.views.generic.base import TemplateView


class ContactView(TemplateView):
    template_name = 'clydefarm/contact.html'


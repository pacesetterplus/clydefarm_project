from django.http.response import HttpResponse
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'clydefarm/index.html'

class AboutView(TemplateView):
    template_name = 'clydefarm/about.html'

    def get(self, request, *args, **kwargs):
        return HttpResponse('result')
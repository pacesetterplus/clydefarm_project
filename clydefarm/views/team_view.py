from django.http.response import HttpResponse
from django.views.generic.base import TemplateView


class TeamView(TemplateView):
    template_name = 'clydefarm/team.html'


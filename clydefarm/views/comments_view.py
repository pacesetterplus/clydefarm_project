from django.http.response import HttpResponse
from django.views.generic.base import TemplateView


class CommentsView(TemplateView):
    template_name = 'clydefarm/comments.html'


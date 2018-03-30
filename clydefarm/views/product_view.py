from django.http.response import HttpResponse
from django.views.generic.base import TemplateView


class ProductView(TemplateView):
    template_name = 'clydefarm/products.html'


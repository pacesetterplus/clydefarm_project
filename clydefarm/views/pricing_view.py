from django.http.response import HttpResponse
from django.views.generic.base import TemplateView


class PricingView(TemplateView):
    template_name = 'clydefarm/pricing.html'


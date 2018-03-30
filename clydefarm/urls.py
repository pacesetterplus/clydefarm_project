from django.conf.urls import url
from clydefarm.views import *
from django.views.generic import TemplateView, CreateView


urlpatterns = [
    url(r'^about/$',about_view.AboutView.as_view(),name='about'),
    url(r'^team/$',team_view.TeamView.as_view(), name='team'),
    url(r'^contact/$', contact_view.ContactView.as_view(), name='contact'),
    url(r'^comments/$', comments_view.CommentsView.as_view(), name='comments'),
    url(r'^products/$',product_view.ProductView.as_view(), name='products'),
    url(r'^pricing/$', pricing_view.PricingView.as_view(), name='pricing'),
]


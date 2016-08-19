from django.conf.urls import url

from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'search$', views.search, name='search'),
    url(r'search\.csv$', views.search, name='search.csv'),
    url(r'search\.json$', views.search, name='search.json'),
    url(r'^grant/(.*)$', views.grant, name='grant'),
    url(r'^grants_datatables$', views.grants_datatables, name='grants_datatables'),
    url(r'^funder/(.*)$', views.funder, name='funder'),
    url(r'^funder/(.*)\.csv$', views.funder, name='funder.csv'),
    url(r'^funder/(.*)\.json$', views.funder, name='funder.json'),
    url(r'^funder_recipients_datatables$', views.funder_recipients_datatables, name='funder_recipients_datatables'),
    url(r'^funder_recipients_datatables.csv$', views.funder_recipients_datatables, name='funder_recipients_datatables.csv'),
    url(r'^funder_recipients_datatables.json$', views.funder_recipients_datatables, name='funder_recipients_datatables.json'),
    url(r'^funders_datatables$', views.funders_datatables, name='funders_datatables'),
    url(r'^funders_datatables.csv$', views.funders_datatables, name='funders_datatables.csv'),
    url(r'^funders_datatables.json$', views.funders_datatables, name='funders_datatables.json'),
    url(r'^recipients', views.recipients, name='recipients'),
    url(r'^funders', views.funders, name='funders'),
    url(r'^recipient/(.*)$', views.recipient, name='recipient'),
    url(r'^recipient/(.*)\.csv$', views.recipient, name='recipient.csv'),
    url(r'^recipient/(.*)\.json$', views.recipient, name='recipient.json'),
    url(r'^region/(.*)$', views.region, name='region'),
    url(r'^region/(.*)\.csv$', views.region, name='region.csv'),
    url(r'^region/(.*)\.json$', views.region, name='region.json'),
    url(r'^district/(.*)$', views.district, name='district'),
    url(r'^district/(.*)\.csv$', views.district, name='district.csv'),
    url(r'^district/(.*)\.json$', views.district, name='district.json'),
    url(r'^publisher/(.*)$', views.publisher, name='publisher'),
    url(r'^datasets/$', views.datasets, name='datasets'),
    url(r'^stats', views.stats, name='stats'),
    url(r'^take_down_policy', TemplateView.as_view(template_name='take_down_policy.html'), name='take_down_policy'),
    url(r'^terms', TemplateView.as_view(template_name='terms.html'), name='terms'),
    url(r'^help', TemplateView.as_view(template_name='help.html'), name='help'),
]

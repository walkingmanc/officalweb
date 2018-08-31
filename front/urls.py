from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^(?P<id>[0-9]+)/$', views.index, name='index'),
    url(r'^show/$', views.show, name='show'),
    url(r'^show/service-info-(?P<serviceId>[0-9]+)$', views.serviceDetail, name='serviceDetail'),
    url(r'^show/case-list-(?P<cata>[0-9]+)-(?P<pageIndex>[0-9]+)$', views.caseList, name='caseList'),
    #url(r'^show/case-list-cata-(?P<cata>[0-9]+)$', views.caseList, name='caseList'),
    url(r'^show/service-list$', views.serviceList, name='serviceList'),
    url(r'^show/product-list-(?P<pageIndex>[0-9]+)$', views.productList, name='productList'),
    url(r'^show/about$', views.about, name='about'),
    url(r'^show/contact$', views.contact, name='contact'),
    url(r'^show/case-info-(?P<caseId>[0-9]+)-(?P<curCata>[0-9]+)-(?P<curPage>[0-9]+)$', views.caseDetail, name='caseDetail'),
    url(r'^show/product-info-(?P<productId>[0-9]+)$',views.productDetail,name='productDetail'),
    url(r'^show/guest/collect$', views.guestCollect, name='guestCollect'),

]
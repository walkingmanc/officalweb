from django.shortcuts import render

import json

# Create your views here.


from django.http import HttpResponse


def index(request, id):
    return HttpResponse("Hello, world. You're at the mainpage index,参数值:%s." % id)


def show(request):
    from .models import CaseShow
    from .models import ServiceShow
    case_list = CaseShow.objects.all()
    service_list = ServiceShow.objects.all()
    context = {'case_list': case_list,
               'service_list': service_list}
    return render(request, 'mainpage/show.html', context)


def productDetail(request, productId):
    from .models import ProductShow
    productDetail = ProductShow.objects.get(pk=productId)
    # caseshowDetailMulti=caseDetail.caseshowdetailmulti_set.all().order_by('order')
    context = {'productDetail': productDetail}
    return render(request, 'mainpage/productDetail.html', context)


def caseDetail(request, caseId,curCata,curPage):
    from .models import CaseShow
    caseDetail = CaseShow.objects.get(pk=caseId)
    caseshowDetailMulti = caseDetail.caseshowdetailmulti_set.all().order_by('order')
    context = {'caseDetail': caseDetail, 'caseshowDetailMulti': caseshowDetailMulti,'curCata':curCata,'curPage':curPage}
    return render(request, 'mainpage/caseDetail.html', context)


def caseList(request, cata, pageIndex):
    from .models import CaseCat
    from .models import CaseShow
    from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

    #0-表示所有类别

    caseCatList = CaseCat.objects.order_by('order')

    if 0==int(cata):
         case_list_all=CaseShow.objects.all()
    else:
         case_list_all = CaseShow.objects.filter(caseCat=cata)

    paginator = Paginator(case_list_all, 6, 1)

    try:
        case_list_page = paginator.page(pageIndex)
    except PageNotAnInteger:
        case_list_page = paginator.page(1)
    except EmptyPage:
        case_list_page = paginator.page(paginator.num_pages)

    context = {'case_list_page': case_list_page, 'caseCatList': caseCatList,'curCata':cata, 'curPage':pageIndex}

    return render(request, 'mainpage/caseList.html', context)


def serviceDetail(request, serviceId):
    return render(request, 'mainpage/serviceDetail' + serviceId + '.html')


def about(request):
    return render(request, 'mainpage/about.html')


def contact(request):
    return render(request, 'mainpage/contact.html')


def serviceList(request):
    from .models import ServiceShow
    service_list = ServiceShow.objects.all()
    context = {'service_list': service_list}
    return render(request, 'mainpage/serviceList.html', context)


def productList(request, pageIndex):
    from .models import ProductShow
    from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
    product_list_all = ProductShow.objects.all()
    paginator = Paginator(product_list_all, 4)

    try:
        product_list_page = paginator.page(pageIndex)
    except PageNotAnInteger:
        product_list_page = paginator.page(1)
    except EmptyPage:
        product_list_page = paginator.page(paginator.num_pages)

    context = {'product_list_page': product_list_page, }

    return render(request, 'mainpage/productList.html', context)


def guestCollect(request):  # 收集客户需求信息
    from .models import GuestCollect
    ctx = {'rlt': 10000}
    if request.POST:
        ctx['name'] = request.POST['name']
        ctx['tel'] = request.POST['tel']
        ctx['txt'] = request.POST['txt']
    else:
        ctx['name'] = request.POST['name']
        ctx['tel'] = request.POST['tel']
        ctx['txt'] = request.POST['txt']

    try:
        GuestCollect.objects.create(guestName=ctx['name'], guestTel=ctx['tel'], guestRequire=ctx['txt']);
    except Exception as e:
        resp = {'code': 101, 'detail': 'Eorr'}

    resp = {'code': 100, 'detail': 'Success'}

    return HttpResponse(json.dumps(resp), content_type="application/json;charset=utf-8")


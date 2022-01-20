from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Enjoyer, PreRegister
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.core.paginator import Paginator


def About(request):
    return render(request, 'users/About.html')
def StillInProcess(request):
    return render(request, 'users/stillinprocess.html')
def WaitingArea(request):
    return render(request, 'users/Processing.html')
def terms(request):
    return render(request, 'users/terms_conditions.html')
def infos(request):
    VC_info = Enjoyer.objects.all().order_by('-id')
    paginator = Paginator(VC_info,5)
    page_number = request.GET.get('page')
    VC_info = paginator.get_page(page_number)
    return render(request, 'users/info_table.html', {'pages':VC_info})
def search(request):
    if request.method =='GET':
        searched = request.GET.get('SearchId')
        if searched:
            VC_info= Enjoyer.objects.filter(Q(Idnumber__icontains=searched )|
                                            Q(Fname__icontains=searched)).order_by('-id')
            paginator = Paginator(VC_info,5)
            page_number = request.GET.get('page')
            VC_info = paginator.get_page(page_number)
            return render(request, 'users/info_table.html', {'pages':VC_info})
        else:
            print('no info found...')
            return render(request, 'users/info_table.html', {})
def index(request):
    return render(request, 'base.html')
def Register(request):
    return render(request,'users/Register.html')
def processRegister(request):
    idnumber=request.POST.get('id number')
    lastname = request.POST.get('last name')
    firstname = request.POST.get('first name')
    middleinitial = request.POST.get('middle initial')
    address = request.POST.get('address')
    contactnumber = request.POST.get('contact number')
    dateofbirth = request.POST.get('birthday')
    vmfd = request.POST.get('first dose')
    vmsd = request.POST.get('second dose')
    dfd= request.POST.get('dfd')
    dsd = request.POST.get('dsd')
    vc_image = request.FILES.get('Vcpic')
    email = request.POST.get('email')
    terms = request.POST.get('terms')

    try:
        n=PreRegister.objects.get(user_Idnumber=idnumber)
        return HttpResponseRedirect('StillInProcess')
    except ObjectDoesNotExist:
        new_user = PreRegister.objects.create(user_Idnumber=idnumber,user_Lname=lastname,user_Fname=firstname,user_MI=middleinitial,user_Address=address\
                                       ,user_contactnumber=contactnumber,user_dateofbirth=dateofbirth,user_VMfirstdose=vmfd,user_VMseconddose=vmsd\
                                       ,user_Sfirstdose=dfd,user_Sseconddose=dsd,VCphoto=vc_image,user_Email=email)
        new_user.save()
        return HttpResponseRedirect('WaitingArea')
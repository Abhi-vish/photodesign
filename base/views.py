from django.shortcuts import render
import sys,os
import time
import tempfile
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from base.models import HowWeWork,WhyToChooseUs,OurServices,AboutUs,ContactUs,Service,FreeTrial,PricingData,OrderNow
from django.core.mail import send_mail
# Create your views here.


def base(request):
    serData = Service.objects.all()
    data5 = {
        'serData':serData
    }
    return render(request,'base.html',data5)
def home(request):
    howdata = HowWeWork.objects.all()
    serData = Service.objects.all()
    choosedata = WhyToChooseUs.objects.all()
    servicedata = OurServices.objects.all()
    data1 = {
        'howdata':howdata,
        'choosedata':choosedata,
        'servicedata':servicedata,
        'serData':serData
    }

    return render(request,'home.html',data1)

def gallery(request):
    return render(request, 'gallery.html')

def about(request):
    aboutdata = AboutUs.objects.all()
    serData = Service.objects.all()
    data2 = {
        'aboutdata':aboutdata,
        'serData':serData
    }
    return render(request,'about.html',data2)

def contact(request):
    serData = Service.objects.all()
    data5 = {
        'serData':serData
    }
    if request.method == 'POST':
        name1 = request.POST.get('name')
        email1 = request.POST.get('email')
        phone1 = request.POST.get('phone')
        country1 = request.POST.get('country')
        findus1 = request.POST.get('findus')
        comment1 = request.POST.get('comment')

        instance = ContactUs(name = name1, email = email1,phone=phone1,country=country1,findus = findus1,comment=comment1)
        instance.save()

    return render(request,'contact.html',data5)

def howework(request):
    howdata = HowWeWork.objects.all()
    servicedata = OurServices.objects.all()
    serData = Service.objects.all()
    data1 = {
        'howdata':howdata,
        'servicedata':servicedata,
        'serData':serData
    }
    return render(request,'HowWeWork.html',data1)


def footer(request):
    return render(request,'footer.html')

def ServicePro(request,id):
    serData = [Service.objects.get(id = id)]
    data2 = {
        'serData':serData
    }
    return render(request,'our_services.html',data2)


def serviceTemp(request,id):
    servicedata = OurServices.objects.all()
    serData = [Service.objects.get(id=id)]
    data1 = {
        'servicedata':servicedata,
        'serData':serData
        
    }
    return render(request,'service_template.html',data1)

def freeTrial(request):
    if request.method == 'POST' and request.FILES: 
        name = request.POST.get('name1')
        email = request.POST.get('email1')
        service = request.POST.get('service1')
        image = request.FILES.get('image1')
        img_path = os.path.join(settings.MEDIA_ROOT,'Trial_image',image.name)
        with open(img_path,'wb') as file:
            for chunk in image.chunks():
                file.write(chunk)
        comment = request.POST.get('comment1')

        freeTrialInstance = FreeTrial(name=name,email=email,service=service,image=image,comment= comment)
        freeTrialInstance.save()

        email_subject = service
        email_body = "{} \n{}".format(service,comment)
        recipient_email = ["mangaverse1002@gmail.com"]
        email = EmailMessage(
            subject=email_subject,
            body=email_body,
            from_email=email,
            to=recipient_email
        )
        
        email.attach_file(img_path)
        email.send(fail_silently=False)

    return render(request,'freetrial.html')

def pricing(request):
    pricingData = PricingData.objects.all()
    serData = Service.objects.all()

    data3 = {
        'pricingData':pricingData,
        'serData':serData
    }

    return render(request,'pricing.html',data3)


def ordernow(request):
    pricingdata = PricingData.objects.all()
    serData = Service.objects.all()
    data3 = {
        'pricingdata':pricingdata,
        'serData':serData
    }
    if request.method == 'POST' and request.FILES:
        service = request.POST.get('service2')
        image = request.FILES.get('image2')
        img_path = os.path.join(settings.MEDIA_ROOT,'Order_img',image.name)
        with open(img_path,'wb') as file:
            for chunk in image.chunks():
                file.write(chunk)
        name = request.POST.get('name2')
        number = request.POST.get('number2')
        email = request.POST.get('email2')
        comment = request.POST.get('comment2')

        OrderInstance = OrderNow(service=service,image=image,name=name,number=number,email= email,comment=comment)

        
        OrderInstance.save()
        
        email_subject = service
        email_body ="{}\n{}".format(service,comment)
        recipient_email = ["mangaverse1002@gmail.com"]
        email = EmailMessage(
            subject=email_subject,
            body=email_body,
            from_email=email,
            to=recipient_email
        )
        
        email.attach_file(img_path)
        email.send(fail_silently=False)
    return render(request,'ordernow.html',data3)
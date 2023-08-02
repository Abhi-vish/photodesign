from django.db import models

# Create your models here.
class HowWeWork(models.Model):
    image = models.ImageField(upload_to='img/',null=True)
    title = models.CharField(max_length=30)
    about = models.TextField()

class WhyToChooseUs(models.Model):
    title = models.CharField(max_length=100)
    descp = models.TextField()

class OurServices(models.Model):
    image = models.ImageField(upload_to='services_img',null=True)
    title = models.CharField(max_length=50)
    descp = models.TextField()

class AboutUs(models.Model):
    desc = models.TextField()

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.TextField(max_length=100)
    phone = models.IntegerField()
    country = models.CharField(max_length=50)
    findus = models.CharField(max_length=50)
    comment = models.TextField()

class Service(models.Model):
    serviceTitle = models.CharField(max_length=200)

    image = models.ImageField(upload_to='our_services')
    title = models.CharField(max_length=200)
    desc = models.TextField(blank=True,null=True)

    title1 = models.CharField(max_length=200)
    image1 = models.ImageField(upload_to='our_services',blank=True,null=True)
    desc1 = models.TextField(blank=True,null=True)

    image2 = models.ImageField(upload_to='our_services',blank=True,null=True)
    desc2 = models.TextField(blank=True,null=True)

    image3 = models.ImageField(upload_to='our_services',blank=True,null=True)
    desc3 = models.TextField(blank=True,null=True)

    image4 = models.ImageField(upload_to='our_services',blank=True,null=True)
    desc4 = models.TextField(blank=True,null=True)
    
    image5 = models.ImageField(upload_to='our_services',blank=True,null=True)
    desc5 = models.TextField(blank=True,null=True)

    image6 = models.ImageField(upload_to='our_services',blank=True)
    desc6 = models.TextField(blank=True,null=True)


class FreeTrial(models.Model):
    name = models.CharField(max_length=200,blank=False,null=False)
    email = models.EmailField(blank=False,null=False)
    service = models.CharField(max_length=200,null=False,blank=False)
    image = models.FileField(upload_to='Trial_image/')
    comment = models.TextField()

class PricingData(models.Model):
    cardTitle = models.CharField(max_length=200)
    image = models.ImageField(upload_to="Pricing_img")
    price = models.IntegerField()

class OrderNow(models.Model):
    service = models.CharField(max_length=200,null=False,blank=False)
    image = models.ImageField(upload_to='Order_img')
    name = models.CharField(max_length=200)
    number = models.IntegerField(null=False,blank=False)
    email = models.EmailField(null=False,blank=False)
    comment = models.TextField(null=False,blank=False)
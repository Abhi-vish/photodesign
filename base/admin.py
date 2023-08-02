from django.contrib import admin
from .models import HowWeWork,WhyToChooseUs,OurServices,AboutUs,ContactUs,Service,FreeTrial,PricingData,OrderNow

# Register your models here.

class HowWeWorkAdmin(admin.ModelAdmin):
    list_display= ['image','title','about']

admin.site.register(HowWeWork,HowWeWorkAdmin)

class WhyToChooseUsAdmin(admin.ModelAdmin):
    list_display = ['title','descp']
admin.site.register(WhyToChooseUs,WhyToChooseUsAdmin)

class OurServicesAdmin(admin.ModelAdmin):
    list_display = ['image','title','descp']
admin.site.register(OurServices,OurServicesAdmin)

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['desc']
admin.site.register(AboutUs,AboutUsAdmin)

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone','country','findus','comment']
admin.site.register(ContactUs,ContactUsAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['serviceTitle','image','title','desc','title1','image1','desc1','image2','desc2','image3','desc3','image4','desc4','image5','desc5','image6','desc6']

admin.site.register(Service,ServiceAdmin)


class FreeTrialAdmin(admin.ModelAdmin):
    list_display = ['name','email','service','image','comment']

admin.site.register(FreeTrial,FreeTrialAdmin)


class PricingAdmin(admin.ModelAdmin):
    list_display = ['cardTitle','image','price']

admin.site.register(PricingData,PricingAdmin)

class OrderNowAdimin(admin.ModelAdmin):
    list_display = ['service','image','name','number','email','comment']
admin.site.register(OrderNow,OrderNowAdimin)
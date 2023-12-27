from django.contrib.admin import ModelAdmin, register
from .models import Job,JobSeeker,Company,Provinces,Category


@register(Job)
class JobAdmin(ModelAdmin):
    pass

@register(JobSeeker)
class JobSeekerAdmin(ModelAdmin):
    pass

@register(Company)
class CompanyAdmin(ModelAdmin):
    pass

@register(Provinces)
class ProvincesAdmin(ModelAdmin):
    pass

@register(Category)
class categoryAdmin(ModelAdmin):
    pass
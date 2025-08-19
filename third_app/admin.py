from django.contrib import admin
from . models import PersonalInfo
from . models import Skill


# Register your models here.
admin.site.register(PersonalInfo)


admin.site.register(Skill)


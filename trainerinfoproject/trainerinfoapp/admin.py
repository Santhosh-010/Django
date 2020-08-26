from django.contrib import admin
from .models import Trainer_info

# Register your models here.
class Trainer_infoAdmin(admin.ModelAdmin):
    '''
        Admin View for Trainer_info
    '''
    list_display = ('FIRST_NAME','LAST_NAME','DOMAIN','EXPERIENCE','BRANCH','ADDRESS','GENDER','SALARY')
    

admin.site.register(Trainer_info, Trainer_infoAdmin)


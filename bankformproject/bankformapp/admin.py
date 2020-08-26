from django.contrib import admin
from bankformapp.models import AccDetails

# Register your models here.
class AccDetailsAdmin(admin.ModelAdmin):
    '''
        Admin View for AccDetails
    '''
    list_display = ('FirstName','LastName','DOB','Address','AccType','PanNo')
    

admin.site.register(AccDetails, AccDetailsAdmin)

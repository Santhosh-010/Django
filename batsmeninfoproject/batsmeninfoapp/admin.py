from django.contrib import admin
from .models import Batsmen_Info

# Register your models here.
class Batsmen_InfoAdmin(admin.ModelAdmin):
    '''
        Admin View for Batsmen_Info
    '''
    list_display = ('First_Name','Last_Name','Country','Age','Runs','Avg','Rank','Played','Strike_rate')
    
admin.site.register(Batsmen_Info, Batsmen_InfoAdmin)

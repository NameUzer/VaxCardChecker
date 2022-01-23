from django.contrib import admin
from .models import Enjoyer, PreRegister
admin.site.site_header='Admin'
admin.site.site_title='VCCS Admin'
admin.site.index_title='Welcome to VCS Admin'

class UserAdmin(admin.ModelAdmin):
    list_display = ['Idnumber','Lname','Fname','MI','VMfirstdose','VMseconddose','Sfirstdose','Sseconddose']
admin.site.register(Enjoyer,UserAdmin)
class reqRegister(admin.ModelAdmin):
    list_display = ['VC_Image', 'user_Idnumber', 'user_Lname', 'user_Fname', 'user_MI', 'user_Address', 'user_contactnumber' \
        , 'user_dateofbirth', 'user_VMfirstdose', 'user_VMseconddose', 'user_Sfirstdose', 'user_Sseconddose','user_Email']
admin.site.register(PreRegister, reqRegister)
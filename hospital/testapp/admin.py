from django.contrib import admin
from .models import Hospital, Salesperson, Register ,My_Temp,My_upload,Multi, Custom_Files,Pagination



class HospitalModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'mobile']

class SalespersonModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','hospital']

class RegisterModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','hospital_name','hospital_owner','mobile','distric','state']

class My_TempModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','hospital','salesperson','address','state']

class My_uploadModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','aadhar_image','pancard_image']

class MultiModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','image']


class Custom_imagesModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','profile_pic','aadhar_pic','xl_file']

class PaginationModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','user_name','hospital','mobile']



admin.site.register(Pagination,PaginationModelAdmin)


admin.site.register(Custom_Files,Custom_imagesModelAdmin)

admin.site.register(Multi,MultiModelAdmin)
admin.site.register(My_upload,My_uploadModelAdmin)

admin.site.register(Hospital,HospitalModelAdmin)
admin.site.register(Salesperson,SalespersonModelAdmin)
admin.site.register(Register,RegisterModelAdmin)
admin.site.register(My_Temp,My_TempModelAdmin)

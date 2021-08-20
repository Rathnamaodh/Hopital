from django.db import models
from django.contrib.auth.models import User

class Hospital(models.Model):
    name = models.CharField(max_length=60)
    mobile = models.IntegerField()

    def __str__(self):
        return str(self.name)


class Salesperson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # hospital = models.ForeignKey(hospital, on_delete=models.CASCADE)
    hospital = models.OneToOneField(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.hospital)


class Register(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    hospital_name = models.CharField(max_length=150)
    hospital_owner = models.CharField(max_length=150)
    mobile = models.IntegerField()
    distric = models.CharField(max_length=100)
    state = models.CharField(max_length=150)

    def __str__(self):
        return str(self.hospital_name)


class My_upload(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    aadhar_image = models.ImageField(upload_to='images')
    pancard_image = models.ImageField(upload_to='images')


    def __str__(self):
        return str(self.user)

class Multi(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.FileField(upload_to='multiple/images')

    def __str__(self):
        return str(self.user)



class My_Temp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    hospital = models.OneToOneField(Hospital, on_delete=models.CASCADE,default=1)

    salesperson = models.OneToOneField(Salesperson, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return str(self.hospital)



#****************************************************************88
#********************************************************************88
from django.core.validators import FileExtensionValidator
from .validation import validate_file_extension_image, validate_file_extension_xls

class Custom_Files(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.FileField(upload_to='custom/images/',validators=(validate_file_extension_image,))
    aadhar_pic = models.FileField(upload_to='custom/pdf/',validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    xl_file = models.FileField(upload_to='custom/xls/',validators=(validate_file_extension_xls,))

    def __str__(self):
        return str(self.user)
##*************************************************************************************************************
##################################################################################################################3
# for pagination concept

class Pagination(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=120)
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    mobile = models.IntegerField()

    def __str__(self):
        return str(self.user)




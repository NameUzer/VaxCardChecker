import os.path
from django.db import models
from datetime import datetime
from django.utils import timezone
from django.utils.html import mark_safe
import os,random
now =timezone.now()
class Enjoyer(models.Model):

    Idnumber = models.CharField(max_length=100,verbose_name='ID NO.',unique=True)
    Lname = models.CharField(max_length=100, verbose_name='Last Name')
    Fname=models.CharField(max_length=100, verbose_name='First Name')
    MI = models.CharField(max_length=100, verbose_name='Middle Initial')
    VMfirstdose=models.CharField(max_length=100,verbose_name='VM First Dose')
    VMseconddose=models.CharField(max_length=100,verbose_name='VM Second Dose')
    Sfirstdose=models.DateField(auto_now_add=False,auto_now=False,blank=True, verbose_name='Sched First Dose')
    Sseconddose = models.DateField(auto_now_add=False,auto_now=False,blank=True, verbose_name='Sched Second Dose')


    def __str__(self):
        return self.Idnumber
class PreRegister(models.Model):
    def image_path(instance, filename):
        basefilename, file_extension = os.path.splitext(filename)
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhijklmnopqrstuvwxyz1234567890'
        randomstr = ''.join((random.choice(chars)) for x in range(10))
        _now = datetime.now()

        return 'VCpic/{year}-{month}-{day}-{imageid}-{basename}-{randomstring}-{ext}'.format\
            (imageid=instance,
             basename=basefilename, randomstring=randomstr, ext=file_extension, year=_now.strftime('%Y'),
             month=_now.strftime('%m'), day=_now.strftime('%d'))

    user_Idnumber = models.CharField(max_length=100, verbose_name='idnum', unique=True)
    user_Lname = models.CharField(max_length=100, verbose_name='LastName')
    user_Fname = models.CharField(max_length=100, verbose_name='FirstName')
    user_MI = models.CharField(max_length=100, verbose_name='MiddleInitial')
    user_Address = models.CharField(max_length=100, verbose_name='Address')
    user_contactnumber = models.CharField(max_length=11, verbose_name='ContactNumber')
    user_dateofbirth = models.DateField(auto_now_add=False, auto_now=False, blank=True, verbose_name='Date of Birth')
    user_VMfirstdose = models.CharField(max_length=100, verbose_name='VMFirstDose')
    user_VMseconddose = models.CharField(max_length=100, verbose_name='VMSecondDose')
    user_Sfirstdose = models.DateField(auto_now_add=False, auto_now=False, blank=True, verbose_name='SchedFirstDose')
    user_Sseconddose = models.DateField(auto_now_add=False, auto_now=False, blank=True, verbose_name='SchedSecondDose')
    VCphoto = models.ImageField(upload_to=image_path, default='VCpic/image.jpg')
    user_Email = models.EmailField(max_length=100, verbose_name='Email', default='Example@gmail.com')

    def VC_Image(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.VCphoto))

    def __str__(self):
        return self.user_Idnumber
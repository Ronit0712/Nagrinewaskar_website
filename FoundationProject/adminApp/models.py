from django.db import models

# Create your models here.
class AdminModel(models.Model):
    user_email = models.EmailField(max_length=200)
    user_password = models.CharField(max_length=50)


class SliderModel(models.Model):
    slider_image = models.ImageField(upload_to="static/uploads/")
    slider_title = models.CharField(max_length=200)
    slider_description = models.CharField(max_length=200)


class ServicesModel(models.Model):
    services_image = models.ImageField(upload_to="static/upolads/")
    services_title = models.CharField(max_length=200)
    services_description = models.CharField(max_length=200)

class CertifideModel(models.Model):
    certifide_image = models.ImageField(upload_to="static/uploads/")

class BlogsModel(models.Model):
    blogs_image = models.ImageField(upload_to="static/uploads/")
    blogs_title = models.CharField(max_length=200)
    blogs_description = models.CharField(max_length=200)
    blogs_text = models.CharField(max_length=200)
    blogs_head = models.CharField(max_length=200)


class Mdesign (models.Model):
    mimage= models.ImageField(upload_to="static/uploads/")

class Mdesign2(models.Model):
    mimage2 = models.ImageField(upload_to="static/uploads/")  

class MissionModel(models.Model):
    mimage= models.ImageField(upload_to="static/uploads/")
    mtitle = models.CharField(max_length = 200, default="true") 
    mdis = models.TextField()

class visionModel(models.Model):
    vtitle = models.CharField(max_length = 200)
    vimage = models.ImageField(upload_to="static/uploads/")
    vdis = models.TextField()
 
class ValuesModdel(models.Model):
    valimage = models.ImageField(upload_to="static/uploads/")
    valtitle =  models.CharField(max_length = 100)
    valdetails = models.TextField()

class VisioncardModel(models.Model):
    vcdis = models.TextField()
    vcimage = models.ImageField(upload_to="static/uploads/")
    vcimgtitle = models.CharField(max_length = 100)

class HistoryModel(models.Model):
    himage = models.ImageField(upload_to="static/uploads/")
    hdate = models.CharField(max_length = 100)
    hdetails = models.TextField()

class RhistoryModel(models.Model):
    rhimage = models.ImageField(upload_to="static/uploads/")
    rhdate = models.CharField(max_length = 100)
    rhdetails = models.TextField()

class Gallerys1model(models.Model):
    s1img =  models.ImageField(upload_to="static/uploads/")

class Gallerys2model(models.Model):
    s2img = models.ImageField(upload_to="static/uploads/")

class Gallerys3model(models.Model):
    s3img = models.ImageField(upload_to="static/uploads/")

class Gallerys4model(models.Model):
    s4vid = models.FileField(upload_to="static/uploads/")
    s4edis = models.TextField()
    s4mdis = models.TextField()

class ActivitysliderModel(models.Model):
    actimage = models.ImageField(upload_to="static/uploads/")
    acttitle = models.CharField(max_length = 100)



class ActivityModel(models.Model):
    actiname = models.CharField(max_length = 100, default="true")
    actiimage = models.ImageField(upload_to="static/uploads/")
    actititle = models.CharField(max_length = 100)

class AchievementModel(models.Model):
    achivimage = models.ImageField(upload_to="static/uploads/")
    achivtitle = models.CharField(max_length = 100)
    achivdis = models.CharField(max_length = 300)

class AchievementModel2(models.Model):
    achivimage = models.ImageField(upload_to="static/uploads/")
    achivdate = models.CharField(max_length=200)
    achivtitle = models.CharField(max_length=200)
    achivdis = models.CharField(max_length=200)


class ContactModel(models.Model) :
    address = models.CharField(max_length = 200)
    phoneno = models.CharField(max_length = 15)
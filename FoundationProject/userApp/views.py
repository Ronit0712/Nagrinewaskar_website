from django.http import HttpResponse
from django.shortcuts import redirect, render
from adminApp.models import AchievementModel, AchievementModel2, ActivityModel, ActivitysliderModel, BlogsModel, CertifideModel, ContactModel, Gallerys1model, Gallerys2model, Gallerys3model, Gallerys4model, HistoryModel, Mdesign, MissionModel, RhistoryModel, ServicesModel, SliderModel, ValuesModdel, VisioncardModel, visionModel
from userApp.models import ContactlistModel, InquiryModel
# Create your views here.
def home(req):
    home = SliderModel.objects.all()
    services = ServicesModel.objects.all()
    certifide = CertifideModel.objects.all()
    blogs = BlogsModel.objects.all()
    missions = MissionModel.objects.all()
    forms = InquiryModel.objects.all()
    return render(req,"user/home.html",{"home":home,"services":services,"certifide":certifide,"blogs":blogs,"missions":missions, "forms":forms})


def save_form(req):
    newforms = InquiryModel(
    name = req.POST['name'],
    mobile = req.POST['mobile'],
    address = req.POST['address'],
    email = req.POST['email'],
    message = req.POST['message'],
    )
    newforms.save()

    return redirect("/")


def mission(req):
    # mimages = Mdesign.objects.all()
    missions = MissionModel.objects.all()
    return render(req,"user/mission.html",{"missions":missions})

def vision(req):
    visions = visionModel.objects.all()
    values = ValuesModdel.objects.all()
    vcards = VisioncardModel.objects.all()
    return render(req,"user/vision.html",{"visions":visions, "values":values, "vcards":vcards})

def history(req):
    hcards = HistoryModel.objects.all()
    rhcards = RhistoryModel.objects.all()
    return render(req,"user/history.html", {"hcards":hcards , "rhcards":rhcards})

def gallery(req):
    s1imgs = Gallerys1model.objects.all()
    s2imgs = Gallerys2model.objects.all()
    s3imgs = Gallerys3model.objects.all()
    s4vid = Gallerys4model.objects.all()
    return render(req,"user/gallery.html",{"s1imgs":s1imgs , "s2imgs":s2imgs, "s3imgs":s3imgs, "s4vid":s4vid})


def activities(req):
    actslides = ActivitysliderModel.objects.all() 
    activities = ActivityModel.objects.all()
    return render(req,"user/activities.html",{"actslides":actslides, "activities":activities})

def achievements(req):
    achievements = AchievementModel.objects.get(id=2)
    achive = AchievementModel2.objects.all()
    return render(req,"user/achievements.html",{"achievements":achievements, "achive":achive})

def contact(req):
    contactinfo = ContactModel.objects.get(id = 5)
    contacts = ContactlistModel.objects.all()
    return render(req,"user/contact.html",{"contacts":contacts, "contactinfo":contactinfo})

def save_contact(req):
    newcontact = ContactlistModel(
        fullname = req.POST['fullname'],
        mnumber = req.POST['mnumber'],
        email = req.POST['email'],
        city = req.POST['city'],
        message = req.POST['message']
    )
    newcontact.save()
    return redirect ("/contact")
    # return HttpResponse("saved")



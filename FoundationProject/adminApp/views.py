from django.http import HttpResponse
from django.shortcuts import redirect, render
from adminApp.models import AchievementModel, AchievementModel2, ActivityModel, AdminModel, BlogsModel, CertifideModel, ContactModel, Gallerys3model, Gallerys4model,MissionModel, RhistoryModel, ServicesModel, SliderModel,visionModel,ValuesModdel, VisioncardModel, HistoryModel, Gallerys1model, Gallerys2model, ActivitysliderModel
from userApp.models import ContactlistModel, InquiryModel
# Create your views here.
def login(req):
    return render(req,"admin/login.html")

def do_login(req):
    # newuser = AdminModel()
    # newuser.user_email = req.POST['useremail'],
    # newuser.user_password = req.POST['userpassword']
    # # newuser.save()
    # return redirect("/admin/home")

    # print(req.POST)


    userdet = AdminModel.objects.filter(
        user_email= req.POST['useremail'],
        user_password = req.POST['userpassword']
    )
    if(len(userdet)>0):
        req.session['user_id']=userdet[0].id
        return redirect("/admin/home")
    else:
        return redirect("/admin/login")
        # return HttpResponse("Login Failed")
    

    



def home(req):
    if(not req.session.has_key('user_id')):
        return redirect("/admin")
    
    home = SliderModel.objects.all()
    services = ServicesModel.objects.all()
    certifide = CertifideModel.objects.all()
    blogs = BlogsModel.objects.all()
    return render(req, "admin/home.html",{"home":home,"services":services,"certifide":certifide,"blogs":blogs})

def save_home(req):
    newhome = SliderModel(
       slider_image = req.FILES['slider_image'],
       slider_title = req.POST['slider_title'],
       slider_description = req.POST['slider_description']

    )
    newhome.save()
    return redirect("/admin/home")




    # update = SliderModel.objects.get(id = 3)
    # if "slider_image" in req.FILES:
    #     update.slider_image = req.FILES['slider_image']
        
    # update.slider_title = req.POST['slider_title']
    # update.slider_description = req.POST['slider_description']
    # update.save()
    # return redirect("/admin/home")
    # return HttpResponse("dhfmgxjcvm")

def delete_home(req):
    SliderModel.objects.get(id = req.GET['id']).delete()
    return  redirect("/admin/home")




def inquiry(req):
    if(not req.session.has_key('user_id')):
        return redirect("/admin")
    forms = InquiryModel.objects.all()
    return render(req,"admin/inquiry.html",{"forms":forms})

def delete_inquiry(req):
    InquiryModel.objects.get(id = req.GET['id']).delete()

    return redirect("/admin/inquiry")

 



def save_services(req):
    newservices = ServicesModel(
       services_image = req.FILES['services_image'],
       services_title = req.POST['services_title'],
       services_description = req.POST['services_description']

    )
    newservices.save()
    return redirect("/admin/home")

def delete_services(req):
    ServicesModel.objects.get(id = req.GET['id']).delete()
    return redirect("/admin/home")

def save_certifide(req):
    nwecertifide = CertifideModel(
       certifide_image = req.FILES['certifide_image'],
    )
    nwecertifide.save()
    return redirect("/admin/home")

def delete_certifide(req):
    CertifideModel.objects.get(id = req.GET['id']).delete()
    return redirect("/admin/home")

def save_blogs(req):
    newblogs = BlogsModel(
        blogs_image = req.FILES['blogs_image'],
        blogs_title = req.POST['blogs_title'],
       blogs_description = req.POST['blogs_description'],
       blogs_text = req.POST['blogs_text'],
       blogs_head = req.POST['blogs_head']
    )
    newblogs.save()
    return redirect("/admin/home")

def delete_blogs(req):
    BlogsModel.objects.get(id = req.GET['id']).delete()
    return redirect("/admin/home")

def edit_blogs(req):
    obj = {"user_blogs":BlogsModel.objects.get(id = req.GET['id'])}

    return render(req,"admin/edit_blogs.html",obj)


def update_blogs(req):
    old = BlogsModel.objects.get(id= req.POST['id'])

    if("blogs_image" in req.FILES):
        old.blogs_image = req.FILES['blogs_image']

    old.blogs_title = req.POST['blogs_title']
    old.blogs_description = req.POST['blogs_description']
    old.blogs_text = req.POST['blogs_text']
    old.blogs_head = req.POST['blogs_head']

    old.save()
    return redirect("/admin/home")


# ABOUT -----------------------------------------------------------------------------------

def about (req):
    if(not req.session.has_key('user_id')):
        return redirect("/admin")
    # mimages = Mdesign.objects.get(id=1)
    # mimages2 = Mdesign2.objects.all()

   

    missions = MissionModel.objects.all()
    visions = visionModel.objects.all()
    values = ValuesModdel.objects.all()
    vcards = VisioncardModel.objects.all()
    hcards = HistoryModel.objects.all()
    rhcards = RhistoryModel.objects.all()
    return render (req, "admin/about.html",{"missions":missions, "visions":visions, "values":values , "vcards":vcards, "hcards":hcards, "rhcards":rhcards})

# def save_mdesign(req):
   
#     # newmimage = Mdesign(
#     #     mimage2 = req.FILES['mimage2']
#     # )
#     # newmimage.save()

#     update_mimage = Mdesign.objects.get(id=1)
#     if "mimage" in req.FILES:
#         update_mimage.mimage = req.FILES['mimage']
    
#     update_mimage.save()
#     return redirect("/admin/about")

# def save_mdesign2(req):
   
#     newmimage2 = Mdesign2(
#         mimage2 = req.FILES['mimage2']
#     )
#     newmimage2.save()

#     # update_mimage = Mdesign.objects.get(id=1)
#     # if "mimage" in req.FILES:
#     #     update_mimage.mimage = req.FILES['mimage']
    
#     # update_mimage.save()
#     return redirect("/admin/about")

def save_mission(req):
    newmission = MissionModel(
        mimage = req.FILES['mimage'],
        mtitle = req.POST['mtitle'],
        mdis = req.POST['mdis']
    )
    newmission.save() 
    return redirect("/admin/about")

def delete_mission(req):
    MissionModel.objects.get(id = req.GET['id']).delete()
    return redirect("/admin/about")

def save_vision(req):
    newvision = visionModel(
        vtitle = req.POST['vtitle'], 
        vimage = req.FILES['vimage'],
        vdis = req.POST['vdis'],
    )
    newvision.save()
    return redirect("/admin/about")

def delete_vision(req):
    visionModel.objects.get(id = req.GET['id']).delete()
    return redirect("/admin/about")


def save_values(req):
    newvalues = ValuesModdel(
        valimage = req.FILES['valimage'],
        valtitle = req.POST['valtitle'],
        valdetails = req.POST['valdetails'],
    )
    newvalues.save()
    return redirect("/admin/about")

def delete_values(req):
    ValuesModdel.objects.get(id = req.GET['id']).delete()
    return redirect("/admin/about")

def save_vcard(req):
    newvcard = VisioncardModel(
        # vcdis = req.POST['vcdis'],
        vcimage = req.FILES['vcimage'],
        vcimgtitle = req.POST['vcimgtitle']
    )
    newvcard.save()
    return redirect("/admin/about")

def delete_vcard(req):
    VisioncardModel.objects.get(id = req.GET['id']).delete()
    return redirect("/admin/about")

def save_history(req):
    newhistory = HistoryModel(
        himage = req.FILES['himage'],
        hdate = req.POST['hdate'],
        hdetails = req.POST['hdetails']
    )
    newhistory.save()
    return redirect("/admin/about")

def delete_history(req):
    HistoryModel.objects.get(id = req.GET['id']).delete()
    return redirect("/admin/about")

def save_rhistory(req):
    newrhistory = RhistoryModel(
        rhimage = req.FILES['rhimage'],
        rhdate = req.POST['rhdate'],
        rhdetails = req.POST['rhdetails']
    )  
    newrhistory.save()
    return redirect("/admin/about") 

def delete_rhistory(req):
    RhistoryModel.objects.get(id  = req.GET['id']).delete()
    return redirect("/admin/about") 



#GALLERY----------------------------------------------------------------------------------
def gallery (req):
    if(not req.session.has_key('user_id')):
        return redirect("/admin")   
    s1imgs = Gallerys1model.objects.all()
    s2imgs = Gallerys2model.objects.all()
    s3imgs = Gallerys3model.objects.all()
    s4vid = Gallerys4model.objects.all()


    return render (req, "admin/gallery.html",{"s1imgs":s1imgs, "s2imgs":s2imgs, "s3imgs":s3imgs, "s4vid":s4vid})

def save_s1img(req):
    news1img = Gallerys1model(
        s1img = req.FILES['s1img']
    )
    news1img.save()
    return redirect("/admin/gallery")

def delete_s1img(req):
    Gallerys1model.objects.get(id = req.GET['id']).delete()
    return redirect("/admin/gallery")

def save_s2img(req):
    news2img = Gallerys2model(
        s2img = req.FILES['s2img']
    )
    news2img.save()
    return redirect("/admin/gallery")

def delete_s2img(req):
    Gallerys2model.objects.get(id = req.GET['id']).delete()
    return redirect("/admin/gallery")

def save_s3img(req):
    news3img = Gallerys3model(
        s3img = req.FILES['s3img']
    )
    news3img.save()
    return redirect("/admin/gallery")

def delete_s3img(req):
    Gallerys3model.objects.get(id = req.GET['id']).delete()
    return redirect("/admin/gallery")

def save_s4vid(req):
    news4vid = Gallerys4model(
        s4vid = req.FILES['s4vid'],
        s4edis = req.POST['s4edis'], 
        s4mdis = req.POST['s4mdis'] 
    )
    news4vid.save()
    return redirect("/admin/gallery")

def delete_s4vid(req):
    Gallerys4model.objects.get(id = req.GET['id']).delete()
    return redirect("/admin/gallery")




#ACTIVITIES----------------------------------------------------------------------------
def activities (req):
    if(not req.session.has_key('user_id')):
        return redirect("/admin")
    actslides = ActivitysliderModel.objects.all() 
    activities = ActivityModel.objects.all()
    return render (req, "admin/activities.html",{"actslides":actslides , "activities":activities})

def save_actslider(req):
    newactslide = ActivitysliderModel(
        actimage = req.FILES['actimage'],
        acttitle = req.POST['acttitle']
    )
    newactslide.save()
    return redirect ("/admin/activities")

def delete_actslide(req):
    ActivitysliderModel.objects.get(id = req.GET['id']).delete()
    return redirect ("/admin/activities")

def save_activity(req):
    newactivity = ActivityModel(
        
        actiimage = req.FILES['actiimage'],
        actititle = req.POST['actititle'],
    )
    newactivity.save()
    return redirect ("/admin/activities")

def delete_activity(req):
    ActivityModel.objects.get(id = req.GET['id']).delete()
    return redirect ("/admin/activities")





#ACHIEVEMENTS ---------------------------------------------------------------------------

def achievements (req):
    if(not req.session.has_key('user_id')):
        return redirect("/admin")
    achievements = AchievementModel.objects.get(id=2)
    achive = AchievementModel2.objects.all()
    return render (req, "admin/achievements.html",{"achievements":achievements,"achive":achive})

def update_achievement(req):
    # newachive = AchievementModel(
    #     achivimage = req.FILES['achivimage'],
    #     achivdis = req.POST['achivdis'],
    #     achivtitle = req.POST['achivtitle'],
    # )
    # newachive.save()
    # return HttpResponse("Done")

    updateachive = AchievementModel.objects.get(id = 2)
    if "achivimage" in req.FILES:
        updateachive.achivimage = req.FILES['achivimage']
    updateachive.achivdis = req.POST['achivdis']
    updateachive.achivtitle = req.POST['achivtitle']

    updateachive .save()
    return redirect("/admin/achievements")

def save_achievements(req):
    newachive = AchievementModel2(
        achivimage = req.FILES['achivimage'],
        achivdis = req.POST['achivdis'],
        achivdate = req.POST['achivdate'],
        achivtitle = req.POST['achivtitle'],
    )
    newachive.save()
    return redirect("/admin/achievements")

def delete_achive(req):
    AchievementModel2.objects.get(id = req.GET['id']).delete()
    return redirect("/admin/achievements")




#CONTACT US------------------------------------------------------------------------------

def contact_us (req):
    if(not req.session.has_key('user_id')):
        return redirect("/admin")
    contacts = ContactModel.objects.get(id=5)
    contactlist = ContactlistModel.objects.all()
    return render (req, "admin/contact_us.html",{"contacts":contacts , "contactlist":contactlist})

def save_contact(req):
    # newcontact = ContactModel(
    #     address = req.POST['address'],
    #     phoneno = req.POST['phoneno']
    # )
    # newcontact.save()
    updatecontact = ContactModel.objects.get(id=5)
    updatecontact.address = req.POST['address']
    updatecontact.phoneno = req.POST['phoneno']
    updatecontact.save()


    return redirect("/admin/contact_us")




def delete_contactlist(req):
    ContactlistModel.objects.get(id = req.GET['id']).delete()
    return redirect ("/admin/contact_us")
from django.urls import path
from adminApp import views
 
urlpatterns = [
    path('',views.login),
    path('home/',views.home),
    path('do_login/',views.do_login),

    path('save_home/',views.save_home),
    path('delete_home/',views.delete_home),

    path('inquiry/',views.inquiry),
    path('delete_inquiry/',views.delete_inquiry),



    path('save_services/',views.save_services),
    path('delete_services/',views.delete_services),

    path('save_certifide/',views.save_certifide),
    path('delete_certifide/',views.delete_certifide),
    
    path('save_blogs/',views.save_blogs),
    path('delete_blogs/',views.delete_blogs),
    path('edit_blogs/',views.edit_blogs),
    path('update_blogs/',views.update_blogs),


    path('about/',views.about),
    # path('save_mdesign/',views.save_mdesign),
    # path('save_mdesign2/',views.save_mdesign2),

    path('save_mission/',views.save_mission),
    path('delete_mission/',views.delete_mission),

    path('save_vision/',views.save_vision),
    path('delete_vision/',views.delete_vision),

    path('save_values/',views.save_values),
    path('delete_values/',views.delete_values),

    path('save_vcard/',views.save_vcard),
    path('delete_vcard/',views.delete_vcard),

    path('save_history/',views.save_history),
    path('delete_history/',views.delete_history),

    path('save_rhistory/',views.save_rhistory),
    path('delete_rhistory/',views.delete_rhistory),

   





    path('gallery/',views.gallery),

    path('save_s1img/',views.save_s1img),
    path('delete_s1img/',views.delete_s1img),

    path('save_s2img/',views.save_s2img),
    path('delete_s2img/',views.delete_s2img),

    path('save_s3img/',views.save_s3img),
    path('delete_s3img/',views.delete_s3img),

    path('save_s4vid/',views.save_s4vid),
    path('delete_s4vid/',views.delete_s4vid),
    





    path('activities/',views.activities),
    path('save_actslider/',views.save_actslider),
    path('delete_actslide/',views.delete_actslide),

    path('save_activity/',views.save_activity),
    path('delete_activity/',views.delete_activity),



    path('achievements/',views.achievements),
    path('update_achievement/',views.update_achievement),
    path('save_achievements/',views.save_achievements),
    path('delete_achive/',views.delete_achive),


    path('contact_us/',views.contact_us),
    path('save_contact/',views.save_contact),

    path('delete_contactlist/',views.delete_contactlist)

   




]
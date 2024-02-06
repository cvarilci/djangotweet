from django.urls import path
from . import views

app_name="tweety_app"

urlpatterns = [
    path("",views.listtweet,name="listtweet"),#atilsamancioglu.com/tweety_app/
    path("addtweet/",views.addtweet,name="addtweet"),#atilsamancıoglu.com/tweety_app/addtweet
    path("addtweetbyform/",views.addtweetbyform,name="addtweetbyform"),
    path("addtweetbymodelform/",views.addtweetbymodelform,name="addtweetbymodelform"),
    path("signup/",views.SignUpView.as_view(),name="signup"),
    path("deletetweet/<int:id>",views.deletetweet,name='deletetweet'),
]
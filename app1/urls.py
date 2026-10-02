from django.urls import path

from . import views

urlpatterns=[
    path("",views.dashboard,name="dashboard"),
    path("sign/",views.sign,name="sign"),
    path("login/",views.login,name="login"),
    path("sign_vad/",views.sign_vad,name="sign_vad"),
    path("login_vad/",views.login_vad,name="login_vad"),
    path("log_out/",views.log_out,name="log_out"),
    path("adddata/",views.adddata,name="adddata"),
    path("home/",views.home,name="home"),
    path("singledataget/",views.singledataget,name="singledataget"),
    path("alldataget/",views.alldataget,name="alldataget"),
    path("deletedataget/",views.deletedataget,name="deletedataget"),
    path("updatestudata/",views.updatestudata,name="updatestudata"),

]
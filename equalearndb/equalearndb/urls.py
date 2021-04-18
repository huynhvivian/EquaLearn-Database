"""equalearndb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from equalearn import views
from accounts import views as accounts_views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),

    # log in, log out, applications
    url(r'^home/(?P<username>[\w\-]+)/$', accounts_views.home, name = "home"),
#    url(r'login/', accounts_views.login, name = "login"),
    url(r'getusername/', accounts_views.getusername, name = "getusername"),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'client_app/(?P<id>\d+)/$', accounts_views.client_app, name = "client_app"),
    url(r'tutor_app/(?P<id>\d+)/$', accounts_views.tutor_app, name = "tutor_app"),
    url(r'choose_account/(?P<id>\d+)/$', accounts_views.choose_account, name = "choose_account"),
    url(r'choose_tutor/(?P<id>\d+)/$', accounts_views.choose_tutor, name = "choose_tutor"),
    url(r'choose_exec/(?P<id>\d+)/$', accounts_views.choose_exec, name = "choose_exec"),
    url(r'choose_client/(?P<id>\d+)/$', accounts_views.choose_client, name = "choose_client"),

    url(r'approve_volunteers/(?P<id>\d+)/$', views.approve_volunteers, name = "approve_volunteers"),
    url(r'approve_tutor/(?P<eid>\d+)/(?P<tid>\d+)/$', views.approve_tutor, name = "approve_tutor"),
    url(r'view_pending_clients/(?P<id>\d+)/$', views.view_pending_clients, name = "view_pending_clients"),
    url(r'approve_client/(?P<eid>\d+)/(?P<cid>\d+)/$', views.approve_client, name = "approve_client"),
    url(r'volunteer_dashboard/(?P<id>\d+)/$', views.volunteer_dashboard, name="volunteer_dashboard"),
    url(r'executive_dashboard/(?P<id>\d+)/$', views.executive_dashboard, name = "executive_dashboard"),
    url(r'volunteer_hours/(?P<id>\d+)/$', views.volunteer_hours, name = "volunteer_hours"),
    url(r'view_volunteer_hours/(?P<eid>\d+)/(?P<tid>\d+)/$', views.view_volunteer_hours, name = "view_volunteer_hours"),
    url(r'approve_hours/(?P<eid>\d+)/$', views.approve_hours, name = "approve_hours"),
    url(r'session_signups/(?P<id>\d+)/$', views.session_signups, name = "session_signups"),
    url(r'edit_session/(?P<uid>\d+)/(?P<sid>\d+)/$', views.edit_sessions, name = "edit_session"),
    url(r'confirm_session/(?P<tid>\d+)/(?P<sid>\d+)/$', views.submit_edited_sessions, name = "confirm_session"),
    url(r'cancel_session/(?P<tid>\d+)/(?P<sid>\d+)/$', views.cancel_session, name = "cancel_session"),
    url(r'view_sessions/(?P<eid>\d+)/$', views.view_pending_sessions, name = "view_sessions"),
    url(r'approve_sessions/(?P<eid>\d+)/(?P<psessionid>\d+)/$', views.approve_sessions, name = "approve_sessions"),
    url(r'sessions_signed_up/(?P<tid>\d+)/(?P<takeid>\d+)/$', views.sessions_signed_up, name = "sessions_signed_up"),
    url(r'client_dashboard/(?P<id>\d+)/$', views.client_dashboard, name="client_dashboard"),
    url(r'editstudents/(?P<id>\d+)/$', views.editstudents, name = "editstudents"),
    url(r'addstudent/(?P<id>\d+)/$', views.addstudent, name = "addstudent"),
    url(r'studentadded/(?P<id>\d+)/$', views.studentadded, name = "studentadded"),
    url(r'editsubject/(?P<id>\d+)/(?P<string>[\w\-]+)/$', views.editsubject, name = "editsubject"),
    path('', include('equalearn.urls'))
]

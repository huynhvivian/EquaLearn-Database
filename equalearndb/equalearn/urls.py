from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'executives', views.ExecutiveViewSet)
#router.register(r'tutors', views.TutorViewSet)
#router.register(r'clients', views.ClientViewSet)
#router.register(r'students', views.StudentViewSet)
#router.register(r'subjects', views.SubjectViewSet)
#router.register(r'sessions', views.SessionViewSet)
#router.register(r'pendingsessions', views.PendingSessionViewSet)
#router.register(r'takes', views.TakesViewSet)
#router.register(r'teaches', views.TeachesViewSet)
#router.register(r'preferredstudents', views.PreferredStudentViewSet)
#router.register(r'schedulesstudents', views.ScheduleStudentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('users/', views.user_list),
    path('users/<int:pk>/', views.user_detail),
    path('executives/', views.executive_list),
    path('executives/<int:pk>/', views.executive_detail),
    path('tutors/', views.tutor_list),
    path('tutors/<int:pk>/', views.tutor_detail),
    path('clients/', views.client_list),
    path('clients/<int:pk>/', views.client_detail),
    path('students/', views.student_list),
    path('students/<int:pk>/', views.student_detail),
    path('subjects/', views.subject_list),
    path('subjects/<int:pk>/', views.subject_detail),
    path('sessions/', views.session_list),
    path('sessions/<int:pk>/', views.session_detail),
    path('locations/', views.location_list),
    path('locations/<str:pk>/', views.location_detail),
    path('pendingsessions/', views.pendingsession_list),
    path('pendingsessions/<int:pk>/', views.pendingsession_detail),
    path('takes/', views.takes_list),
    path('takes/<int:pk>/', views.takes_detail),
    path('preferredstudents/', views.preferredstudent_list),
    path('preferredstudents/<int:pk>/', views.preferredstudent_detail),
    path('schedulestudents/', views.schedulestudent_list),
    path('schedulestudents/<int:pk>/', views.schedulestudent_detail),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

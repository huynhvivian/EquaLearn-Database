from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'executives', views.ExecutiveViewSet)
router.register(r'tutors', views.TutorViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'subjects', views.SubjectViewSet)
router.register(r'sessions', views.SessionViewSet)
router.register(r'pendingsessions', views.PendingSessionViewSet)
router.register(r'takes', views.TakesViewSet)
router.register(r'teaches', views.TeachesViewSet)
router.register(r'preferredstudents', views.PreferredStudentViewSet)
router.register(r'schedulesstudents', views.ScheduleStudentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

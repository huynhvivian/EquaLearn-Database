from rest_framework import serializers
from .models import User
from .models import Executive
from .models import Tutor
from .models import Client
from .models import Student
from .models import Session
from .models import Subject
from .models import Takes
from .models import Teaches
from .models import Location
from .models import schedule_student
from .models import preferred_student
from .models import PendingSession

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('User_ID', 'name', 'email', 'phone_number')


class ExecutiveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Executive
        fields = ('User_ID', 'name', 'email', 'phone_number', 'position')


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('User_ID', 'name', 'email', 'phone_number', 'referred_organization', 'proof_of_low_income', 'accepted')

class TutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tutor
        fields = ('User_ID', 'name', 'email', 'phone_number', 'date_started', 'preference_online', 'accepted', 'grade', 'club')

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('student_id', 'user_id_client', 'name', 'school')

class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = "('subject_id', 'course_name', 'grade_level')"

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"

class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"

class TakesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Takes
        fields = "__all__"

class TeachesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teaches
        fields = "__all__"

class PendingSessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PendingSession
        fields = "__all__"

class PreferredStudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preferred_student
        fields = "__all__"

class ScheduleStudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = schedule_student
        fields = "__all__"

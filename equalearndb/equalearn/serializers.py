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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ExecutiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executive
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"

class TakesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Takes
        fields = "__all__"

class TeachesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teaches
        fields = "__all__"

class PendingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PendingSession
        fields = "__all__"

class PreferredStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = preferred_student
        fields = "__all__"

class ScheduleStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = schedule_student
        fields = "__all__"

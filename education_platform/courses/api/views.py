from rest_framework import generics, viewsets
from rest_framework.views import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from courses.models import Subject, Course
from .serializers import (
    SubjectSerializer, CourseSerializer, CourseWithContentSerializer
)
from .permissions import IsEnrolled


class SubjectListView(generics.ListAPIView):
    """
    Get list of all subjects.
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    """
    Get details for a subject.
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(
        detail=True,
        methods=['post'],
        permission_classes=(IsAuthenticated, ),
        authentication_classes=(BasicAuthentication, )
    )
    def enroll(self, request, *args, **kwargs):
        course = self.get_object()
        course.students.add(request.user)
        return Response({'enrolled': True})

    @action(
        detail=True,
        methods=['get'],
        serializer_class=CourseWithContentSerializer,
        permission_classes=(IsAuthenticated, IsEnrolled,),
        authentication_classes=(BasicAuthentication, )
    )
    def contents(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

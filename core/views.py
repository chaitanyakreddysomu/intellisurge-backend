from rest_framework import viewsets
from .models import Blog, JobNotification, JobApplication,AdminUser,Contact,ClientTestimonials,OurTeam,TeamTestimonials,OurPartners,OurTeamCareer
from .serializers import BlogSerializer, JobNotificationSerializer,JobApplicationSerializer,AdminSerializer,ContactSerializer,ClientTestimonialsSerializer,OurTeamSerializer,TeamTestimonialsSerializer,PartnersSerializer,OurTeamCareerSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import status,generics
# from .models import AdminUser
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def create_admin(request):
    serializer = AdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminViewSet(viewsets.ModelViewSet):
    queryset = AdminUser.objects.all().order_by('-date_posted')
    serializer_class = AdminSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-date_posted')
    serializer_class = BlogSerializer

class JobNotificationViewSet(viewsets.ModelViewSet):
    queryset = JobNotification.objects.all().order_by('-posted_on')
    serializer_class = JobNotificationSerializer


class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
class ClientTestimonialsViewSet(viewsets.ModelViewSet):
    queryset = ClientTestimonials.objects.all()
    serializer_class = ClientTestimonialsSerializer
    
    
class TeamTestimonialsViewSet(viewsets.ModelViewSet):
    queryset = TeamTestimonials.objects.all()
    serializer_class = TeamTestimonialsSerializer

class OurTeamViewSet(viewsets.ModelViewSet):
    queryset = OurTeam.objects.all()
    serializer_class = OurTeamSerializer
    
class OurTeamCareerViewSet(viewsets.ModelViewSet):
    queryset = OurTeamCareer.objects.all()
    serializer_class = OurTeamCareerSerializer

class PartnersViewSet(viewsets.ModelViewSet):
    queryset = OurPartners.objects.all()
    serializer_class = PartnersSerializer


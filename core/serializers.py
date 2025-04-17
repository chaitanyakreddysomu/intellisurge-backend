from rest_framework import serializers
from .models import Blog, JobNotification,JobApplication,AdminUser,Contact,ClientTestimonials,OurTeam,TeamTestimonials,OurPartners,OurTeamCareer

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        fields = '__all__'
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class JobNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobNotification
        fields = '__all__'


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        
class ClientTestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientTestimonials
        fields = '__all__'
        
class TeamTestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamTestimonials
        fields = '__all__'
        
class OurTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeam
        fields = '__all__'
        
class OurTeamCareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeamCareer
        fields = '__all__'
        
class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurPartners
        fields = '__all__'
        

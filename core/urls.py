from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, JobNotificationViewSet,JobApplicationViewSet,AdminViewSet,create_admin,ContactViewSet,ClientTestimonialsViewSet,OurTeamViewSet,TeamTestimonialsViewSet,PartnersViewSet,OurTeamCareerViewSet


router = DefaultRouter()
router.register(r'blogs', BlogViewSet)
router.register(r'jobs', JobNotificationViewSet)
router.register(r'applications', JobApplicationViewSet)
router.register(r'admin', AdminViewSet)
router.register(r'contact', ContactViewSet)
router.register(r'Client-Testimonials', ClientTestimonialsViewSet)
router.register(r'Team-Testimonials', TeamTestimonialsViewSet)
router.register(r'OurTeam', OurTeamViewSet)
router.register(r'OurTeamCareer', OurTeamCareerViewSet)
router.register(r'Partners', PartnersViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api/admin/', create_admin),
    
]

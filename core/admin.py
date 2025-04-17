from django.contrib import admin
from .models import Blog, JobNotification,AdminUser,Contact,OurTeam,OurTeamCareer

admin.site.register(Blog)
admin.site.register(JobNotification)
admin.site.register(AdminUser)
admin.site.register(Contact)
admin.site.register(OurTeam)
admin.site.register(OurTeamCareer)

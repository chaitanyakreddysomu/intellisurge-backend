from django.db import models



class AdminUser(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email



class Blog(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(blank=True)
    content = models.TextField()
    image = models.FileField(upload_to='Blog_image/', blank=True, null=True,default='team_images/Logo_IntelliSurge_TM_No_BG.png')
    youtube_url = models.URLField(blank=True)     # Featured YouTube URL
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


JOB_TYPE_CHOICES = [
    ('Full-time', 'Full-time'),
    ('Part-time', 'Part-time'),
    ('Internship', 'Internship'),
    ('Contract', 'Contract'),
    ('Remote', 'Remote'),
]

class JobNotification(models.Model):
    job_title = models.CharField(max_length=255)
    department = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    job_type = models.CharField(max_length=50, choices=JOB_TYPE_CHOICES)
    salary_range = models.CharField(max_length=100, blank=True, null=True)
    job_description = models.TextField()
    requirements_qualifications = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.job_title} - {self.department}"


class JobApplication(models.Model):
    job = models.ForeignKey('JobNotification', on_delete=models.CASCADE, related_name='applications')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.job.job_title}"


class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    company = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)  # Removed choices, now plain text
    technologies = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.fullname

class ClientTestimonials(models.Model):
    author = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    stars = models.CharField(max_length=5)
    Content = models.CharField(max_length=255)

    def __str__(self):
        return self.author
    
    
   

class OurTeam(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.FileField(upload_to='team_images/', blank=False, null=False,default='team_images/Logo_IntelliSurge_TM_No_BG.png')

    def __str__(self):
        return f"{self.name}"




class OurTeamCareer(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.FileField(upload_to='team_images/', blank=False, null=False,default='team_images/Logo_IntelliSurge_TM_No_BG.png')
    # Content = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

class TeamTestimonials(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.FileField(upload_to='team_images/', blank=False, null=False,default='team_images/Logo_IntelliSurge_TM_No_BG.png')
    Content = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class OurPartners(models.Model):
    company = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    image = models.FileField(upload_to='partner_logos/', blank=False, null=False,default='team_images/Logo_IntelliSurge_TM_No_BG.png')

    def __str__(self):
        return f"{self.name}"

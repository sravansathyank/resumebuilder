from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    objective = models.TextField()
    skills = models.TextField()
    experience = models.TextField()
    education = models.TextField()
    projects = models.TextField()
    extracurricular_activities = models.TextField()

    def __str__(self):
        return f"Resume of {self.full_name}"

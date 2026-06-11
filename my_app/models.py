from django.db import models
# Users
from django.contrib.auth.models import User

# Projects
class Project(models.Model):
    STATUS_CHOICES = [
        ("planning", "Planning"),
        ("active", "Active"),
        ("completed", "Completed"),
        ("archived", "Archived"),
    ]
    
    name = models.CharField(max_length= 200)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length = 20,
        choices= STATUS_CHOICES,
        default = "planning"
    )
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.name
    
# Experiments

# Samples

# Tasks

# Quality Control Review

# Audit Logs

from django.db import models
from users.models import User

class Artist(models.Model) :
    stage_name = models.CharField(max_length = 20)
    social_link = models.URLField(max_length = 200)
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True)

    def __str__(self) :
        return self.stage_name       

from autoslug import AutoSlugField
from django.db import models

# Create your models here.
class Service(models.Model):
    service_icon = models.CharField(max_length=50)
    service_title = models.CharField(max_length=50)
    service_desc = models.TextField()
    service_slug = AutoSlugField(populate_from='service_title', unique=True, null=True, default=None)
    
    def __str__(self) -> str:
        return f"{self.service_title}\n {self.service_desc[:30]}\n"
    

    

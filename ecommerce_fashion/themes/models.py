from django.db import models

# theams models

class Sitesetting(models.Model):
    image=models.ImageField(upload_to='media/site')
    caption=models.TextField()
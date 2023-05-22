from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    birthday = models.DateField(null=True,blank=True)
    country = models.CharField(max_length=30,null=True,blank=True)
    about = models.TextField(null=True,blank=True)
    img = models.ImageField(default='profile_icons/user_default_new.jpg',upload_to='profile_icons')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
        try:
            image = Image.open(self.img.path)

            if image.height > 350 or image.width >350:
                new_sizes = (350, 350)
                image.thumbnail(new_sizes)
                image.save(self.img.path)
        except Exception as e:
            print(e)


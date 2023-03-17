from django.db import models
from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from django.core.files.storage import default_storage as storage
from storages.backends.s3boto3 import S3Boto3Storage


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(storage=S3Boto3Storage(), default='./media/default.png', upload_to='media/profile_images', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        image_read = storage.open(self.profile_image.name, "rb")
        img = Image.open(image_read)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            # img.save(self.profile_image.name, force_insert=True)
            img.save(image_read, force_insert=True)
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(
        default='default.png', upload_to='profile_images/', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
      
    # Resize the image when a user upload
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.profile_image.path)  # Open image

        # resize image
        if img.height > 300 or img.width > 400:
            output_size = (400, 300)
            img.thumbnail(output_size)  # Resize image
            # Save it again and override the larger image
            img.save(self.profile_image.path)

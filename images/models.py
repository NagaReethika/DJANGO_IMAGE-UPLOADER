import os
from django.db import models
from django.utils import timezone

def unique_upload_path(instance, filename):
    """
    Generates a secure chronological folder path pattern for user uploads.
    Renames the file to prevent duplicate names from overwriting one another.
    """
    ext = filename.split('.')[-1]
    time_prefix = timezone.now().strftime('%H%M%S')
    clean_name = f"{time_prefix}_{instance.title.replace(' ', '_')}.{ext}"
    return os.path.join('uploads', timezone.now().strftime('%Y/%m/%d'), clean_name)

class UploadedImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to=unique_upload_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at'] # Displays newer uploads at the top of the feed

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        """
        Removes the actual graphic asset from disk storage space
        when its database record row is deleted.
        """
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)
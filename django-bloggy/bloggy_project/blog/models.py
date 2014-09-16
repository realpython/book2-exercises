from django.db import models

from uuslug import uuslug


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    tag = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    views = models.IntegerField(default=0)
    slug = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self, separator="_") # optional non-dash separator
        self.slug = uuslug(self.title, instance=self, max_length=40)
        super(Post, self).save(*args, **kwargs)

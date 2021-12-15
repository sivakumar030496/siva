from django.db import models

class Quotes(models.Model):
    title = models.CharField(max_length=50)
    likes = models.PositiveIntegerField(default=0)

    def __dir__(self):
        return self.title
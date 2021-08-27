from django.db import models

class HompageModel(models.Model):
    caption = models.CharField(max_length=255, blank=True, null=True)
    sub_caption = models.TextField( blank=True, null=True)

    def __str__(self):
        return self.caption

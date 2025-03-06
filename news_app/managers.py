from django.db import models

class PublishedManager(models.Manager):
    def get_queryset(self):
        from news_app.models import News
        return super().get_queryset().filter(status = News.Status.Published)
    

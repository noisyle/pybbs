from django.db import models

# Create your models here.
class Thread(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(upload_to="bbs/%Y/%m/%d",null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.title

class Comment(models.Model):
    thread = models.ForeignKey(Thread)
    content = models.TextField()
    image = models.ImageField(upload_to="bbs/%Y/%m/%d",null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

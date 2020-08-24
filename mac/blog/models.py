from django.db import models

# Create your models here.
class Blogpost(models.Model):
    post_id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    mainhead= models.CharField(max_length=500,default="")
    cmainhead= models.CharField(max_length=5000,default="")
    head= models.CharField(max_length=500,default="")
    chead= models.CharField(max_length=5000,default="")
    subhead= models.CharField(max_length=500,default="")
    csubhead= models.CharField(max_length=5000,default="")
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to="blog/images", default="")

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
class Blogpost(models.Model) :
    post_id = models.AutoField(primary_key=True)
    Title= models.CharField(max_length=80)
    head0 = models.CharField(max_length=500,default="")
    chead0 = models.CharField(max_length=50000,default="")
    head1 = models.CharField(max_length=500,default="")
    chead1 = models.CharField(max_length=50000,default="")
    head2 = models.CharField(max_length=500,default="")
    chead2 = models.CharField(max_length=50000,default="")
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to ='shop/images', default="")

    def __str__(self) :
        return self.Title
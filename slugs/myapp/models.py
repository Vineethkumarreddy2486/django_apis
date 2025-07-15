from django.db import models
from django.utils.text import slugify
# Create your models here.

class Slug(models.Model):
    title = models.CharField(max_length=100)
    desc=models.TextField()
    slug=models.SlugField(unique=True,blank=True)

# slug is a short label used in URLs which helps to make the URLs easy to understand
# this code says, slug is created when the slug is empty, even if we update the title value slug remains same
                # if we want to change the slug automatically after changing the title then the code is 
        #                     def save(self,*args,**kwargs):
        #                     self.slug=slugify(self.title)        # Always update slug from title
        #                     super().save(*args,**kwargs)


    def save(self,*args,**kwargs):
        if not self.slug:                         #This means the slug is only created when it's empty.
            self.slug=slugify(self.title)        
        super().save(*args,**kwargs)

    def __str__(self):
        return self.title
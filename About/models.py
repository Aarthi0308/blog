from django.db import models

class About(models.Model):
    about_heading=models.CharField(max_length=25)
    about_descrription=models.TextField(max_length=250)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
            verbose_name_plural='About'


    def __str__(self):
         return self.about_heading
class sociallinks(models.Model):
      platform=models.CharField(max_length=25)
      link=models.URLField(max_length=100)
      created_at=models.DateTimeField(auto_now_add=True)
      updated_at=models.DateTimeField(auto_now=True)
      def __str__(self):
               return self.platform
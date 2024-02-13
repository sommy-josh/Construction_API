from django.db import models

class GetQUote(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50, unique=True)
    phone=models.CharField(max_length=20)
    message=models.TextField()
    
    def __str__(self):
        return self.name


class Contact(models.Model):
    your_name=models.CharField(max_length=50)
    your_email=models.EmailField(max_length=50)
    subject=models.CharField(max_length=50)
    message=models.TextField()
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)

    def __str__(self):
        return self.your_email

class Home(models.Model):
    product=models.CharField(max_length=200, default=None, null=True)
    image=models.ImageField(upload_to='project_images/', )
    
  
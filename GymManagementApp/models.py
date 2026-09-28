from django.db import models

# Create your models here.
class MembershipPlan(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    duration=models.CharField(max_length=50)
    description=models.TextField()
    features=models.TextField()
    is_popular=models.BooleanField(default=False)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

# services
class Service(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    icon=models.CharField(max_length=100,blank=True)
    image=models.ImageField(upload_to='services/',blank=True,null=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name



# trainer
class Trainer(models.Model):
    name=models.CharField(max_length=100)
    specialization=models.CharField(max_length=150)
    experience=models.PositiveIntegerField()
    bio=models.TextField()
    image=models.ImageField(upload_to='trainers/',blank=True,null=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name
# contact
class ContactMessage(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    message=models.TextField()
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

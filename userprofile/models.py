from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	fullname=models.CharField(max_length=255,null=True)
	contact= models.CharField(max_length=100,null=True)
	address=models.CharField(max_length=200,null=True)

	class Meta:
		verbose_name_plural='Profile'
		
	def __str__(self):
		return self.user.username


	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)
# ############

@receiver(post_save,sender=User)
def update_profile(sender,instance,created,**kwargs):
	if created:
		Profile.objects.create(user=instance)
		instance.profile.save()
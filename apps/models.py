from django.db import models

# Create your models here.
class Publication(models.Model):
	name=models.CharField(max_length=200)
	address=models.TextField()
	contact=models.CharField(max_length=200)
	active=models.BooleanField(default=True)

	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)

	def __str__(self):
		return self.name




class Book(models.Model):
	name=models.CharField(max_length=200)
	isbn=models.CharField(max_length=100,blank=True,null=True)
	price=models.CharField(max_length=100,blank=True,null=True)
	created=models.DateTimeField(auto_now_add=True) ## create but not editable 
	modified=models.DateTimeField(auto_now=True)  ## create and also editable
	published_by=models.ForeignKey(Publication,on_delete=models.CASCADE,null=True)

	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)

	def __str__(self):
		return self.name


# One to One relationship
# One to Many relationship
# Many to Many relationship


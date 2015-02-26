from django.db import models

# Create your models here.

class Posts(models.Model):
	title = models.CharField(max_length = 30)
	body = models.TextField()
	pub_date = models.DateTimeField('Date Published')

	def __unicode__(self):
		return self.title

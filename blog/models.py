from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from m.models import viewers
from django.urls import reverse

class posts(models.Model) :
    title = models.CharField(max_length = 20)
    content = models.TextField(max_length=1000)
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    viewer = models.ManyToManyField(viewers)
    def __str__(self):
        return 'this is posted on:'+ str(self.date_posted)+'by'+str(self.author)
    def get_absolute_url(self):
    	return reverse('post-detail',kwargs={'pk':self.pk})
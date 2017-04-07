from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
	#post = Post(id_post = 1, title = "bla", content = "bla bla bla", tags="#bla",created_time='2017-04-06',author_id=3) 
    id_post = models.IntegerField()
    author_id = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length = 25, blank = False, default = '')
    content = models.TextField()
    tags = models.TextField()
    create_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now_add = True)
    # author_id = models.ForeignKey(User, related_name = 'user', on_delete = models.CASCADE)
    author_id = models.IntegerField()
    class Meta:
     # managed = False
      db_table = 'shmoterapp_post'

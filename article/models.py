from django.db import models
# import built-in user model
from django.contrib.auth.models import User
# timezone, to handle time-related matter
from django.utils import timezone

# Blog post data model

class ArticlePost(models.Model):
    # Author of the article, which has a parameter on_delete to specify the method of data deletion
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Title of the article
    title = models.CharField(max_length=100)
    # Article Body
    body = models.TextField()
    # Creation time
    createdAt = models.DateTimeField(default=timezone.now)
    # Updated Time
    updatedAt = models.DateTimeField(auto_now = True)
    
    # Class meta is ued to define the meta data
    # class Meta:
    #     # order data of model from latest to oldest
    #     ordering = ('-created,')

    # Function defines the return value content when calling the str() method of the object
    def __str__(self):
        # return title of the article
        return self.title
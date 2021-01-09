from django.db import models


class Article(models.Model):
    author = models.EmailField(max_length=100)  # Who created this article
    title = models.CharField(max_length=100)  # Title of the article
    body = models.CharField(max_length=5000)  # Content of the article
    date = models.DateTimeField('date published')  # Date when the article was published


class Comment(models.Model):
    author = models.EmailField(max_length=100)  # Who left this comment
    body = models.CharField(max_length=400)  # Comment body
    date = models.DateTimeField('date commented')  # Date when the comment was written

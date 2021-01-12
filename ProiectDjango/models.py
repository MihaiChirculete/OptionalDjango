from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.db import models


class PublishedArticleManager(models.Manager):
    def get_queryset(self):
        return super(PublishedArticleManager, self).get_queryset().filter(status='published')


class Article(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'),
                      ('published', 'Published'))
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_articles')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    @property
    def article_id(self):
        return self.id

    # Sort results by the publishing date
    # (descending order)
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    objects = models.Manager()  # The default manager
    published = PublishedArticleManager()  # Custom manager defined above

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day, self.slug])


class Comment(models.Model):
    article_id = models.PositiveIntegerField(default=0)  # Parent article of this comment
    author = models.EmailField(max_length=100)  # Who left this comment
    body = models.CharField(max_length=400)  # Comment body
    date = models.DateTimeField('date commented')  # Date when the comment was written

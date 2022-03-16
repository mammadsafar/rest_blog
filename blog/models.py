from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
# class postManager(models.Manager):
#     def Y(self, year):
#         return self.filter(publish__year=year)

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)  # VARCHAR
    slug = models.CharField(max_length=250, unique_for_date='publish')  # اگه دو نفر همزمان باهم بخوان اسلاگی بسازند بر اساس زمانشون اونارو یونسک میکنه که اسلاگ مشابهی نداشته باشن
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')  # برای درج کردن کاربر در جدول کاربران از کلاس User استفاده میکنیم | اگه یوزر پاک شد پستاشم پاک بشه |
    body = models.TextField()  # TEXT
    publish = models.DateTimeField(default=timezone.now)  # DATETIME
    created = models.DateTimeField(auto_now_add=True)  # DATETIME
    updated = models.DateTimeField(auto_now=True)  # DATETIME
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')  # VARCHAR
    # objects = postManager()
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # اگه از کلاس postManager استفاده میکنیم از objects استفاده نمیشه

    class Meta:
        ordering = ('-publish',)

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

    def __str__(self):
        return self.title

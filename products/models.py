from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("product_detail", args=[self.id])
    

class CustomManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)

class Comment(models.Model):
    STARS_CHOICES = [('1', 'Very Bad'), ('2', 'Bad'), ('3', 'Normal'), ('4', 'Good'), ('5', 'Very Good')]
    
    text = models.TextField(verbose_name=_('Comment Text'))
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modifed = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    stars = models.CharField(choices=STARS_CHOICES, max_length=10, blank=True, verbose_name=_('Stars'))

    def __str__(self):
        return self.text
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])
    
    objects = models.Manager()
    active_posts = CustomManger()
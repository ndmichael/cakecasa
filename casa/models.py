from django.db import models
from django.urls import reverse

# Create your models here.


class CakeCategory(models.Model):
    name = models.CharField(max_length=200, db_index=True, default="standard")
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse('casa:cake_list_by_category', args=[self.slug])


class CakeProduct(models.Model):
    cake_category = models.ForeignKey(CakeCategory, related_name='products', on_delete=models.CASCADE)
    cake_name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', default="category_default.jpg",  blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('cake_name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return f"{self.cake_name}"

    # def get_absolute_url(self):
    #     return reverse('casa:cake_list_by_category', args=[self.id, self.slug])

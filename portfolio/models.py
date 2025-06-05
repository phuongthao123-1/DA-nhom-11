from django.db import models
from django.utils.text import slugify

class PortfolioCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Danh mục portfolio'

class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField()
    category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE, related_name='items')
    thumbnail = models.ImageField(upload_to='portfolio/')
    client = models.CharField(max_length=100, blank=True)
    completion_date = models.DateField()
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Portfolio'
        ordering = ['-created_at']

class PortfolioImage(models.Model):
    portfolio_item = models.ForeignKey(PortfolioItem, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='portfolio/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"Hình ảnh cho {self.portfolio_item.title}"
    
    class Meta:
        ordering = ['order']

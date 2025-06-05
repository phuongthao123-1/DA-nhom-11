from django.db import models

# Create your models here.

class Biography(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Tiểu sử'

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.institution
    
    class Meta:
        verbose_name_plural = 'Học vấn'
        ordering = ['-end_date']

class WorkExperience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.position} tại {self.company}"
    
    class Meta:
        verbose_name_plural = 'Kinh nghiệm làm việc'
        ordering = ['-end_date']

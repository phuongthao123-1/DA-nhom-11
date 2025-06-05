from django.db import models

# Create your models here.

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Danh mục kỹ năng'
        ordering = ['order']

class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    level = models.IntegerField(choices=[(i, f"{i*10}%") for i in range(1, 11)], default=5)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True, help_text="Font Awesome icon class")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Kỹ năng'
        ordering = ['-level', 'name']

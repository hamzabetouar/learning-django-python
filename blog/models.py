from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)
    category = models.ForeignKey('category', on_delete=models.CASCADE)
    tags = models.ManyToManyField ('tag')

    def __str__(self):
        return self.title;

    def tags_text(self):
        tags = []
        for tag in self.tags.all():
            tags.append(tag.value.upper());
        return ', '.join(tags)

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title;

    class Meta:
        verbose_name_plural = 'Categories'

class Tag(models.Model):
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.value;
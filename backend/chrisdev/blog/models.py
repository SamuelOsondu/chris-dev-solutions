from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="states")

    def __str__(self):
        return f"{self.name}, {self.country.name}"


class Tribe(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="tribes")

    def __str__(self):
        return f"{self.name}, {self.state.name}"


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to='blogs')
    content = CKEditor5Field('Text', config_name='extends')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="blogs")
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="blogs")
    tribe = models.ForeignKey(Tribe, on_delete=models.CASCADE, related_name="blogs")

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="comments")
    author_name = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author_name} on {self.blog_post.title}"

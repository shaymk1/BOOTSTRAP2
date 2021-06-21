from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce.models import HTMLField

# Create your models here.


class Quotes(models.Model):
    quotes = models.TextField()
    quote_by = models.CharField(max_length=100)


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title





class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = HTMLField()
    # view_count = models.IntegerField(default=0)
    # comment_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    slug = models.SlugField(unique=True, db_index=True, null=True)
    featured = models.BooleanField()
    slug = models.SlugField(unique=True, db_index=True)
    tags = models.ManyToManyField(Tag)
    previous_post = models.ForeignKey(
        'self', related_name="previous", on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey(
        'self', related_name="next", on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('post_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('post_delete', kwargs={'pk': self.pk})
    
    #for the comments
    @property
    def get_comments(self):
            return self.comments.all().order_by('-timestamp')
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True)
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE) #related name allows us to call this comments from a post model

    def __str__(self):
        return self.user.username

    # user_name = models.CharField(max_length=200)
    # user_email = models.EmailField()
    # text = models.TextField(max_length=1000)
    # post = models.ForeignKey(
    #     Post, on_delete=models.CASCADE, related_name="comments")


class Signup(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

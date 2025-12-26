import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django_extensions.db.models import ActivatorModel, TimeStampedModel
from global_data.enum import UserStatus, UserRole, BlogStatus, CommentStatus, CategoryStatus

class BlogBaseModel(ActivatorModel, TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    meta = models.JSONField(default=dict, blank=True)

    class Meta:
        abstract = True

class User(AbstractUser, BlogBaseModel):
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.READER
    )
    account_status = models.CharField(
        max_length=20,
        choices=UserStatus.choices,
        default=UserStatus.ACTIVE
    )
    # Profile fields
    bio = models.TextField(blank=True, verbose_name="Bio / About")
    website = models.URLField(blank=True, verbose_name="Website")
    location = models.CharField(max_length=100, blank=True, verbose_name="Location")
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name="Profile Photo")
    
    # Social Links
    twitter_username = models.CharField(max_length=50, blank=True, verbose_name="Twitter Username")
    linkedin_url = models.URLField(blank=True, verbose_name="LinkedIn URL")
    github_username = models.CharField(max_length=50, blank=True, verbose_name="GitHub Username")

    def __str__(self):
        return self.username

class Category(BlogBaseModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=CategoryStatus.choices,
        default=CategoryStatus.ACTIVE
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Article(BlogBaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    image = models.ImageField(upload_to='articles', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='articles')
    status = models.CharField(
        max_length=20,
        choices=BlogStatus.choices,
        default=BlogStatus.DRAFT
    )
    views = models.PositiveIntegerField(default=0)
    featured = models.BooleanField(default=False)
    newsletter_feature = models.BooleanField(default=False)
    allow_comments = models.BooleanField(default=True)
    tags = models.CharField(max_length=200, blank=True, help_text="Comma separated tags")

    def __str__(self):
        return self.name

class Comment(BlogBaseModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=CommentStatus.choices,
        default=CommentStatus.PENDING
    )
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Comment by {self.author} on {self.article}"
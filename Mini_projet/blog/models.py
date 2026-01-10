import uuid
from datetime import datetime
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
    icon = models.CharField(max_length=50, default='fa-folder', blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
from django.utils.text import slugify

class Article(BlogBaseModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, blank=True)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    image = models.ImageField(upload_to='articles', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='articles')
    status = models.CharField(
        max_length=20,
        choices=BlogStatus.choices,
        default=BlogStatus.DRAFT
    )
    date = models.DateTimeField(default=datetime.now)
    views = models.PositiveIntegerField(default=0)
    featured = models.BooleanField(default=False)
    newsletter_feature = models.BooleanField(default=False)
    allow_comments = models.BooleanField(default=True)
    tags = models.CharField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
from django.contrib.auth import get_user_model

User = get_user_model()

class Comment(BlogBaseModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=CommentStatus.choices,
        default=CommentStatus.PENDING
    )
    liked_by = models.ManyToManyField(User, blank=True, related_name='liked_comments')

    @property
    def likes_count(self):
        return self.liked_by.count()

    def __str__(self):
        return f"Comment by {self.author} on {self.article}"
    
    
    
    
    
class ContactMessage(models.Model):

    SUBJECT_CHOICES = [
        ('general', 'Demande Générale'),
        ('submission', "Soumission d'Article"),
        ('partnership', 'Opportunité de Partenariat'),
        ('technical', 'Support Technique'),
        ('feedback', 'Commentaires & Suggestions'),
        ('other', 'Autre'),
    ]

    name = models.CharField(
        max_length=150,
        verbose_name="Nom"
    )

    email = models.EmailField(
        verbose_name="Adresse email"
    )

    subject = models.CharField(
        max_length=20,
        choices=SUBJECT_CHOICES,
        verbose_name="Sujet"
    )

    message = models.TextField(
        verbose_name="Message"
    )

    newsletter = models.BooleanField(
        default=False,
        verbose_name="Abonné à la newsletter"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date d'envoi"
    )

    is_read = models.BooleanField(
        default=False,
        verbose_name="Lu"
    )

    class Meta:
        verbose_name = "Message de contact"
        verbose_name_plural = "Messages de contact"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"

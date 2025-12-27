from django.db import models
from django.utils.translation import gettext_lazy as _

class UserStatus(models.TextChoices):
    ACTIVE = 'active', _('Active')
    INACTIVE = 'inactive', _('Inactive')
    SUSPENDED = 'suspended', _('Suspended')

class UserRole(models.TextChoices):
    ADMIN = 'admin', _('Admin')
    AUTHOR = 'author', _('Author')
    READER = 'reader', _('Reader')

class BlogStatus(models.TextChoices):
    DRAFT = 'draft', _('Draft')
    PUBLISHED = 'published', _('Published')
    PENDING = 'pending', _('Pending Review')

class CommentStatus(models.TextChoices):
    APPROVED = 'approved', _('Approved')
    SPAM = 'spam', _('Spam')
    REPORTED = 'reported', _('Reported')
    PENDING = 'pending', _('Pending')

class CategoryStatus(models.TextChoices):
    ACTIVE = 'active', _('Active')
    INACTIVE = 'inactive', _('Inactive')

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.managers import SHUserManager


class SHUser(AbstractUser):
    objects = SHUserManager()
    username = None
    email = models.EmailField(
        _("Email address"),
        unique=True,
        error_messages={
            "unique": _("This email address is already in use.")
        },
    )
    first_name = models.CharField(_("First name"), max_length=50)
    last_name = models.CharField(_("Last name"), max_length=50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

from django.contrib.auth.models import (AbstractBaseUser, AbstractUser,
                                        BaseUserManager, PermissionsMixin)
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self, username, password, email, **kwargs):
        if not username:
            raise ValueError("请输入用户名")
        if not password:
            password = "111111"
        user = self.model(username=username, email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, password, email, **kwargs):
        kwargs["is_superuser"] = False
        return self._create_user(username, password, email, **kwargs)

    def create_superuser(self, username, password, email, **kwargs):
        kwargs["is_superuser"] = True
        kwargs["is_staff"] = True
        return self._create_user(username, password, email, **kwargs)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=128, verbose_name="借书人", unique=True)
    email = models.EmailField(verbose_name="邮箱", blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=True,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    EMAIL_FIELD = 'email'

    objects = UserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, auth_user=None, auth_password=None, **kwargs):
        """
        Easy wrapper for sending a single message to a recipient list. All members
        of the recipient list will see the other recipients in the 'To' field.

        If auth_user is None, use the EMAIL_HOST_USER setting.
        If auth_password is None, use the EMAIL_HOST_PASSWORD setting.

        Note: The API for this method is frozen. New code wanting to extend the
        functionality should use the EmailMessage class directly.
        """
        send_mail(subject, message, from_email, [self.email], auth_user, auth_password, **kwargs)

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    

class Book(models.Model):
    """定义书籍属性"""
    name = models.CharField(max_length=512, verbose_name="书名")
    author = models.CharField(max_length=512, verbose_name="作者")
    reader = models.ForeignKey(User, related_name="reader", on_delete=models.SET_NULL, null=True, blank=True, default="", verbose_name="借书人")
    borrow_date = models.DateField(null=True, blank=True, verbose_name="借书时间")
    return_date = models.DateField(null=True, blank=True, verbose_name="还书时间")
    reminder = models.BooleanField(default=True, verbose_name="到期发送提醒")
    desc = models.TextField(blank=True, default="", verbose_name="备注")

    class Meta:
        verbose_name = '书籍管理'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name

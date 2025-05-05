from django.contrib.auth.models import AbstractUser, Permission, Group
from django.contrib.gis.db import models

class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='group',  # Укажите имя, чтобы избежать конфликта
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='permission',  # Укажите имя, чтобы избежать конфликта
        blank=True,
    )
    date_birth = models.DateField(null=True, blank=True)
    number_phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.username

class Location(models.Model):
    name_location = models.CharField(max_length=200)
    address = models.TextField()
    is_exit = models.BooleanField(default=False)  # Для разделения локаций на объекты и выезды

    def __str__(self):
        return self.name_location


class Mark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='marks')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='marks')
    photo_in = models.ImageField(upload_to='photos_in/', null=True, blank=True)
    photo_out = models.ImageField(upload_to='photos_out/', null=True, blank=True)
    geo_in = models.PointField(null=True, blank=True)
    geo_out = models.PointField(null=True, blank=True)
    time_in = models.DateTimeField()
    time_out = models.DateTimeField(null=True, blank=True)

    def duration(self):
        if self.time_out:
            return self.time_out - self.time_in
        return None

    def __str__(self):
        return f"{self.user.username} - {self.location.name_location} - {self.time_in.date()}"
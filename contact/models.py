from django.db import models


class Contact(models.Model):
    """Рассылка"""
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
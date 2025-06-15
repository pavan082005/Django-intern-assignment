from django.db import models

class TelegramUser(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    joined_at = models.DateTimeField(auto_now_add=True)  # <== Add this

    def __str__(self):
        return f"{self.username} ({self.telegram_id})"

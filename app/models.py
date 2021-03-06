from django.db import models

class product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name
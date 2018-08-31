from django.db import models


# Account model.
class Account(models.Model):
    # Fields
    name = models.CharField(max_length=128)
    parent = models.ForeignKey("self", null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    # Methods
    def __str__(self):
        return self.name

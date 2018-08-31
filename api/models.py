from django.db import models


# Account model.
class Account(models.Model):
    # Fields
    name = models.CharField(max_length=128)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True
    )

    # Methods
    def __str__(self):
        return self.name

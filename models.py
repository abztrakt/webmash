from django.db import models

class Artifact(models.Model):
    """ Base class for digital artifacts of all kinds.
    """
    children = models.ManyToManyField("self", blank=True)

class LocalText(Artifact):
    """ A text artifact stored locally.
    """
    text = models.TextField()

from django.db import models

class Artifact(models.Model):
    """ Base class for digital artifacts of all kinds.
    """
    title = models.CharField(max_length=256)


class Container(models.Model):
    """ Class to act as a parent container which can hold many artifacts and store their order.
    """
    title = models.CharField(max_length=256)
    related_artifact = models.ManyToManyField(Artifact, blank=True)
    related_container = models.ManyToManyField('self', blank=True)


class LocalText(Artifact):
    """ A text artifact stored locally.
    """
    text = models.TextField()

from django.db import models

class Base(models.Model):
    """ Base class for all other models. This exists primarily so that Artifacts and Containser can be imported as peers.
    """
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class Artifact(Base):
    """ Base class for digital artifacts of all kinds.
    """
    pass


class Container(Base):
    """ Class to act as a parent container which can hold many artifacts and store their order.
    """
    related_items = models.ManyToManyField(Base, related_name='related_items', blank=True)


class LocalText(Artifact):
    """ A text artifact stored locally.
    """
    text = models.TextField()

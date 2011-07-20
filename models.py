from django.db import models
from django.template.loader import render_to_string
from polymorphic.models import *

# start Base classes

class Base(models.Model):
    """ Base class for all other models. This exists primarily so that Artifacts and Container can be imported as peers.
    """
    title = models.CharField(max_length=256)
    slug = models.SlugField()
    __metaclass__ = PolymorphicMetaclass

    def get_classname(self):
        return self.__class__.__name__
    
    def to_html_template(self):
        """ THIS METHOD IS NOW DEPRECATED
        """
        return render_to_string("%s.html" % self.get_classname(), {'self':self,})

    def __str__(self):
        return self.title

class Artifact(Base):
    """ Base class for digital artifacts of all kinds.
    """
    pass

class Container(Base):
    """ Base class for objects which can hold many artifacts and store their order.
    """
    related_items = models.ManyToManyField(Base, related_name='related_items', blank=True)

# end Base classes


class Folder(Container):
    """ Folders hold any number of objects and an order in which to display them.
    TODO: Provide a pager that can be used to go prev/next between objects.
    """
    __metaclass__ = DowncastMetaclass

class Page(Container):
    """ Pages hold any number of artifacts and a layout.
    """
    __metaclass__ = DowncastMetaclass

class LocalText(Artifact):
    """ A text artifact stored locally.
    """
    text = models.TextField()
    __metaclass__ = DowncastMetaclass

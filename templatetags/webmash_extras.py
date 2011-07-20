from django import template
from webmash.models import *

register = template.Library()

class TemplatedObjectNode(template.Node):
    """ Builds the node for a templated object. Templated objects should have a model and a template that matches <Classname>.html
    """
    def __init__(self, obj):
        self.obj = obj
        self.children = []
        try:
            for a in obj.related_items.values():
                self.children.append(Base.objects.get(id=a['id']).downcast())
        except obj.DoesNotExist:
            pass
    def render(self, context):
        return render_to_string("%s.html" % self.obj.get_classname(), {'self':self.obj, 'children':self.children,})

@register.simple_tag(takes_context=True)
def templated_object(context, token):
    """ Return a template node for a templated object. Called as a template tag.
    """
    return TemplatedObjectNode(token)

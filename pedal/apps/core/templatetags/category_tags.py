from django import template

from ..models import Category

register = template.Library()


@register.tag(name="category_list")
def do_category_list(parser, token):
    tokens = token.split_contents()
    error_msg = ("%r tag uses the following syntax: {%% category_list as categories %%}" % tokens[0])
    if tokens[1] != 'as':
        raise template.TemplateSyntaxError(error_msg)
    as_var = tokens[2]
    return CategoryTreeNode(as_var)


class CategoryTreeNode(template.Node):

    def __init__(self, as_var):
        self.as_var = as_var

    def render(self, context):
        context[self.as_var] = Category.objects.all().values().order_by('order')
        return ''

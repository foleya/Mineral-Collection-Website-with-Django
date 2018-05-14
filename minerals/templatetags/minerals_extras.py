from django import template


register = template.Library()


@register.filter('remove_underscores')
def remove_underscores(text):
    return text.replace('_', ' ')


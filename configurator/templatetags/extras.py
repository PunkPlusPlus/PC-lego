from django import template

register = template.Library()


@register.filter()
def my_range(number):
    return range(1, number + 1)
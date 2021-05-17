from django import template

register = template.Library()

@register.filter
def custom_format(value):
	return value.strftime('%b %d, %Y, %H:%M:%S')
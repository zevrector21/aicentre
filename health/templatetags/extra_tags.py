from django import template

register = template.Library()

@register.filter
def wrap_path(value, arg):
	return f"https://{arg}/static{value.replace('/media', '')}"

@register.filter
def wrap_temp(value):
	return round(float(value), 2)

@register.filter
def wrap_domain(value):
	if value == '/':
		return value
	return f'https://{value}'
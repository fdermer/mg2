# -*- coding: utf-8 -*-


from django import template

register = template.Library()

@register.inclusion_tag('recipe/details/_ingredients.html')
def recipe_ingredients(ingredient_list):
    return {
        "ingredient_list": ingredient_list,
    }

@register.inclusion_tag('recipe/details/_steps.html')
def recipe_steps(step_list):
    return {
        "step_list": step_list,
    }







#@register.filter()
#def french_weekday(value):
#    return settings.FRENCH_WEEKDAYS[value]
#
#
#@register.filter
#def bill_value(value):
#    if value:
#        value = str(value / float(100))
#        value = value.replace(".", ",")
#        valArray = value.split(",")
#        if len(valArray) == 2:
#            try:
#                decimals = int(valArray[1])
#                if not decimals:
#                    value = valArray[0]
#            except Exception:
#                pass
#    else:
#        value = 0
#    return value
#
#
#
#
#@register.inclusion_tag('smartmail/buttons/email_button_small_green.html')
#def email_button_small_green (href, anchor, title, mso_width):
#    return {
#        "href": href,
#        "anchor": anchor,
#        "title": title,
#        "mso_width": mso_width,
#    }
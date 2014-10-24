#!/usr/bin/env python
# -*- coding: utf-8 -*-


#To install slugify:
# (venv)$ pip install python-slug


from recipe.models import Recipe
from slugify import slugify

for recipe in Recipe.objects.all():
    if recipe.image_name:
        slug = recipe.image_name.split(".")
        slug = slugify(slug[0]) + "." + slugify(slug[1])
        recipe.image_slug = slug
        recipe.save()
        print recipe.image_slug
#!/usr/bin/env python
# -*- coding: utf-8 -*-


from recipe.models import Recipe
import os

root_dir = "/Users/Fred/www/mg2/mg2/recipe/static/"
count = 0

for recipe in Recipe.objects.all():
    if recipe.image_slug and recipe.image_name:
        if os.path.exists(os.path.join(root_dir, recipe.get_image_url())):
            count +=1
            print "http://127.0.0.1:8000/static/" + recipe.get_image_url()


print "Nb de photos trouvées: ", count
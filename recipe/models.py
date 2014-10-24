# -*- coding: utf-8 -*-

from django.db import models
import hashlib, string, re, os

class Recipe(models.Model):
    id = models.IntegerField(default=None, null=False, blank=False, primary_key=True)
    enabled = models.BooleanField(default=False)
    lang = models.CharField(max_length=5, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    chef_name = models.CharField(max_length=255, null=True, blank=True)
    courses = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    serving = models.IntegerField(default=None, null=True, blank=True)
    price = models.IntegerField(default=None, null=True, blank=True)
    difficulty = models.IntegerField(default=None, null=True, blank=True)
    for_children = models.BooleanField(default=False)
    light = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    selection = models.BooleanField(default=False)
    note = models.FloatField(default=0, null=True, blank=True)
    quality = models.IntegerField(default=None, null=True, blank=True)
    theme = models.CharField(max_length=255, null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)
    ugc_ingredients = models.TextField(null=True, blank=True)
    steps = models.TextField(null=True, blank=True)
    prep_time = models.IntegerField(default=None, null=True, blank=True)
    pause_time = models.IntegerField(default=None, null=True, blank=True)
    cooking_time = models.IntegerField(default=None, null=True, blank=True)
    total_time = models.IntegerField(default=None, null=True, blank=True)
    image_name = models.TextField(null=True, blank=True)
    image_slug = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_image_url(self):
        if self.image_slug and self.image_name:
            url = "recettes/"+hashlib.md5(self.image_name.encode('utf-8')).hexdigest()[:1]+"/"+self.image_slug

            # TODO: gérer proprement les recettes sans photos. Avec le chemin en dur, ça ne risque pas de marcher.
            # Mettre un chemin dans les local settings ?
            # Ou alors, MAJ la base pour ajouter un champ: "j'ai la photo ou pas". cf ./manage.py count_recipes_with_photos

            root_dir = "/Users/Fred/www/mg2/mg2/recipe/static/"

            if os.path.exists(os.path.join(root_dir, url)):
                return url
            else:
                return "images/recette_default.jpg"
        else:
            return "images/recette_default.jpg"

    def get_ingredients(self):
        #import pdb;pdb.set_trace()
        if len(self.ingredients) > 15:
            # Replace the separator in the ingredient list
            sep = "§".decode('utf-8')
            #ingredient_list = string.replace(ingredient_list, sep+"g","g")
            #ingredient_list = string.replace(ingredient_list, sep+"l","l")
            ingredient_list = string.replace(self.ingredients, sep,";")
            ingredient_list = re.sub(";(;)*",";",ingredient_list) #Delete multiple ";"
            ingredient_list = ingredient_list.split(";")
            #Todo Gérer le cas d'une chaine qui commence par un séparateur <=> élément vide, ex recettes 25861
            #Todo Idem dans le cas Ingrédient UGC
            return ingredient_list
        else:
            sep = "•".decode('utf-8')
            ingredient_list = re.sub(sep+"( )*","",self.ugc_ingredients)
            return ingredient_list.split('\\r\\n')


    def get_steps(self):
        # Replace the separator in the ingredient list
        sep = "§".decode('utf-8')
        step_list = self.steps.split(sep)
        return step_list

    def get_difficulty(self):
        if self.difficulty == 1:
            return "très facile"
        elif self.difficulty == 2:
            return "facile"
        else:
            return "moyenne"
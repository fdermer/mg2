# -*- coding: utf-8 -*-

from models import Recipe
from django.shortcuts import render, render_to_response, get_object_or_404, RequestContext, HttpResponse


# Create your views here.

def view_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    context = {
        "recipe_name": recipe.name,
    }
    #return render_to_response('recipe/view.html', context, context_instance=RequestContext(request))
    return render(request,'recipe/view.html', context)
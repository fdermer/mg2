# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from models import Recipe


# Create your views here.

class RecipeList(generic.ListView):
    model = Recipe
    template_name = 'recipe/recipe_list.html'
    context_object_name = 'recipe_list'
    paginate_by = 10

    def get_queryset(self):
        """Return the last five published recipes."""
        return Recipe.objects.order_by('id')[:555]

class RecipeDetail(generic.DetailView):
    model = Recipe
    template_name = 'recipe/recipe_view.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation
        context = super(RecipeDetail, self).get_context_data(**kwargs)

        # Add more context
        # context['image_folder'] = hashlib.md5(self.object.image_name.encode('utf-8')).hexdigest()[:1]

        return context


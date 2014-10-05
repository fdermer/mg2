# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from models import Recipe
import hashlib

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'recipe/index.html'
    #context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """Return the last five published recipes."""
        return Recipe.objects.order_by('-id')[:5]

class RecipeDetail(generic.DetailView):
    model = Recipe
    template_name = 'recipe/wp-template.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation
        context = super(RecipeDetail, self).get_context_data(**kwargs)

        # Add more context
        context['image_folder'] = hashlib.md5(self.object.image_name.encode('utf-8')).hexdigest()[:1]

        return context


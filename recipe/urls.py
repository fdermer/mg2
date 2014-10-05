from django.conf.urls import patterns, url

from recipe import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'weetest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^(?P<pk>\d+)/$', views.RecipeDetail.as_view(), name='RecipeDetail'),
    #url(r'^(?P<recipe_id>.+)/$', 'recipe.views.view_recipe', name='view_recipes'),
    #url(r'^recipe$', 'recipe.views.recipeazera', name='recipe'),
    #url(r'^admin/', include(admin.site.urls)),
)

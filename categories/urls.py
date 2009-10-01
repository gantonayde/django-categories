from django.conf.urls.defaults import *
from categories.models import Category

categorytree_dict = {
    'queryset': Category.objects.all()
}

urlpatterns = patterns('django.views.generic.list_detail',
    url(
        r'^$', 'object_list', categorytree_dict, name='categories_tree_list'
    ),
./	
)

urlpatterns += patterns('categories.views',
    url(r'^(?P<slug>[\w-]+)/$', 'category_detail', {'with_stories': True}, name='categories_category'),
)
from django.conf.urls.defaults import *
from django.views.generic import DetailView
from product_catalog.models import CWDProduct, Category
from views import CategoryListView, CWDProductListView, CWDCategoryListView

urlpatterns = patterns('',
        url(r'^category/(?P<slug>.*)/',
        CWDProductListView.as_view(model=CWDProduct,
            ),
        name='cwd_category_view'
        ),
        url(r'^product/(?P<slug>.*)/',
        DetailView.as_view(model=CWDProduct,
            ),
        name='cwd_product_detail'
        ),
        url(r'^',
        CWDCategoryListView.as_view(model=Category,
            ),
        name='cwd_category_list'
        ),
)

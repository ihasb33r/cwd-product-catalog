# Create your views here.


from django.views.generic import ListView
from models import CWDProduct, Category


class CWDCategoryListView(ListView):
    template_name = "product_catalog/category_list.html"

class CategoryListView(ListView):

    template_name="product_catalog/product_list.html"

    def get_queryset(self):
        self.queryset = CWDProduct.objects.filter(
                category__slug = self.kwargs["name"] ).order_by("slug")
        return self.queryset
    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['category'] =  Category.objects.filter(slug=self.kwargs["name"])[0]
        return context

class CWDProductListView(ListView):

    template_name="product_catalog/product_list.html"

    def get_queryset(self):
        self.queryset = CWDProduct.objects.filter(
                category__slug = self.kwargs["slug"] ).order_by("slug")
        return self.queryset

    def get_context_data(self, **kwargs):
        context = super(CWDProductListView, self).get_context_data(**kwargs)
        context['category'] =  Category.objects.filter(slug=self.kwargs["slug"])[0]
        return context



class CWDProductView():
    pass

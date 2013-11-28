from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from menu import MyShopProductCategoryMenu

class ProductCatalogAppHook(CMSApp):
    name = _("Product Catalog App Hook")
    urls = ["product_catalog.urls"]
    menus = [MyShopProductCategoryMenu]

apphook_pool.register(ProductCatalogAppHook)

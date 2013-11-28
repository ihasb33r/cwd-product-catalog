from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu
from cwd_product_catalog.models import Category

class MyShopProductCategoryMenu(CMSAttachMenu):

    name = _("Categorii de Produse")

    def get_nodes(self, request):
        nodes = []
        for category in Category.objects.all():
            if category.menu_entry:
                node = NavigationNode(
                    category.name,
                    category.get_absolute_url(),
                    category.name,
                    0,
                )
                nodes.append(node)
        return nodes

menu_pool.register_menu(MyShopProductCategoryMenu)



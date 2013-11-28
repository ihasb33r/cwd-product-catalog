from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from models import ShowCategoryPluginModel

class ShowCategoryPlugin(CMSPluginBase):
    model = ShowCategoryPluginModel
    name = _("Show Product Category ")
    render_template = "product_catalog/show_category_plugin.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(ShowCategoryPlugin)

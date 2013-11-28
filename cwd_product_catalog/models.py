from django.db import models
from django.db.models.signals import post_save
from filer.fields.image import FilerImageField
from cms.models.fields import PlaceholderField
from cms.models.pluginmodel import CMSPlugin
from django.core.urlresolvers import reverse
from django.dispatch import receiver


class Category(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, default=None)
    name = models.CharField(max_length=100)
    image = FilerImageField(blank=True, null=True, default=None)
    description = PlaceholderField("product_catalog_category_description")
    slug = models.SlugField()
    menu_entry = models.BooleanField(default=True)
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('cwd_category_view', args=[self.slug])
    class Meta:
        pass

@receiver(post_save, sender=Category)
def postCategorySave(sender, **kwargs):
    try:
        from menus.menu_pool import menu_pool
        menu_pool.clear()
    except:
        pass


class CWDProduct(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    image = FilerImageField(blank=True, null=True, default=None)
    description = PlaceholderField("product_catalog_product_description")
    category = models.ManyToManyField(Category)
    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ['name']


class ShowCategoryPluginModel(CMSPlugin):
    category = models.ForeignKey(Category)
    number_of_items = models.IntegerField(blank=True, null=True, default=10)

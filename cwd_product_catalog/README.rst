=====
CWD Product Catalog
=====

an attempt for a product catalog for django cms with a plugin and cms app hook

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'cwd_product_catalog',
    )


2. Run `python manage.py syncdb --all ; python manage.py migrate --fake` to create the models.

3. Start the development server and visit http://127.0.0.1:8000/admin/
   to create add items.

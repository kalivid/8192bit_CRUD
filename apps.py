from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules

class BitCrudConfig(AppConfig):
    name = 'bit_CRUD'

    def ready(self):
        autodiscover_modules('bit_CRUD')
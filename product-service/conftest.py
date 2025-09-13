import os
import django
import pytest

# Устанавливаем переменную окружения
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "product_service.settings")

# Настраиваем Django
django.setup()

@pytest.fixture(scope='session')
def db_setup():
    """Фикстура для инициализации базы данных"""
    pass
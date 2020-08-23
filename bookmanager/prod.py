# -*- coding: utf-8 -*-
# flake8: noqa
from .settings import *

DB_USER = get_env_variable("DB_USER", default_value="book")
DB_PASSWORD = get_env_variable("DB_PASSWORD", default_value="12345678")
DB_HOST = get_env_variable("DB_HOST", default_value="0.0.0.0")
DB_PORT = get_env_variable("DB_PORT", default_value="3306")
DB_NAME = get_env_variable("DB_NAME", default_value="book")

REDIS_SERVE = get_env_variable("REDIS_HOST", default_value="127.0.0.1")
REDIS_PORT = get_env_variable("REDIS_PORT", default_value=6379)
REDIS_DB = get_env_variable("REDIS_DB", default_value=0)
REDIS_DECODE_RESPONSES = True


ENV = "prod"
STATIC_ROOT = "/var/www/book/static/"
DEBUG = True
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": DB_NAME,
        "USER": DB_USER,
        "PASSWORD": DB_PASSWORD,
        "HOST": DB_HOST,
        "PORT": DB_PORT,
        "OPTIONS": {"charset": "utf8mb4",},
    }
}
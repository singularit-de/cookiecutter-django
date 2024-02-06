"""
Minimal configuration for collecting static files. For example the command is independent of a connected database.
"""
# Relative Imports
from .base import *  # noqa

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """
    Define separate directory for static files
    """
    location = settings.STATICFILES_LOCATION
    
class MediaStorage(S3Boto3Storage):
    """
    Define separate directory for media files
    """
    location = settings.MEDIAFILES_LOCATION
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings

class StaticStorage(FileSystemStorage):
    def __init__(self, location=None, base_url=None):
        location = os.path.join(settings.BASE_DIR, 'static', 'medical_histories')
        base_url = '/static/medical_histories/'
        super().__init__(location, base_url)

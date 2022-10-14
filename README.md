![PyPI](https://img.shields.io/pypi/v/drf_filestream_api)
![GitHub last commit](https://img.shields.io/github/last-commit/suqingdong/drf_filestream)

# A file upload application for DjangoRestFramework

### Installation
```bash
python3 -m pip install drf_filestream_api
```

### Usage
- edit `project/settings.py`

```python
INSTALL_APPS += [
    'drf_filestream',
]

MEDIA_ROOT = 'data/'  # default: /

FILE_UPLOAD_TO = 'upload/%Y/%m/%d'   # support strftime format, default: MEDIA_ROOT
FILE_UPLOAD_MAX_SIZE = '10M'              # limit max file size, default: None
```

- edit `project/urls.py`

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/file/', include('drf_filestream.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### API
![](https://suqingdong.github.io/drf_filestream/gallery/api.png)

### Demo
```bash
git clone https://github.com/suqingdong/drf_filestream

cd demo

python3 -m pip install -r requirements.txt

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py createsuperuser

python3 manage.py runserver
```



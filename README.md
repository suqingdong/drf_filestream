![PyPI](https://img.shields.io/pypi/v/drf_filestream)
![GitHub last commit](https://img.shields.io/github/last-commit/suqingdong/drf_filestream)

# A file stream application for DjangoRestFramework

### Installation
```bash
python3 -m pip install drf_filestream
```

### Usage
- edit `project/settings.py`

```python
from rest_framework import permissions

INSTALL_APPS += [
    'drf_filestream',
]

MEDIA_ROOT = 'data/'  # default: /

FILE_ACCESS_PERMISSIONS = [permissions.IsAuthenticated]
```

### Demo
```bash
git clone https://github.com/suqingdong/drf_filestream.git

cd demo

python3 -m pip install -r requirements.txt

python3 manage.py createsuperuser

python3 manage.py runserver
```

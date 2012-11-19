from settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(project_path, 'codes-in-process.db'),
    }
}

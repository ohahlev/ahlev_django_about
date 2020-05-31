# TMP APPLICATION
![pypi](https://img.shields.io/pypi/v/tmp) ![pypi](https://img.shields.io/pypi/status/tmp)

> Replace tmp with real application name

## install from this repository
### clone

> git clone https://github.com/ohahlev/tmp.git

### go to directory tmp

> cd tmp

### create installer package

> make package

### install package

cd into project directory

> cd ../my_project_dir

install ahlev_django_about_us from the project directory

> pip install ../tmp/dist/tmp-0.0.1.tar.gz


## install from pypi
[tmp](https://pypi.org/project/tmp/)

## project configuration
### add tmp app to settings.py

    INSTALLED_APPS = [
      'tmp',  # add this line
      ...
    ]


### make sure these lines exist in settings.py

    STATICFILES_DIRS = [
      os.path.join(BASE_DIR, "static")
    ]
    STATIC_URL = '/static/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
    MEDIA_URL = '/medias/'

### make sure these lines exists in urls.py

    # replace tmp with application name
    from django.conf import settings
    from django.conf.urls.static import static
    from django.urls import include, path

    urlpatterns = [
       path('tmp/', include('tmp.urls')),
       path('admin/', admin.site.urls),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


## screenshots

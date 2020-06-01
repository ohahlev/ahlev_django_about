# About Application
![pypi](https://img.shields.io/pypi/v/ahlev_django_about) ![pypi](https://img.shields.io/pypi/status/ahlev_django_about)

### clone

> git clone https://github.com/ohahlev/ahlev_django_about.git

### go to directory ahlev_django_about

> cd ahlev_django_about

### create installer package

> make package

### install package

cd into project directory

> cd ../my_project_dir

install ahlev_django_about from the project directory

> pip install ../ahlev_django_about/dist/ahlev_django_about-0.0.1.tar.gz


## install from pypi
[ahlev_django_about](https://pypi.org/project/tmp/)

## project configuration
### add about to settings.py

    INSTALLED_APPS = [
      'about',  # add this line
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
      path('about/', include('about.urls')),
       path('admin/', admin.site.urls),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


## screenshots
### dashboard
![](screenshots/dashboard.jpg)

### list
![](screenshots/list.png)

### edit
![](screenshots/edit.png)

### change history
![](screenshots/change-history.png)


# djangocms SVG Image plugin

Since djangocms_picture pluging does not allow us to use SVG files, we code this small plugin. It is inteded to be very simple but useful to insert SVG images on our pages as need it.

## Setup

You can install the plugin by:

1. Executing the following command:

```bash
pip install git+https://github.com/pablo-pinargote/djangocms_svgimage
```

2. Adding the plugin to your CMS INSTALLED_APPS settings variable.

```python
INSTALLED_APPS = [
    ...,
    'djangocms_svgimage',
]
```

3. Executing plugin migrations to create the corresponding model:

```bash
python manage.py makemigrations djangocms_svgimage
python manage.py migrate djangocms_svgimage
```

## Using the plugin

Using the plugin is very straightforward, we just select it from the plugin's list, select the file and enter the image width and height parameters accordingly.

![](readme-support-files/svgimage-01.png)

![](readme-support-files/svgimage-02.png)

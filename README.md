Django Draggable Sorting
========================

Simple plugin for draggable sorting Django inlines. Works great with [django-suit](https://github.com/darklow/django-suit)

## Requirements

- jQuery for jquery-ui. 

This package DOES NOT ship with jQuery.

## Quick start

1. Install:
    ```
       pip install -e git+https://github.com/diveru4i/django-draggable_sorting.git#egg=draggable_sorting
    ```
2. Add "draggable_sorting" to your INSTALLED_APPS setting for collectstatic
    ```python
       INSTALLED_APPS = (
           ...
           'draggable_sorting',
           ...
           
       )
    ```
3. Run 
   ```
      ./manage.py collectstatic
   ```
4. You'll need to add field "order" to your model:
    ```python
        class YourModel(admin.Model):
            order = models.PositiveSmallIntegerField(default=1)
            ...
            
            class Meta:
                ordering = ['order']
    ```
5. In your ```admin.py```:
   ```python
      ...
      from draggable_sorting import DraggableMixin
      ...
      
      class YourModelAdmin(DraggableMixin, admin.ModelAdmin):
          ...
   ```


**Based on this thread**

- <https://djangosnippets.org/snippets/1053/>

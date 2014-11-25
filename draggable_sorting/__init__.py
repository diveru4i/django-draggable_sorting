# -*- coding: utf-8 -*-
__version__ = '0.0.1'


class DraggableMixin(object):
    class Media:
        js = (
            '/static/draggable_sorting/vendor/jquery-ui/jquery-ui.js',
            '/static/draggable_sorting/js/draggable.js',
            '/static/draggable_sorting/js/deleteAll.js',
        )
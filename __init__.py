# -*- coding: utf-8 -*-

class DraggableMixin(object):
    class Media:
        js = (
            '/static/draggable_sorting/vendor/jquery-ui/jquery-ui.js',
            '/static/draggable_sorting/js/draggable.js',
            '/static/draggable_sorting/js/deleteAll.js',
        )
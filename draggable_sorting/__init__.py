# -*- coding: utf-8 -*-
__version__ = '0.0.2'


class DraggableMixin(object):
    def __init__(self, *args, **kwargs):
        self.Media.js = list(self.Media.js) + [
            '/static/draggable_sorting/vendor/jquery-ui/jquery-ui.js',
            '/static/draggable_sorting/js/draggable.js',
        ]
        super(Dr, self).__init__(*args, **kwargs)

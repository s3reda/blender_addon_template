bl_info = {
    "name": "Blank Addon",
    "author": "sereda",
    "version": (0, 0, 1),
    "blender": (4, 1, 0),
    "location": "",
    "description": "",
    "warning": "Test",
    "doc_url": "",
    "category": "",
}

import bpy
from .ops import module
from . import ui
from . import preferences


_classes = (
    module.ADDONNAME_OT_MOD_my_operator,
    module.OBJECT_OT_my_operator
)

# register, unregister = bpy.utils.register_classes_factory(_classes)


def register():
    for cls in _classes:
        bpy.utils.register_class(cls)
    preferences.register()
    ui.register()


def unregister():
    for cls in reversed(_classes):
        bpy.utils.unregister_class(cls)
    preferences.unregister()
    ui.unregister()
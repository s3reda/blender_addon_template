bl_info = {
    "name": "Blank Addon",
    "author": "sereda",
    "version": (0, 0, 1),
    "blender": (4, 1, 0),
    "location": "F3",
    "description": "",
    "warning": "alpha",
    "doc_url": "",
    "category": "Modifier",
}

import bpy
from .ops import data_transfer


_classes = [data_transfer.MODQACT_OT_MOD_data_transfer, ]

def register():
    for cls in _classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(_classes):
        bpy.utils.unregister_class(cls)
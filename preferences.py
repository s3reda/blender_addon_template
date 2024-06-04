import bpy

class MyAddonPreferences(bpy.types.AddonPreferences):
    # It should be the default way to declare(?) the addon preferences.
    # bl_idname = __package__
    # That's how it works now, not sure why exactly.
    bl_idname = __package__.split('.')[0]  # Use the top-level package name

    # Examples of properties types:
    # String Property
    my_string: bpy.props.StringProperty(
        name="String Value",
        description="A string property for the addon",
        default="Default Value"
    )

    # Integer Property
    my_int: bpy.props.IntProperty(
        name="Integer Value",
        description="An integer property for the addon",
        default=10,
        min=1,
        max=100
    )

    # Float Property
    my_float: bpy.props.FloatProperty(
        name="Float Value",
        description="A float property for the addon",
        default=1.0,
        min=0.0,
        max=10.0
    )

    # Boolean Property
    my_bool: bpy.props.BoolProperty(
        name="Boolean Value",
        description="A boolean property for the addon",
        default=False
    )

    # Enum Property
    my_enum: bpy.props.EnumProperty(
        name="Enum Value",
        description="An enum property for the addon",
        items=[
            ('OPT_A', "Option A", "Description of Option A"),
            ('OPT_B', "Option B", "Description of Option B"),
            ('OPT_C', "Option C", "Description of Option C")
        ],
        default='OPT_A'
    )

    # Path Property
    my_path: bpy.props.StringProperty(
        name="Path Value",
        description="A path property for the addon",
        subtype='FILE_PATH',
        default=""
    )

    # Directory Property
    my_dir: bpy.props.StringProperty(
        name="Directory Value",
        description="A directory property for the addon",
        subtype='DIR_PATH',
        default=""
    )

    # File Property
    my_file: bpy.props.StringProperty(
        name="File Value",
        description="A file property for the addon",
        subtype='FILE_NAME',
        default=""
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "my_string")
        layout.prop(self, "my_int")
        layout.prop(self, "my_float")
        layout.prop(self, "my_bool")
        layout.prop(self, "my_enum")
        layout.prop(self, "my_path")
        layout.prop(self, "my_dir")
        layout.prop(self, "my_file")

def register():
    bpy.utils.register_class(MyAddonPreferences)

def unregister():
    bpy.utils.unregister_class(MyAddonPreferences)

import bpy
from ..preferences import MyAddonPreferences

class ADDONNAME_OT_MOD_my_operator(bpy.types.Operator):
    bl_idname = "addonname.my_operator"
    bl_label = "My Operator Name"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return context.active_object #and len(bpy.context.selected_objects)>1
        # return context.area.type == 'VIEW_3D' and context.active_object and len(bpy.context.selected_objects)>1
    
    def execute(self, context):
    
        def myfunction_example():
            return bpy.context.active_object.name
            
        def main():
            print (myfunction_example())
            
        main()
        self.report({'INFO'}, "message")
        return {'FINISHED'}


class OBJECT_OT_my_operator(bpy.types.Operator):
    bl_idname = "object.my_operator"
    bl_label = "My Operator"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        # Access the addon preferences.
        # That is how the preferences should be accessable if they are in the same directory
        # prefs = context.preferences.addons[__package__].preferences
        # I`m not sure why, but this need to be done to access preferences from relative parent folder.
        # Yet it works fine so far.
        addon_name = __package__.split('.')[0]  # Get the top-level package name
        prefs = context.preferences.addons[addon_name].preferences
    
        # Retrieve the properties
        my_string = prefs.my_string
        my_int = prefs.my_int
        my_float = prefs.my_float
        my_bool = prefs.my_bool
        my_enum = prefs.my_enum
        my_path = prefs.my_path
        my_dir = prefs.my_dir
        my_file = prefs.my_file

        # Use the properties (for demonstration, we'll just print them)
        self.report({'INFO'}, f"String: {my_string}")
        self.report({'INFO'}, f"Integer: {my_int}")
        self.report({'INFO'}, f"Float: {my_float}")
        self.report({'INFO'}, f"Boolean: {my_bool}")
        self.report({'INFO'}, f"Enum: {my_enum}")
        self.report({'INFO'}, f"Path: {my_path}")
        self.report({'INFO'}, f"Directory: {my_dir}")
        self.report({'INFO'}, f"File: {my_file}")
    
        return {'FINISHED'}

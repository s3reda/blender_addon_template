import bpy
from .ops import module

class ADDONNAME_PT_panel(bpy.types.Panel):
#It's just another regular panel.
#Do not use it if not necessary (too much of the panels).
    bl_label = "Template Addon Panel"
    bl_idname = "ADDONNAME_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Template Addon"
    
    def draw(self, context):
        layout = self.layout
        layout.operator(module.ADDONNAME_OT_MOD_my_operator.bl_idname, text="Run My Operator")

# def menu(self, context): # A simple button without submenu. Use this if the addon has one button.
    # layout = self.layout
    # layout.separator()
    # layout.operator(module.ADDONNAME_OT_MOD_my_operator.bl_idname, )
    
def menu(self, context): #This is more advanced setup - it's a main menu which is attached to Blender's menus.
    layout = self.layout
    layout.menu("VIEW3D_MT_object_my_addon_menu", text='Custom', icon_value=31)

class MyAddonSubMenu(bpy.types.Menu): #This is a submenu which is attached to menu. Must be registered though.
    bl_idname = "VIEW3D_MT_object_my_addon_menu"
    bl_label = "My Addon"
    
    def draw(self, context):
        layout = self.layout
        layout.operator(module.ADDONNAME_OT_MOD_my_operator.bl_idname, )
        layout.separator()# You could use separators
        layout.operator(module.OBJECT_OT_my_operator.bl_idname, )
        # You can add more items to the submenu if needed

def register():
    bpy.utils.register_class(ADDONNAME_PT_panel)
    bpy.utils.register_class(MyAddonSubMenu)
    bpy.types.VIEW3D_MT_object_context_menu.append(menu) # Appending our menu to the other menu.


def unregister():
    bpy.utils.unregister_class(ADDONNAME_PT_panel)
    bpy.utils.unregister_class(MyAddonSubMenu)
    bpy.types.VIEW3D_MT_object_context_menu.remove(menu)
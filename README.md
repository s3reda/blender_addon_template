# blender_addon_template
A template of an addon for Blender with basic modular structure.

Great article about naming conventions for Blender addons:
https://darkfallblender.blogspot.com/2020/07/blender-python-tutorial-class-naming.html

I wanted to make the addon scalable, so all the basic features are separated to different modules.

How to use:

Write your functionaliity inside ops package.
I suggest creating one module per operator / logical group of operators.
Set up the addon preferences inside the preferences module.
Create the UI inside the ui module.
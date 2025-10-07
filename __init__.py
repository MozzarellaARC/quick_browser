# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy

def toggle_asset_browser_split():
    screen = bpy.context.screen
    asset_area = next((a for a in screen.areas if a.type == 'FILE_BROWSER' and a.ui_type == 'ASSETS'), None)

    if asset_area:
        with bpy.context.temp_override(area=asset_area):
            bpy.ops.screen.area_close()
        return

    view3d_area = next((a for a in screen.areas if a.type == 'VIEW_3D'), None)
    if not view3d_area:
        return

    region = next((r for r in view3d_area.regions if r.type == 'WINDOW'), None)
    if not region:
        return

    with bpy.context.temp_override(area=view3d_area, region=region):
        bpy.ops.screen.area_split(direction='VERTICAL', factor=0.5)

    new_area = screen.areas[-1]
    new_area.type = 'FILE_BROWSER'
    new_area.ui_type = 'ASSETS'

class QuickAssetBrowser_Operator(bpy.types.Operator):
    bl_idname = "wm.quick_asset_browser"
    bl_label = "Toggle Asset Browser"
    bl_description = "Toggle the Asset Browser panel"

    def execute(self, context):
        toggle_asset_browser_split()
        return {'FINISHED'}

class QuickAssetBrowser_Preferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    def draw(self, context):
        layout = self.layout
        layout.label(text="No preferences available.")

def register():
    bpy.utils.register_class(QuickAssetBrowser_Operator)
    bpy.utils.register_class(QuickAssetBrowser_Preferences)

def unregister():
    bpy.utils.unregister_class(QuickAssetBrowser_Operator)
    bpy.utils.unregister_class(QuickAssetBrowser_Preferences)
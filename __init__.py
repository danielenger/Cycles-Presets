#    Cycles Presets
#    Copyright (C) 2019 Daniel Engler

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from .cycles_presets import *
import bpy

bl_info = {
    "name": "Cycles Presets",
    "description": "Save Cycles Presets",
    "author": "Daniel Engler",
    "version": (0, 0, 3),
    "blender": (2, 82, 0),
    "location": "Properties > Render",
    "category": "Render"
}


classes = (
    CYCLESPRESETS_PT_panel,
    CYCLESPRESETS_OT_AddPreset,
    CYCLESPRESETS_MT_DisplayPresets,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()

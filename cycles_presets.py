import inspect
from pathlib import Path

import bpy
from bl_operators.presets import AddPresetBase
from bpy.props import StringProperty, BoolProperty
from bpy.types import Menu, Operator, Panel
from mathutils import Color

PRESET_SUBDIR = "cycles_presets"
EXCLUDE_LIST = ["__", "bl_rna", "rna_type", "register", "unregister"]
CYCLES_KEY_PREFIX = "cycles"
PRESET_HEAD = """import bpy
cycles = bpy.context.scene.cycles
render = bpy.context.scene.render

"""


def get_cycles_values():
    pre_vals = {}
    cycles_settings_list = inspect.getmembers(bpy.context.scene.cycles)
    for elem in cycles_settings_list:
        key, value = elem
        if all(item not in key for item in EXCLUDE_LIST):
            if isinstance(value, Color):
                val = (value.r, value.g, value.b)
            elif isinstance(value, str):
                val = f"'{value}'"
            else:
                val = value
            pre_vals[f"{CYCLES_KEY_PREFIX}.{key}"] = val
    return pre_vals


class CYCLESPRESETS_MT_DisplayPresets(Menu):
    bl_label = "Cycles Presets"
    preset_subdir = PRESET_SUBDIR
    preset_operator = "script.execute_preset"
    draw = Menu.draw_preset


class CYCLESPRESETS_OT_AddPreset(AddPresetBase, Operator):
    bl_idname = "cyclespresets.preset_add"
    bl_label = "Add Cycles Preset"
    preset_menu = "CYCLESPRESETS_MT_DisplayPresets"

    preset_defines = ["cycles = bpy.context.scene.cycles",
                      "render = bpy.context.scene.render"]

    preset_subdir = PRESET_SUBDIR


class CYCLESPRESETS_OT_AddCyclesPreset(bpy.types.Operator):
    bl_idname = "cyclespresets.add_cycles_preset"
    bl_label = "Add Cycles Preset"

    preset_name: StringProperty(name="Name",
                                description="Save ",
                                default="")

    film_transparent: BoolProperty(name="Save Film Transparent",
                                        description="",
                                        default=True)

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "film_transparent")
        layout.prop(self, "preset_name")

    def execute(self, context):
        if self.preset_name == "":
            self.report({'INFO'}, "Preset needs a name!")
            return {'CANCELLED'}

        cycles_values = {}
        cycles_values[f"render.use_motion_blur"] = bpy.context.scene.render.use_motion_blur
        cycles_values[f"render.motion_blur_shutter"] = bpy.context.scene.render.motion_blur_shutter
        if self.film_transparent:
            cycles_values[f"render.film_transparent"] = bpy.context.scene.render.film_transparent
        cycles_values.update(get_cycles_values())

        preset_lines = [PRESET_HEAD]
        for key, value in cycles_values.items():
            line = f"{key} = {value}\n"
            preset_lines.append(line)

        preset_path = Path(
            bpy.utils.resource_path('USER')) / Path(
                f"scripts/presets/{PRESET_SUBDIR}/{self.preset_name}.py")

        with open(preset_path, 'w') as preset_file:
            preset_file.writelines(preset_lines)

        return {'FINISHED'}


class CYCLESPRESETS_PT_panel(Panel):
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"
    bl_label = "Cycles Presets"
    bl_category = "Cycles Presets"

    @classmethod
    def poll(cls, context):
        if context.scene.render.engine == 'CYCLES':
            return True

    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)
        row.menu(CYCLESPRESETS_MT_DisplayPresets.__name__,
                 text=CYCLESPRESETS_MT_DisplayPresets.bl_label)
        row.operator("cyclespresets.add_cycles_preset",
                     text="", icon='ADD')
        row.operator(CYCLESPRESETS_OT_AddPreset.bl_idname,
                     text="", icon='REMOVE').remove_active = True

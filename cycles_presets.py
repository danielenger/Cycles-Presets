
import bpy
from bl_operators.presets import AddPresetBase
from bpy.types import Menu, Operator, Panel


PRESET_SUBDIR = "cycles_presets"


class CYCLESPRESETS_MT_display_presets(Menu):
    bl_label = "Cycles Presets"
    preset_subdir = PRESET_SUBDIR
    preset_operator = "script.execute_preset"
    draw = Menu.draw_preset


class CYCLESPRESETS_AddPresetObjectDisplay(AddPresetBase, Operator):
    bl_idname = "cyclespresets.preset_add"
    bl_label = "Add Cycles Preset"
    preset_menu = "CYCLESPRESETS_MT_display_presets"

    preset_defines = ["cycles = bpy.context.scene.cycles"]

    preset_values = [
        "cycles.aa_samples",
        "cycles.ao_bounces",
        "cycles.ao_bounces_render",
        "cycles.ao_samples",
        "cycles.blur_glossy",
        "cycles.camera_cull_margin",
        "cycles.caustics_reflective",
        "cycles.caustics_refractive",
        "cycles.debug_bvh_layout",
        "cycles.debug_bvh_time_steps",
        "cycles.debug_bvh_type",
        "cycles.debug_cancel_timeout",
        "cycles.debug_opencl_device_type",
        "cycles.debug_opencl_kernel_type",
        "cycles.debug_opencl_mem_limit",
        "cycles.debug_reset_timeout",
        "cycles.debug_text_timeout",
        "cycles.debug_tile_size",
        "cycles.debug_use_cpu_avx",
        "cycles.debug_use_cpu_avx2",
        "cycles.debug_use_cpu_split_kernel",
        "cycles.debug_use_cpu_sse2",
        "cycles.debug_use_cpu_sse3",
        "cycles.debug_use_cpu_sse41",
        "cycles.debug_use_cuda_adaptive_compile",
        "cycles.debug_use_cuda_split_kernel",
        "cycles.debug_use_hair_bvh",
        "cycles.debug_use_opencl_debug",
        "cycles.debug_use_spatial_splits",
        "cycles.device",
        "cycles.dicing_camera",
        "cycles.dicing_rate",
        "cycles.diffuse_bounces",
        "cycles.diffuse_samples",
        "cycles.distance_cull_margin",
        "cycles.feature_set",
        "cycles.film_exposure",
        "cycles.film_transparent_glass",
        "cycles.film_transparent_roughness",
        "cycles.filter_type",
        "cycles.filter_width",
        "cycles.glossy_bounces",
        "cycles.glossy_samples",
        "cycles.light_sampling_threshold",
        "cycles.max_bounces",
        "cycles.max_subdivisions",
        "cycles.mesh_light_samples",
        "cycles.motion_blur_position",
        "cycles.name",
        "cycles.offscreen_dicing_scale",
        "cycles.pixel_filter_type",
        "cycles.preview_aa_samples",
        "cycles.preview_dicing_rate",
        "cycles.preview_pause",
        "cycles.preview_samples",
        "cycles.preview_start_resolution",
        "cycles.progressive",
        "cycles.rolling_shutter_duration",
        "cycles.rolling_shutter_type",
        "cycles.sample_all_lights_direct",
        "cycles.sample_all_lights_indirect",
        "cycles.sample_clamp_direct",
        "cycles.sample_clamp_indirect",
        "cycles.samples",
        "cycles.sampling_pattern",
        "cycles.seed",
        "cycles.shading_system",
        "cycles.subsurface_samples",
        "cycles.texture_limit",
        "cycles.texture_limit_render",
        "cycles.tile_order",
        "cycles.transmission_bounces",
        "cycles.transmission_samples",
        "cycles.transparent_max_bounces",
        "cycles.use_animated_seed",
        "cycles.use_bvh_embree",
        "cycles.use_camera_cull",
        "cycles.use_distance_cull",
        "cycles.use_layer_samples",
        "cycles.use_progressive_refine",
        "cycles.use_square_samples",
        "cycles.volume_bounces",
        "cycles.volume_max_steps",
        "cycles.volume_samples",
        "cycles.volume_step_size",
    ]

    preset_subdir = PRESET_SUBDIR


class CYCLESPRESETS_PT_panel(Panel):
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"
    bl_label = "Cycles Presets"
    bl_category = "Cycles Presets"

    def draw(self, context):
        row = self.layout.row(align=True)
        row.menu(CYCLESPRESETS_MT_display_presets.__name__,
                 text=CYCLESPRESETS_MT_display_presets.bl_label)
        row.operator(CYCLESPRESETS_AddPresetObjectDisplay.bl_idname,
                     text="", icon='ZOOM_IN')
        row.operator(CYCLESPRESETS_AddPresetObjectDisplay.bl_idname,
                     text="", icon='ZOOM_OUT').remove_active = True

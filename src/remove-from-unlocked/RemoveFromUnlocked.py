bl_info = {
    "name": "Remove Selected From Unlocked",
    "author": "Bill Hails",
    "version": (1, 0),
    "blender": (3, 3, 1),
    "location": "View3D > Mesh > Clean Up > Remove from Unlocked Groups",
    "description": "Removes selected vertices from all unlocked vertex groups",
    "warning": "",
    "doc_url": "",
    "category": "Mesh",
}


import bpy
import bmesh

def remove_from_unlocked(self, context):
    # get active mesh
    obj = context.object
    me = obj.data

    # get bMesh representation
    bm = bmesh.from_edit_mesh(me)

    selected_vertex_indices = [v.index for v in bm.verts if (v.select and not v.hide)]

    vertex_groups = bpy.context.edit_object.vertex_groups
    bpy.ops.object.editmode_toggle()
    for vg in vertex_groups:
        if not vg.lock_weight:
            vg.remove(selected_vertex_indices)
    bpy.ops.object.editmode_toggle()


class MESH_OT_remove_from_unlocked(bpy.types.Operator):
    """Remove selected vertices from all unlocked vertex groups"""
    bl_idname = "mesh.remove_from_unlocked"
    bl_label = "Remove from Unlocked Groups"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return context.edit_object is not None

    def execute(self, context):
        remove_from_unlocked(self, context)
        return {'FINISHED'}

# Registration

def remove_from_unlocked_button(self, context):
    self.layout.operator(
        MESH_OT_remove_from_unlocked.bl_idname,
        text="Remove from Unlocked Groups",
        icon='PLUGIN')



def register():
    bpy.utils.register_class(MESH_OT_remove_from_unlocked)
    bpy.types.VIEW3D_MT_edit_mesh_clean.append(remove_from_unlocked_button)


def unregister():
    bpy.utils.unregister_class(MESH_OT_remove_from_unlocked)
    bpy.types.VIEW3D_MT_edit_mesh_clean.remove(remove_from_unlocked_button)


if __name__ == "__main__":
    register()

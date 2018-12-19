# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but without any warranty; without even the implied warranty of
#  merchantability or fitness for a particular purpose.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Finish Sewing",
    "author": "Bill Hails",
    "version": (1, 0),
    "blender": (2, 79, 0),
    "location": "View3D > Mesh > Clean up > Finish Sewing",
    "description": "Merge sets of vertices connected by edges without faces",
    "warning": "",
    "wiki_url": "https://github.com/billhails/blender-addons/blob/master/src/finish-sewing/README.md",
    "category": "Mesh",
    }
    
import bpy
import bmesh
from mathutils import Vector

class WHFinishSewing(bpy.types.Operator):
    """Merge sets of vertices connected by edges without faces (e.g. sewing springs)"""
    bl_idname = "mesh.finish_sewing"
    bl_label = "Finish Sewing"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        # Get the active mesh
        obj = bpy.context.edit_object
        me = obj.data

        # Get a BMesh representation
        bm = bmesh.from_edit_mesh(me)
        bm.faces.active = None

        # Find the set of all edges in the mesh
        # i.e. {A--B, B--C, D--E, E--F, G--H}
        # (where A, B, C etc. are vertices)
        all_edges = set()
        for edge in bm.edges:
            all_edges.add(edge)

        # Find the set of all edges with faces
        # i.e. {E--F, G--H}
        faced_edges = set()
        for face in bm.faces:
            for edge in face.edges:
                faced_edges.add(edge)

        # The set of edges without faces is the difference between those two sets
        # {A--B, B--C, D--E, E--F, G--H} - {E--F, G--H} = {A--B, B--C, D--E}
        unfaced_edges = all_edges - faced_edges

        # Build a set of all of the vertices belonging to those unfaced edges
        #
        # so for example if we have the set of edges:
        # {A--B, B--C, D--E}
        # we end up with the set of vertices:
        # {A, B, C, D, E}
        unfaced_edge_vertices = set()
        for edge in unfaced_edges:
            for vertex in edge.verts:
                unfaced_edge_vertices.add(vertex)

        # Put each vertex in its own set
        #
        # so if we have the set of vertices:
        # {A, B, C, D, E}
        # we end up with an array of singleton sets:
        # [{A}, {B}, {C}, {D}, {E}]
        vertex_sets = []
        for vertex in unfaced_edge_vertices:
            vertex_sets.append({vertex})

        # Merge sets of vertices that share an unfaced edge
        #
        # so for example if we have the set of unfaced edges:
        # {A--B, B--C, D--E}
        # and the array of singleton sets of their vertices:
        # [{A}, {B}, {C}, {D}, {E}]
        # Then we end up with an array of sets of vertices:
        # [{A, B, C}, {D, E}]
        for edge in unfaced_edges:
            (vertex_1, vertex_2) = edge.verts[:]
            for index, vertex_set in enumerate(vertex_sets):
                if vertex_1 in vertex_set:
                    index_1 = index
                if vertex_2 in vertex_set:
                    index_2 = index
            if index_1 != index_2:
                vertex_sets[index_1] |= vertex_sets[index_2]
                del vertex_sets[index_2]

        # Collapse each of those sets of vertices, at centre.
        # [A, B, C] => A
        # [D, E] => D
        for vertex_set in vertex_sets:
            bmesh.ops.pointmerge(bm, verts=list(vertex_set), merge_co=self.average_vectors(vertex_set))
            
        # Write the result back to the active mesh
        bmesh.update_edit_mesh(me, True)
        
        # Tell blender everything is ok
        return {'FINISHED'}

    def average_vectors(self, vertex_set):
        """average a set of vectors"""
        result = Vector()
        count = 0
        for vertex in vertex_set:
            result += vertex.co
            count += 1
        return result / count

def wh_finish_sewing_button(self, context):
    self.layout.operator(
        WHFinishSewing.bl_idname,
        text="Finish Sewing",
        icon='PLUGIN'
    )

def register():
    bpy.utils.register_class(WHFinishSewing)
    bpy.types.VIEW3D_MT_edit_mesh_clean.append(wh_finish_sewing_button)

def unregister():
    bpy.utils.unregister_class(WHFinishSewing)
    bpy.types.VIEW3D_MT_edit_mesh_clean.remove(wh_finish_sewing_button)

if __name__ == "__main__":
    register()

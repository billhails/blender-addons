# Remove From Unlocked

A simple add-on to remove selected vertices from all unlocked vertex groups.

## Use Case

If you are rigging and you parent your mesh to your armature with automatic weights, there may be loose parts
of your mesh, such as the tongue, teeth, eyeballs, eyelashes etc. that receive unwanted influence from
nearby bones.

The standard way to fix this is with weight painting, but if you know you only need a small number of vertex
groups to influence a piece of mesh, this add-on makes it a bit easier.

## Usage

1. Ensure that the vertex groups you want to preserve are locked, and all other vertex groups are unlocked.
2. In edit mode, select the vertices you want to disassociate from the unlocked vertex groups.
3. Click on Mesh > Clean Up > Remove from Unlocked Groups.

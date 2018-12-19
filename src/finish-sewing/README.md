# Finish Sewing

This little plugin saves you some time when using cloth simulations
with sewing springs to manufacture clothing.

It applies to the following scenario:

* You've created some clothing meshes, with springs (edges without faces).
* You've given the meshes a cloth simulation.
* You've given your mannequin a collision modifier.
* You've run the simulation.
* You're happy with the result.
* You've applied the cloth simulation.

Normally you'd then have to go in to edit mode on the resulting
mesh and clean up all of those springs, by selecting pairs or sets
of vertices and doing "merge at center" for every stitch individually.
This can be very tedious and fiddly for a complex piece of clothing
with many springs/stitches.

The FinishSewing add-on does this step for you:

* Tab in to edit mode on your clothing mesh.
* Select `Mesh > Clean up > Finish Sewing`
* Tab out of edit mode.

Here's a screenshot of a mesh before running the add-on:

![Before](https://raw.githubusercontent.com/billhails/blender-addons/master/images/finish-sewing-before.png)

And this is after:

![After](https://raw.githubusercontent.com/billhails/blender-addons/master/images/finish-sewing-after.png)

Here's how to find it in the menus:

![Menu](https://raw.githubusercontent.com/billhails/blender-addons/master/images/finish-sewing-menu.png)

## Installation

* Download the `FinishSewing.py` file.
* Open `File > User preferences` in Blender.
* Choose the `Add-ons` tab.
* Choose `Install add-on from file...`
* Browse to the file you just downloaded.
* Install it.
* Check the little tick box to activate it.

## Testing Notes

I've tested this with 2.79a only, I've no idea if it'll work on 2.8
yet, though it doesn't use the shrinking vertex group so it should
be fairly easy to port.

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
mesh and clean up all of those springs, by selecting vertices and
doing "merge at center" for every stitch individually.  This can
be very tedious and fiddly for a complex piece of clothing with
many stitching springs.

The FinishSewing add-on does this last step for you.

Here's a screenshot of a mesh before running the add-on:

![Before](https://raw.githubusercontent.com/billhails/blender-addons/master/images/finish-sewing-before.png)

And this is after:

![After](https://raw.githubusercontent.com/billhails/blender-addons/master/images/finish-sewing-after.png)

Here's how to find it in the menus:

![Menu](https://raw.githubusercontent.com/billhails/blender-addons/master/images/finish-sewing-menu.png)

## Installation

* Download the current release.
* unpack the downloaded file.
* Open `File > User preferences` in Blender 2.79, or `Edit > User Preferences` in 2.80.
* Choose the `Add-ons` tab.
* Choose `Install add-on from file...`
* Browse to the directory you just unpacked and go to the `src/finish-sewing` directory in there.
* Select `FinishSewing279.py` if you're still on blender 2.79, or `FinishSewing.py` if you're on 2.80.
* Install  it.
* Check the little tick box to activate it.

## Usage

*  Make sure you are in edit mode on your clothing mesh.
* Select `Mesh > Clean up > Finish Sewing`

## How it Works

In a bit more detail, it looks through the mesh to find all edges
that don't have faces. It assumes these are all sewing springs. It
collects sets of vertices reachable by traversing these edges.
Typically these sets are just pairs of vertices but it can cope
with more complex situations.  For each set of vertices, it
does "merge at center".

## Testing Notes

There are two versions of the script: `FinishSewing279.py` which has been
tested on Blender 2.79a, and `FinishSewing.py` which was tested on Blender 2.80 beta
(build `blender-2.80.0-git20181221.7a26e930a8c0-x86_64`).
